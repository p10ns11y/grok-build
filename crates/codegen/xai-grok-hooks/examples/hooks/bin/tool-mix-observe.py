#!/usr/bin/env python3
"""ToolMixSnapshot: offline join of chat_history tool_calls → tool_results.

Standard post-session recipe for harness learning-cost ranking (calls ×
result volume × turns). Safe to run anytime; optional SessionEnd hook writes
`tool_mix.json` next to the session.

Usage:
  # Analyze one or more sessions (dir or chat_history.jsonl)
  python3 tool-mix-observe.py ~/.grok/sessions/<enc-cwd>/<session-id>

  # Resolve from hook env (GROK_SESSION_ID + workspace) and write tool_mix.json
  python3 tool-mix-observe.py --from-env --write

  # Largest multi-tool sessions under a workspace encoding
  python3 tool-mix-observe.py --workspace-dir ~/.grok/sessions/<enc-cwd> --pick-largest 3

Reads session files only; never mutates the product tree.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import quote


def grok_home() -> Path:
    raw = os.environ.get("GROK_HOME") or os.path.join(os.path.expanduser("~"), ".grok")
    return Path(raw).expanduser()


def encode_cwd_dirname(cwd: str) -> str:
    """Match short-path branch of xai_grok_config::encode_cwd_dirname (url encode).

    Long paths use a blake3 slug form; for those, prefer find_session_dir().
    """
    return quote(cwd, safe="")


def find_session_dir(session_id: str, home: Path | None = None) -> Path | None:
    """Locate session dir by id under ~/.grok/sessions (any encoded cwd)."""
    home = home or grok_home()
    root = home / "sessions"
    if not root.is_dir():
        return None
    # Fast path: env workspace encoding
    ws = os.environ.get("GROK_WORKSPACE_ROOT") or os.environ.get("CLAUDE_PROJECT_DIR")
    if ws:
        candidate = root / encode_cwd_dirname(ws) / session_id
        if (candidate / "chat_history.jsonl").is_file():
            return candidate
    # Scan (one-shot; SessionEnd is rare)
    for cwd_dir in root.iterdir():
        if not cwd_dir.is_dir():
            continue
        candidate = cwd_dir / session_id
        if (candidate / "chat_history.jsonl").is_file():
            return candidate
    return None


def percentile(sorted_vals: list[int], p: float) -> int | None:
    if not sorted_vals:
        return None
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    k = min(len(sorted_vals) - 1, max(0, math.ceil(p / 100.0 * len(sorted_vals)) - 1))
    return sorted_vals[k]


def content_chars(content: Any) -> int:
    if content is None:
        return 0
    if isinstance(content, str):
        return len(content)
    try:
        return len(json.dumps(content, ensure_ascii=False))
    except Exception:
        return len(str(content))


@dataclass
class ToolMixSnapshot:
    session_id: str
    session_dir: Path
    path: Path
    n_user: int = 0
    n_assistant: int = 0
    n_reasoning: int = 0
    n_tool_result: int = 0
    n_system: int = 0
    id_to_name: dict[str, str] = field(default_factory=dict)
    sizes_by_tool: dict[str, list[int]] = field(default_factory=lambda: defaultdict(list))
    calls_by_tool: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    unknown_results: int = 0
    tools_per_user_turn: list[int] = field(default_factory=list)
    bash_output_byte_limit: Any = "missing"

    def total_calls(self) -> int:
        return sum(self.calls_by_tool.values())

    def total_result_chars(self) -> int:
        return sum(sum(v) for v in self.sizes_by_tool.values())

    def to_dict(self) -> dict[str, Any]:
        tools: list[dict[str, Any]] = []
        names = set(self.calls_by_tool) | set(self.sizes_by_tool)
        for name in sorted(names, key=lambda n: (-self.calls_by_tool.get(n, 0), n)):
            sizes = sorted(self.sizes_by_tool.get(name, []))
            n = len(sizes)
            sm = sum(sizes) if n else 0
            tools.append(
                {
                    "name": name,
                    "calls": self.calls_by_tool.get(name, 0),
                    "results": n,
                    "p50": percentile(sizes, 50),
                    "p95": percentile(sizes, 95),
                    "max": max(sizes) if n else None,
                    "sum": sm,
                    "mean": (sm / n) if n else 0.0,
                }
            )
        tpt = self.tools_per_user_turn
        return {
            "schema": "tool_mix.v1",
            "session_id": self.session_id,
            "session_dir": str(self.session_dir),
            "chat_history": str(self.path),
            "messages": {
                "user": self.n_user,
                "assistant": self.n_assistant,
                "reasoning": self.n_reasoning,
                "tool_result": self.n_tool_result,
                "system": self.n_system,
            },
            "tool_calls": self.total_calls(),
            "tool_result_chars_sum": self.total_result_chars(),
            "tools_per_user_turn": {
                "n": len(tpt),
                "mean": (sum(tpt) / len(tpt)) if tpt else 0.0,
                "max": max(tpt) if tpt else 0,
                "sum": sum(tpt) if tpt else 0,
                "list": tpt,
            },
            "bash_output_byte_limit": self.bash_output_byte_limit,
            "unknown_results": self.unknown_results,
            "tools": tools,
        }


def load_resources_bash_limit(session_dir: Path) -> Any:
    rs = session_dir / "resources_state.json"
    if not rs.is_file():
        return "missing"
    try:
        data = json.loads(rs.read_text())
    except Exception as e:
        return f"error:{e}"
    params = data.get("params") or {}
    bash = params.get("grok_build.Bash")
    if bash is None and isinstance(params.get("grok_build"), dict):
        bash = params["grok_build"].get("Bash")
    if not isinstance(bash, dict):
        return "key_absent"
    if "output_byte_limit" not in bash:
        return "key_absent"
    return bash.get("output_byte_limit")  # may be null → runtime default


def observe_session(chat_path: Path) -> ToolMixSnapshot:
    session_dir = chat_path.parent
    snap = ToolMixSnapshot(
        session_id=session_dir.name,
        session_dir=session_dir,
        path=chat_path,
        bash_output_byte_limit=load_resources_bash_limit(session_dir),
    )
    tools_since_user = 0
    seen_user = False

    with chat_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(o, dict):
                continue
            t = o.get("type")
            if t == "user":
                if seen_user:
                    snap.tools_per_user_turn.append(tools_since_user)
                seen_user = True
                tools_since_user = 0
                snap.n_user += 1
            elif t == "assistant":
                snap.n_assistant += 1
                tcs = o.get("tool_calls") or []
                if isinstance(tcs, list):
                    for tc in tcs:
                        if not isinstance(tc, dict):
                            continue
                        name = str(tc.get("name") or "unknown")
                        tid = tc.get("id")
                        if tid:
                            snap.id_to_name[str(tid)] = name
                        snap.calls_by_tool[name] += 1
                        tools_since_user += 1
            elif t == "tool_result":
                snap.n_tool_result += 1
                tid = o.get("tool_call_id")
                name = snap.id_to_name.get(str(tid)) if tid is not None else None
                if not name:
                    name = "unknown"
                    snap.unknown_results += 1
                snap.sizes_by_tool[name].append(content_chars(o.get("content")))
            elif t == "reasoning":
                snap.n_reasoning += 1
            elif t == "system":
                snap.n_system += 1

    if seen_user:
        snap.tools_per_user_turn.append(tools_since_user)
    return snap


def format_snapshot(snap: ToolMixSnapshot) -> str:
    d = snap.to_dict()
    lines = [
        f"## session {d['session_id']}",
        f"path: {d['chat_history']}",
        (
            f"messages: user={d['messages']['user']} assistant={d['messages']['assistant']} "
            f"reasoning={d['messages']['reasoning']} tool_result={d['messages']['tool_result']} "
            f"system={d['messages']['system']}"
        ),
        f"tool_calls (from assistant): {d['tool_calls']}",
        f"tool_result chars (sum): {d['tool_result_chars_sum']}",
    ]
    tpt = d["tools_per_user_turn"]
    if tpt["n"]:
        lines.append(
            f"tools/user_turn: n={tpt['n']} mean={tpt['mean']:.2f} "
            f"max={tpt['max']} sum={tpt['sum']} list={tpt['list']}"
        )
    else:
        lines.append("tools/user_turn: n=0")
    lines.append(f"bash output_byte_limit (resources_state): {d['bash_output_byte_limit']!r}")
    if d["unknown_results"]:
        lines.append(f"WARNING: unknown tool_result joins: {d['unknown_results']}")

    lines.append("")
    lines.append(
        f"{'tool':<36} {'calls':>6} {'results':>7} {'p50':>7} {'p95':>7} "
        f"{'max':>7} {'sum':>9} {'mean':>8}"
    )
    lines.append("-" * 96)
    for row in d["tools"]:
        p50 = row["p50"] if row["p50"] is not None else "-"
        p95 = row["p95"] if row["p95"] is not None else "-"
        mx = row["max"] if row["max"] is not None else "-"
        lines.append(
            f"{row['name']:<36} {row['calls']:6d} {row['results']:7d} "
            f"{p50:>7} {p95:>7} {mx:>7} {row['sum']:9d} {row['mean']:8.1f}"
        )

    total = d["tool_result_chars_sum"]
    if total > 0:
        lines.append("")
        lines.append("share of result chars:")
        for row in sorted(d["tools"], key=lambda r: -r["sum"]):
            if row["sum"]:
                lines.append(f"  {row['name']}: {row['sum']} ({100.0 * row['sum'] / total:.1f}%)")
    if d["tool_calls"] > 0:
        lines.append("share of calls:")
        for row in sorted(d["tools"], key=lambda r: -r["calls"]):
            if row["calls"]:
                lines.append(
                    f"  {row['name']}: {row['calls']} ({100.0 * row['calls'] / d['tool_calls']:.1f}%)"
                )
    return "\n".join(lines)


def resolve_chat_path(p: Path) -> Path:
    if p.is_dir():
        return p / "chat_history.jsonl"
    return p


def pick_largest(root: Path, n: int) -> list[Path]:
    cands: list[tuple[int, Path]] = []
    if not root.is_dir():
        return []
    for d in root.iterdir():
        ch = d / "chat_history.jsonl"
        if ch.is_file():
            cands.append((ch.stat().st_size, ch))
    cands.sort(reverse=True)
    return [p for _, p in cands[:n]]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="ToolMixSnapshot offline observe")
    ap.add_argument("paths", nargs="*", help="session dirs or chat_history.jsonl paths")
    ap.add_argument(
        "--from-env",
        action="store_true",
        help="resolve session from GROK_SESSION_ID (+ optional GROK_WORKSPACE_ROOT)",
    )
    ap.add_argument(
        "--write",
        action="store_true",
        help="write tool_mix.json into each session directory",
    )
    ap.add_argument(
        "--json",
        action="store_true",
        help="emit JSON (array if multiple) instead of text tables",
    )
    ap.add_argument("--workspace-dir", type=Path, help="encoded cwd sessions dir for --pick-largest")
    ap.add_argument("--pick-largest", type=int, metavar="N")
    ap.add_argument("--min-tools", type=int, default=1)
    ap.add_argument(
        "--quiet",
        action="store_true",
        help="with --write, suppress text tables (hook-friendly)",
    )
    args = ap.parse_args(argv)

    paths: list[Path] = []

    if args.from_env:
        sid = os.environ.get("GROK_SESSION_ID")
        if not sid:
            print("tool-mix-observe: GROK_SESSION_ID unset", file=sys.stderr)
            return 0  # fail-open for hooks
        found = find_session_dir(sid)
        if not found:
            print(f"tool-mix-observe: session not found: {sid}", file=sys.stderr)
            return 0  # fail-open
        paths.append(found / "chat_history.jsonl")

    if args.pick_largest:
        root = args.workspace_dir
        if root is None:
            ws = os.environ.get("GROK_WORKSPACE_ROOT") or os.getcwd()
            root = grok_home() / "sessions" / encode_cwd_dirname(ws)
        paths.extend(pick_largest(root, max(args.pick_largest * 3, args.pick_largest)))

    for p in args.paths:
        paths.append(resolve_chat_path(Path(p).expanduser()))

    if not paths and not args.from_env:
        # default: pick largest 3 under current workspace encoding
        ws = os.environ.get("GROK_WORKSPACE_ROOT") or os.getcwd()
        root = grok_home() / "sessions" / encode_cwd_dirname(ws)
        paths = pick_largest(root, 3)

    snaps: list[ToolMixSnapshot] = []
    seen: set[Path] = set()
    for path in paths:
        path = path.resolve() if path.exists() else path
        if path in seen:
            continue
        seen.add(path)
        if not path.is_file():
            if not args.quiet:
                print(f"SKIP missing: {path}", file=sys.stderr)
            continue
        snap = observe_session(path)
        if args.pick_largest and snap.n_tool_result < args.min_tools:
            continue
        snaps.append(snap)
        if args.pick_largest and len(snaps) >= args.pick_largest:
            break
        if args.write:
            out = snap.session_dir / "tool_mix.json"
            try:
                out.write_text(json.dumps(snap.to_dict(), indent=2) + "\n")
            except OSError as e:
                print(f"tool-mix-observe: write failed {out}: {e}", file=sys.stderr)

    if not snaps:
        if not args.quiet:
            print("No sessions observed", file=sys.stderr)
        return 0 if args.from_env else 1

    if args.json:
        payload = snaps[0].to_dict() if len(snaps) == 1 else [s.to_dict() for s in snaps]
        print(json.dumps(payload, indent=2))
    elif not args.quiet:
        print("\n\n".join(format_snapshot(s) for s in snaps))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

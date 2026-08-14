# Control overlay + host prep (what we shipped, why, impact)

**Date:** 2026-08-14  
**Status:** overlay live; harness product still frozen  
**Not:** a new graph crate, install.sh seeder, or inceptor claim

This is the authorship layer in front of official Grok Build: **route before ReAct**, **tune the host before blaming the model**. It exists so [next-deep-focus.md](./next-deep-focus.md) can measure EVA vs skip instead of improvising a stack every dump.

---

## What we did

| Surface | Where | Job |
|---------|--------|-----|
| **control-feeder** | `p10ns11y/skills` `master` (`a5344ed`); `~/.grok/skills/` + `~/.cursor/skills/` symlink | Dump → rewrite wording → route `light` \| `cg-outer` \| `eva-inner` → emit **Feed** → one next owner |
| **grok-host-prep** | same library + `scripts/prepare.sh` | Check/apply host knobs: `lsp.json`, `[features] lsp_tools`, MCP `command` on PATH, `[subagents]` |
| **eva-emptiness** (plugin, already) | Grok marketplace / `installed-plugins/` | Inner `Prior→Probe→Simulate→Score→ActOrAsk` **only** when emptiness gate fires |
| **control-graph** (skill, already) | skills library | Outer phases + Control Card; never owns EVA body |

`https://x.ai/cli/install.sh` only seeds `~/.grok/{bin,downloads,completions}` + a thin `config.toml`. It does **not** create `skills/` or `plugins/`. Official shipped skills appear under **`~/.grok/bundled/`** after credentials (`grok login` or deployment key) via `maybe_sync_bundle_*`. User `~/.grok/skills` and `plugins/` appear when we write or symlink them.

---

## Why these, not more runtime

Same spine as [harness-feed-filter.md](./harness-feed-filter.md):

| Failure class | Lever | Skill / plugin |
|---------------|--------|----------------|
| Missing capability (LSP hidden, MCP binary gone, bash &lt;8192) | **Harness** | grok-host-prep |
| Unbounded “keep going” / wrong phase | **Graph skill** | control-graph (after Feed) |
| Map missing, auth unclear, futures disagree | **EVA Inner** | eva-emptiness plugin + skill |
| Dump is vague or stacked | **Pre-graph** | control-feeder |

[author-vs-inceptor.md](./author-vs-inceptor.md): we author **when not to run**. We do not incept `turn.rs`. Feeder is the skip gate made executable; host-prep is the harness gap made checkable.

---

## Impact (what changes on the invoice)

Unit of account stays **done work / $** (no extra re-prompt). `tool_mix` = invoices.

| Change | First-order | Second-order |
|--------|-------------|--------------|
| Feed routes greppable → `light` | Skip Card + skip EVA | Track A in next-deep-focus is *runnable* (skip arm is named) |
| Feed routes emptiness → CG + EVA | Probe budget instead of silent Act | Fewer YOLO / overclaim turns |
| `lsp.json` + `lsp_tools` | `goToDefinition` / hover vs fat `read_file` | Lower result-char bill on this Rust+C tree |
| `[subagents] enabled` | `task` exists without a one-off env | Orchestrator / CG Inner can fan-out |
| MCP `command` check | Dead servers do not burn startup | Project `.grok/config.toml` replace-not-merge stays visible |
| Cursor + Grok symlink to one library | One SoT | No dual-edit drift |
| `bundled/` after login (known) | Stop hunting install.sh for skills | User overlay vs shipped overlay stay distinct |

**Do not treat as wins:** `permission_mode=always-approve`, lowering `output_byte_limit`, nesting `grok`, a 40-node graph, extra north-star skills.

---

## How a dump should flow now

```text
dump
  → /control-feeder          Feed block (goal, route, why, next)
       ├─ harness_gap?       /grok-host-prep  (then re-route the work)
       ├─ light              implement / agent-orchestrator   — no Card
       ├─ cg-outer           control-graph Card  inner_mode=standard
       └─ eva-inner          control-graph Card  inner_mode=eva
                             + eva-emptiness plugin (Inner only)
```

Verify: `/control-feeder` emits a table; `bash ~/.grok/skills/grok-host-prep/scripts/prepare.sh --check` is green on lsp + `lsp_tools`; new grok session lists `lsp` and `task`.

---

## Still env-only (host, not a skill)

`GROK_WEB_FETCH=1` and `GROK_MEMORY=1` stay session exports. `[memory] enabled` is not enough for `memory_search`. Do not write those into random shell rc from this note.

Pairs with: [harness-feed-filter.md](./harness-feed-filter.md) · [harness-economy-model.md](./harness-economy-model.md) · [next-deep-focus.md](./next-deep-focus.md).

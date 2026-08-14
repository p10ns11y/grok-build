# How to read harness / loop / graph posts

**Status:** filter card (not a product lever)  
**Date:** 2026-08-14  
**Pairs with:** [harness-economy-model.md](./harness-economy-model.md) · [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md)

X is full of the same three-layer deck: **harness vs loop vs graph**. Some of it is a real control-plane vocabulary. Most of it is a bookmark-farm with Temporal + LangGraph + sandbox links. This note is how to **filter the feed**, what to **keep**, how it **differs by tool**, and what **burns dollars and time** instead of shipping work.

The purpose of the stack, when it is honest: **quality** (the run stops on evidence) and **structured outcome** (you can name the phase and the blast radius without asking the model to narrate itself). It is not prettier mermaid.

---

## The three questions (keep these)

| Layer | Question | Failure if missing |
|-------|----------|--------------------|
| **Loop** | Should this run *again*? | Never stops; spends without new evidence |
| **Graph** | *Where* may it go next? | Right action, wrong phase; path invisible |
| **Harness** | What may it *touch*? | Correct workflow, wrong effect |

If a post cannot be reduced to those three questions, it is branding. Close it.

A useful counter-signal from the same feed: do **not** build a forty-node graph before watching the agent do the work once. A loop that is only “keep trying,” with no fresh evidence and no cap, is a **cost leak**, not reliability.

---

## How to filter a post (one pass)

Read the first screen only. Score it. Then stop or open the article.

| Filter | Keep if | Drop if |
|--------|---------|---------|
| **Owner of failure** | Names *which layer* broke, in one sentence | “Just add a graph / more retries / a smarter model” |
| **Evidence** | Test, join, trace, or $ per *done task* | Demo GIF, “save this,” no number, no fail mode |
| **Stop rule** | When the loop *must* exit | Unlimited ReAct sold as agency |
| **Blast radius** | Permissions, sandbox, HITL, what it must *not* touch | “Give it a phone / the whole repo / YOLO” as the punchline |
| **Transfer** | Works on *your* harness without a new runtime | Requires LangGraph / Temporal / a desktop wrapper to “count” |
| **Unit of account** | Useful work / $ (no extra re-prompt) | HUD %, longer sessions, more tools, more nodes |

**Two-strike rule:** if it fails **owner** and **evidence**, it is a fantasy demo. Do not implement it. Do not open `grok-local` to “try the pattern.”

**Discipline first:** if you cannot state the stop rule and the unit of account, you are not ready for a new layer. The missing piece is habit, not topology.

---

## What to take (portable)

Take the **questions**, not the product.

1. Debug the layer that owns the failure (tools/isolate → harness; storms/no-stop → loop; wrong phase → graph).  
2. Continues only on **new evidence** (test, join, user ack) — not on “the model feels done.”  
3. Bound hops (turns, tools, $). Jevons: cheaper models make *more* loops unless you tax them.  
4. One trace / one session lake you can join **offline** (`tool_mix`, `chat_history`). Nested agents to “measure” are invoices, not GDP.  
5. Harness design often moves **cost per done task** more than swapping the model. That is already this fork’s bet (8 KB dumps, hop tax, observe). It is not a reason to rewrite `turn.rs`.

Do **not** take: a new graph crate, a second loop platform, “harness 2.0,” or a 40-node control plane because a video said the model is the smallest box.

---

## How it differs by tool (do not copy-paste)

The deck uses one vocabulary. **The machine underneath is not the same.** A pattern that is load-bearing in LangGraph can be **already shipped** or **actively harmful** in Grok Build.

| System | What it already *is* | What the feed usually sells | Waste if you obey the feed |
|--------|----------------------|-----------------------------|----------------------------|
| **Grok Build (this tree)** | Full **harness** (tools, sandbox, perms, memory, hooks, sessions). **Loop** in `turn.rs` (`max_turns`, stationarity, soft-call 12/20). **Graph** only where emptiness is high (plan, Rhai workflows, EVA, subagents) | “You need a graph engine” | LangGraph-in-every-turn; nest `grok`; rebuild mid-session; another cap |
| **Official `grok` 1.0.3** | Same family, **no** this-fork loop patches | Dogfood every `local` knob here | Measuring treatment in the official lake; mixed `GROK_HOME` |
| **Claude Code / Cursor / Codex** | Different tool taxonomies, permission UIs, compaction | “Same harness, swap the brand” | Copying their folder-context tricks that fight *this* inject/compaction |
| **LangGraph / Crew-style** | Graph *is* the product | Always start with nodes | 40 nodes before one successful `read_file` + test |
| **Temporal / durable exec** | Crash-survive long jobs | Every coding turn needs a workflow engine | Serializing a TUI turn through a cluster |
| **DeepSeek Harness + desktops** | Plugin OS + Web UI | “Now we have a harness” | Second agent OS beside a pager that already *is* one |
| **Phone / cloud-device harnesses** | Extra **environment** (pixels, OCR, a VM) | “Agents can finally act” | Demo that clicks; no self-heal; $ on retries against a brittle UI |

**Rule:** if the post’s reference implementation is not this repo’s `turn.rs` / session files, treat it as **analogy**. Port the question, not the crate.

---

## What wastes dollars and time (not just weak demos)

These look like engineering. They are **invoice printers**.

| Pattern | Why it feels smart | What it actually bills |
|---------|--------------------|------------------------|
| Forty-node graph before one watched session | “Structure” | Design week + merge conflict with upstream `turn.rs` |
| Loop = keep going | “The agent is thorough” | Storms (28–109 tools/turn); context re-bills every dump |
| Nested full agent to measure | “A/B science” | Shared auth/socket; wedges the outer TUI; child dumps enter *this* context |
| New harness wrapper | “OS around the model” | You already have one. Second OS is FX volume |
| Eval theater with no join | “Quality gate” | Prompts and dashboards; no `tool_mix` before/after |
| YOLO / always-approve as speed | “Unblock the demo” | One wrong `rm` or leak; harness layer abdicated |
| Skill-list / inject polish because the HUD is fat | “Trim the system prompt” | Organs, not the bill (inject ≪5%, skills ~2%) |
| Bash below 8192 or hard-stop-first | “Tighter is cheaper” | Quality cliff; extra user re-prompt = new river |
| Rebuild pager while it is running | “Need the new bits” | Invisible binary; you measure the *old* image |
| Open `grok-local` to “understand the harness” | Curiosity | Tourism. The map is the roadmap + this filter |

Fantasy demo tells: vertical video, “save this,” three arrows into Temporal/LangGraph/E2B, no stop rule, no $ per **done** task, no “what we refused.”

---

## Applied here (so the article has a spine)

Grok Build already **is** the three-layer machine. The feed is a **relabel**.

- Missing capability → harness (permissions, 8192, `AGENTS.md`).  
- Unreliable completion → loop (stationarity, soft-cap). Official `grok` does not have this-fork soft-cap — do not pretend it does.  
- Uncontrolled branching → graph **skills** (plan / EVA / workflow) when emptiness is high — not every user turn.

**Discipline first:** official `grok` to ship; `tool-mix-observe` on the right `GROK_HOME`; freeze new layers until a join changes the table. Open `grok-local` only to falsify an **in-tree** claim (today: soft-call binds at 20). That is the opposite of the feed’s “add a graph.”

---

## One-screen cheat

```text
Can I name loop vs graph vs harness for this failure?  → no → close
Is there a stop rule and a $ / done-task number?         → no → close
Does it require a runtime we do not have?                → yes → analogy only
Would this add a lever before a disk join?               → yes → refuse
Would this nest grok or YOLO?                            → yes → trauma
Else: take the question, keep the freeze.
```

Operator loop and freeze: [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md).  
What the economy metaphor keeps: [harness-economy-model.md](./harness-economy-model.md).

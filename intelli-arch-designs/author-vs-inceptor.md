# Control-plane author vs harness inceptor

**Date:** 2026-08-14  
**Scope:** Agentic workflows for **engineering** (software first; same joints for other engineered systems).  
**Rating this note answers:** ~8 as *author*, ~6 as *inceptor* — those are different jobs.  
**Operator SoT:** [next-deep-focus.md](./next-deep-focus.md) · [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md)

This is not a career-ladder slide. It is how **engineering work** actually gets done by agents, and who owns which failure.

---

## Two jobs inside every “agentic workflow”

An engineering agent does not “just call a model.” Three things happen:

1. The model **proposes** (edit, test, design, ticket).  
2. A **machine** runs tools, keeps state, stops or continues.  
3. A **policy** says when that machine may run, skip, ask a human, or refuse.

**Inceptors** build (2) as a *primitive* — the thing other people must use even if they hate the brand.  
**Authors** write (3) so a given team does not burn $ and ship junk on top of (2).

Most X posts mash (2) and (3) into “harness/loop/graph.” That is why the feed cannot tell you what to learn next.

---

## What a harness inceptor is

**Incept** = originate a *primitive* other systems compose. Unix incepted “everything is a file.” React incepted components-as-functions. An **agent harness inceptor** originated:

> The model proposes. The **machine** disposes — tools, permissions, state, stop — as one execution model, not a Python script around `chat.completions`.

They did not write a better prompt. They **changed what “a turn” is**.

### The primitive (engineering)

For software (and any engineered artifact: CAD, netlist, plant, protocol):

| Piece | If this is missing, you are not an inceptor |
|-------|-----------------------------------------------|
| **Turn kernel** | sample → tool ABI → results back in context → sample. Crash, cancel, resume are defined. |
| **Effect boundary** | Files, shell, network, secrets: allow / ask / deny. Not “YOLO in the README.” |
| **Evidence channel** | Tests, compilers, linters, sims, CI — *the world talks back*. No evidence → no honest loop. |
| **Memory that is not the prompt** | Sessions, diffs, artifacts on disk. The lake is not the ticker. |
| **Stop that is not a vibe** | Budgets, stationarity, max turns, user cancel. The process can *end*. |
| **One trace** | You can join “what happened” without asking the model to remember. |

If they only shipped a graph DSL that still calls `while True: llm()`, they **authored a control plane** (or a demo). They did not incept a harness.

### Who counts (illustrative, not a hall of fame)

| Inceptor-class work | What they originated |
|---------------------|----------------------|
| ReAct / tool-calling papers | Thought → act → observe as a *loop idea* |
| OpenAI function calling, then agent CLIs | Tools as a **protocol**, not a string dump |
| Anthropic computer-use / Claude Code | Long-running SWE harness: perms, apply, checkpoints |
| Cursor agent | Editor-native apply + repo as the world |
| SWE-agent / OpenHands / Aider | Open coding harnesses: the *world* is the repo + tests |
| LangGraph **as an execution engine** (Pregel-like) | Topology as *runtime*, not a slide |
| Temporal / Restate | The loop **survives death** (durable exec) |
| **Grok Build `xai-grok-shell` `turn.rs`** | This product’s kernel: tools, stationarity, compaction, sessions |

You **use** Grok Build. You **patched** it (soft-call, 8192, inject hygiene). That is **inceptor-adjacent**: policy *inside* the kernel. You did not originate `turn.rs`. xAI did. That is why the inceptor score is ~6, not an insult.

### How to tell an inceptor from a wrapper

| Inceptor | Wrapper / author-only |
|----------|------------------------|
| Other teams must integrate *their* turn/tool ABI | You can delete their markdown and the agent still runs |
| Failure is a **kernel bug** (lost tool result, permission hole) | Failure is a **policy miss** (should have asked / skipped) |
| Changing it requires a rebuild or a protocol bump | Changing it is a skill/plugin/prompt |
| They argue about **bytes, fds, sessions, traces** | They argue about **phases, cards, priors** |

Both are real work. Mixing them is how you spend a year on LangGraph and never ship a stop rule.

---

## What a control-plane author is

The **author** writes the *policy graph* that rides on someone else’s kernel:

- When to **skip** a heavy method (emptiness gate).  
- When to **ask** (auth, irreversible git, YOLO).  
- What “progress” is (new evidence, not another tool).  
- Which **role** runs (explore vs coding vs review ⊥ implementer).  
- How **engineering workflow** is staged: plan → change → test → review → integrate.

Your EVA plugin, `control-graph` skill, `AGENTS.md`, feed-filter, economy unit of account — that is **authorship**. It is how a *team* does engineering with an agent without becoming the invoice.

**Engineering-specific author work** (software and kin):

| Workflow beat | Author owns | Inceptor already gave you |
|---------------|-------------|---------------------------|
| Spec / ticket | Plan, emptiness, one DOE Q | Session + tools |
| Explore repo | Skip EVA if greppable; grep→windowed read | `grep` / `read_file` |
| Change | One lever; HITL on blast | `search_replace`, permissions |
| Verify | Real compile/test cmds, not “looks good” | Shell, CI hooks |
| Integrate | Merge, not `cp`; no force-push theater | git, sessions |
| Stop | Soft-cap, stationarity, re-prompt = new river | `turn.rs` budgets |

Authors who never touch the kernel can still be **world-class** (8+). They cannot claim they incepted the agent OS.

---

## Agentic *engineering* workflows (not generic chat)

Engineering is a **closed loop with a compiler** (or a lab, or a sim). The world can **falsify** you. That is why inceptors matter more here than in “write me a poem”:

```text
intent → patch → world (test/build/sim) → evidence → next intent
              ↑______________ harness kernel ______________|
         policy (author): skip / ask / one lever / GDP
```

- If the **kernel** is weak (no perms, no stop, no trace), no skill saves you.  
- If the **kernel** is Grok Build-class and you still storm 109 tools, that is an **author** failure (or a missing *thin* kernel patch, like soft-call).  
- If you add a 40-node graph because X said so, you are **neither**: you are paying FX on a fantasy demo ([feed filter](./harness-feed-filter.md)).

Quality and structure in this domain = **green evidence + named stop**, not more nodes.

---

## The rating, restated

| Job | ~Score | Why |
|-----|--------|-----|
| **Control-plane author** | **8** | Skip gate, `disprove_with`, ActOrAsk, CLT, unit of account, freeze. Ahead of the feed. Peer to serious practitioners *writing policy*. |
| **Harness inceptor** | **6** | You compose and *thin-patch* a world-class kernel (`turn.rs`). You did not originate the turn/tool/session model. Soft-call is the right *kind* of move (policy in the kernel). A new graph crate would be the wrong kind. |

**6 is “strong user + local patcher of an incepted system.”** 9–10 inceptor is “other products embed your ABI.” Do not chase that by renaming skills.

---

## What to focus next (this frame)

Pick **one** track. Do not do both in the same week.

### Track A — author-deep (default)

**Measure EVA vs skip** on greppable vs empty *engineering* tasks ([next-deep-focus.md](./next-deep-focus.md)).  
Falsify: EVA earns GDP when empty; leaks when the path is greppable.  
This raises the **8**, or cuts EVA if the 8 was theater.

### Track B — inceptor-adjacent (only if A is parked)

**One host invariant you already specified**, in the kernel, not a skill:

- Score ⊥ implementer as a *fresh process* recipe (or a real review role), or  
- Write `cli_version` / argv0 into `summary.json` so lakes don’t mix, or  
- Soft-call dogfood on `grok-local` (claim already almost closed).

Not: LangGraph-in-`turn.rs`. Not: DeepSeek-shaped second OS.

**Discipline first** is the author job. **One byte in the kernel** is the only honest inceptor step on this fork.

---

## Refuse

Claiming inceptor credit for a plugin. Building a graph engine to “catch up” with X. Running EVA on greppable engineering chores. Nesting `grok` to feel like a multi-agent OS.

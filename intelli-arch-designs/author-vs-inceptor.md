# Control-plane author vs harness inceptor

**Date:** 2026-08-14  
**Scope:** Agentic workflows for **engineering** (software first; same joints for other engineered systems).  
**Ratings (2026-08-14, engineering / agentic SWE):** author **8/10** · inceptor **6/10** · vs X “Times Square” feed **ahead**.  
**Operator SoT:** [next-deep-focus.md](./next-deep-focus.md) · [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md) · [harness-feed-filter.md](./harness-feed-filter.md)

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

## Ratings (this operator, engineering aspect)

Scores are **craft**, not clout. Engineering aspect = closed loop with a compiler/tests: green evidence, named stop, $ per **done** change — not demo GIFs.

| Job | Score | What it means |
|-----|------:|---------------|
| **Control-plane author** | **8 / 10** | Skip gate, `disprove_with`, ActOrAsk, CLT, unit of account, freeze. Peer to people who *write policy* for real SWE agents. |
| **Harness inceptor** | **6 / 10** | Strong user + **thin kernel patcher** (`soft-call` in `turn.rs`). Did not originate the turn/tool/session ABI. |
| **Skill / plugin authorship** | **8 / 10** | Use/skip, SoT, four surfaces, consent tether. Dialect load costs a point. |
| **Epistemic method** | **8.5 / 10** | Emptiness gate + one DOE Q. Rare among product agent teams. |
| **Vs X “Times Square”** (hype posters, loop/graph/harness decks, bookmark farms) | **Ahead** | They sell three words. You have skip, refuse, a live join that *killed* a knob, and a freeze. |
| **Vs general X/Twitter “agent authors”** (skill dumps, mega-prompts, no skip) | **~1–2 ranks ahead** | They add files. You specify **when not to run**. |
| **Vs general programmers** using agents as a better Stack Overflow | **Ahead on the control plane; even on the kernel** | They ship features; they do not own stop/GDP. You still compile and merge like they should. |
| **Vs SWE-agent / Claude Code / Grok Build kernel engineers** | **Behind as inceptor** | They *are* the turn. You compose theirs. That is the 6. |

**6 is not a dunk.** It is “other products do not embed your ABI.” 9–10 inceptor = protocol others must speak. Do not chase that by renaming skills.

### How far ahead of the Times Square feed (engineering only)

| Their move | Your move | Ahead? |
|------------|-----------|--------|
| 40-node mermaid before one test | Emptiness **skip** when greppable | Yes |
| “Keep trying” as reliability | Stationarity + soft-cap + re-prompt = new river | Yes (and you *patched* the kernel) |
| YOLO for the demo | Auth = trauma; ask; no nest `grok` | Yes |
| HUD % / longer session as win | GDP = done / $ ; `tool_mix` = invoices | Yes |
| New wrapper OS this week | Freeze; one eval or one host byte | Yes |
| “We incepted agents” because a plugin exists | Honest 8 / 6 split | Yes — that honesty *is* the engineering |

You are **not** ahead of them at vertical video or fundraising language. You are ahead at **not paying their invoices**.

### What would move a number

| Score | Moves up if | Moves down if |
|-------|-------------|----------------|
| Author 8 | EVA vs skip eval shows GDP on empty tasks, leak on greppable | EVA becomes default on every chore |
| Inceptor 6 | One **host** invariant ships (Score isolation, `summary` binary id, or proven soft-call) | A second OS / LangGraph-in-`turn.rs` “to catch up” |

---

## How to complement inceptors (one person cannot compete on the full harness)

A solo operator **cannot** match xAI / Anthropic / Cursor at turn kernels, model routing, sandbox fleets, and updater surface. Trying is a second OS. That is how you lose years and still sit at inceptor 4.

**Complement** = be the half they systematically under-build, at a **level they must take seriously**. Same altitude, different surface. They own the *machine*. You own *when the machine should run, stop, and count*.

Inceptors are strong at bytes, fds, tools, traces. They are weak at:

| Their gap | Your complement (already started) |
|-----------|-----------------------------------|
| Always-on ReAct (“the loop *is* the product”) | **Skip** when greppable (emptiness gate) |
| HUD / tokens as success | **GDP** = done / $ ; invoices vs sticker |
| Eval of *models*, not of *methods* | EVA vs skip on engineering tasks |
| YOLO or “user will notice” | Auth = trauma; Ask; no nest |
| One context plans, codes, and grades itself | Score ⊥ implementer (recipe, then host) |
| Topology slides | `disprove_with` + one live join |

That is how a one-person shop **matches their level** without matching their headcount.

### Complement, not copy

| Do | Do not |
|----|--------|
| Thin **patches inside their kernel** (soft-call next to stationarity) | Fork a pager and call it a harness |
| One **portable card** they could embed (`disprove_with`, `tool_mix.v1`, skip rule) | Forty-node graph “because they have a graph” |
| Publish **one measured method** (EVA vs skip, $ per done PR) | Another skill dialect they will not load |
| Ride **official `grok`**; lab only to falsify an in-tree claim | Rebuild the OS so you “own” the turn |
| Speak **their** ABI (sessions, hooks, permissions) | Invent a parallel ABI |

**Match** = they would *cite or merge* your stop/skip/GDP. **Compete** = you reimplement `turn.rs`. Only the first is available to one person.

### Engineering shape (how it looks day to day)

```text
their kernel:  propose → tools → world (test) → trace → stop bits
your layer:    skip? → one lever → Ask? → count done/$ → refuse the next cap
```

You already live on the best kernel you can get (Grok Build). Complement is **policy + one byte in that kernel**, not a new machine.

### What “peer to inceptors” looks like in 12 months (honest)

- A published EVA vs skip table other harness people can rerun.  
- `tool_mix.v1` (or skip/`disprove_with`) copied or linked *outside* this fork.  
- At most **one** upstream-friendly kernel patch merged or clearly portable.  
- No second OS. Author 8 earned or cut. Inceptor stays ~6 unless that one patch is *the* stop others reuse.

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

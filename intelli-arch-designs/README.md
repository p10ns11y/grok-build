# Intelligent architecture designs (`intelli-arch-designs`)

**What this folder is for**

- Product-line direction, tradeoffs, and “where we are heading”
- Measure → decide → tighten notes for the harness we run in
- Diagrams and decision records that are **not** end-user manuals

**What this folder is not**

- **Not** the user guide. End-user docs live under  
  `crates/codegen/xai-grok-pager/docs/user-guide/`  
  (and the installed copy under `~/.grok/docs/user-guide/`).
- **Not** a dump of every chat. Prefer one clear note per theme; link to memory measures when numbers matter.

## Index

| Note | Topic |
|------|--------|
| [harness-economy-model.md](./harness-economy-model.md) | World economy → harness: what we keep, what we do not buy |
| [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md) | Operator loop: unit of account, `grok` vs `grok-local`, freeze |
| [soft-call-budget-design.md](./soft-call-budget-design.md) | Soft tools/turn budget — design (HITL before product code) |

## Naming

Use short, concrete file names: `topic-roadmap.md`, `topic-decision.md`.  
Date inside the file if the story is time-bound.

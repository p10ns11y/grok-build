# World economy as a model for the harness

**Status:** literacy + mapping (not a live feed, not a product lever)  
**Date:** 2026-08-14  
**Runs as:** inspiration. **SoT for what we ship:** [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md)

The world economy is a **great model** for a coding harness *when we keep the joints* (flow vs stock vs sticker, invoices vs value-added, Jevons). It is **not** a schema to buy whole: no central bank, no fleet KDI, no “market cap” dashboard as the goal.

Private literacy source (operator disk, not in this repo): `~/life-os/Resources/economy-first-principles.md`. Do not paste household or ledger facts here.

---

## Load-bearing line

> Spending is the metabolism. Wealth is who has title to the organs. Market cap is the sticker on the tickets.

Harness translation: **API $ and tool hops are the metabolism.** Memory, skills, and session files are title to organs. HUD context % is the sticker.

---

## What we keep (maps cleanly)

| World | Harness | What we do |
|-------|---------|------------|
| Flow / GDP (this year’s output) | Useful work / $ — task done, PR shipped, **no extra re-prompt** | **Unit of account** |
| FX / invoice volume | `tool_mix`: calls × result chars × rounds (same dump re-billed next call) | Watch and tax hops. Not the goal |
| Market cap (last sale × all tickets) | HUD %, `signals.json` `contextTokensUsed` | Thermometer only |
| Stock / lake (homes, titles) | Memory, skills, logs on disk, policy knobs | Compound; do not restuff into the model |
| Value-added vs supply-chain invoices | Keep the **decision**, drop unused tool dumps | Next prompt should not re-bill steel→part→car |
| Do not add household wealth + company caps | Do not add inject + skills + tools as three “cost piles” | One window. E0: inject ≪5%, skills ~2%; tools dominate |
| Jevons (cheaper energy → more use) | Cheaper/faster models → more tool storms | Soft-call stays even when inference “feels cheap” |
| Efficiency ≠ resilience | Bash 4 KB or hard-stop-first | Keep 8192; hard-stop off |
| Chokepoints | `turn.rs`, context window, API, HITL | One storm turn reprices the session |
| Comparative advantage only if ships sail | Subagents only if coordination does not sink the outer TUI | Never nest `grok` inside `grok` |

---

## What we do **not** buy (harness nuances)

| World idea | Why it does not ship here |
|------------|---------------------------|
| Fleet importance / KDI store | SpaceXAI scale. Local observe → one knob → remasure is enough |
| “Traders help each other” | Parallel tool fan-out **competes** for context; last call holds the bag |
| Crypto market cap / FX prints as output | `tool_mix` call counts are **churn**, not GDP |
| Lower every price (bash 4 KB, skill-list ceiling) | Organs are not the bill; diminishing ROI; quality risk |
| Fit the metaphor first | Proven method (measure, one lever, freeze) beats metaphor-fit |

Nuance: a coding session has **one buyer** (you) and **one firm** (this turn). There is no secondary market that “cashes out” unused reads. So the strongest world lesson is **value-added accounting**, not ticker games.

---

## Unit of account (copy used by the roadmap)

| Name | What it is here | Optimize? |
|------|-----------------|-----------|
| **GDP / river** | Useful output per dollar (done, no extra re-prompt) | **Yes** |
| **FX / invoices** | `tool_mix` calls × chars × rounds | Watch |
| **Market cap / sticker** | HUD / `contextTokensUsed` | No |
| **Stock / lake** | Memory, skills, session files, knobs | Compound off-model |

---

## Enough for now

The model already paid for itself if it stops a **wrong lever** (skill-list, inject polish, bash &lt;8192) and keeps **official `grok`** as the editor. It does not justify a new economy crate.

Operator loop, freeze, `grok` vs `grok-local`: [harness-learning-cost-roadmap.md](./harness-learning-cost-roadmap.md).  
Filter X harness/loop/graph posts: [harness-feed-filter.md](./harness-feed-filter.md).

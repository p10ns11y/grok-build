# grok-build (this repo)

Unit of account: useful work / $ (done, no extra re-prompt). `tool_mix` = invoices. HUD % = sticker.

1. Tight grep/list before `read_file`. Read only the hit window (`offset`+`limit` ≤80). Do not omit `limit`. A 120-line first read is still a fat invoice (p95 reads were 7–16k chars).
2. Do not re-read a file already in context. Prefer grep context over another full window.
3. One lever. Official grok has no soft-cap: stop and ask if this user turn needs >12 tools. Do not spawn a crowd then poll.
4. Do not run `grok` / `grok -p` / nested agents from a live session. Measure: `tool-mix-observe.py`. Official lake `~/.grok`; local pager `GROK_HOME=~/.grok-local`.
5. Keep this file tiny — it is re-injected every turn. Do not lower bash below 8192. No TurnPolicyGate, no fleet KDI.
6. Operator compass [life-os UX/north-star](https://github.com/p10ns11y/life-os/blob/master/UX/north-star.md): finance-now, SpaceXAI by compounding. End with `Next on path:` one step. No PII.

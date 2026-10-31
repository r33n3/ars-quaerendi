# Ars Quaerendi Unified v2.0
**The Art of Inquiry**. HCU-inspired, not affiliated with HCU.

Six independently callable skills consolidated from Ars Quaerendi, Telos, Instrumentum, Judicium, Contribution Harvesting and Anomaly & Serendipity Recognition.

| Skill | Question |
|---|---|
| inquiry | What do we need to understand? |
| purpose-planning | Which goals serve our authorized purpose? |
| toolcraft | What tool should we reuse, borrow or build? |
| judgment | Is the evidence sufficient for the next use? |
| discovery | What unexpected pattern or serendipitous lead appeared? |
| contribution | What useful value emerged even if the project failed? |

## Architecture and flows
Brokkr (or another existing main agent) owns purpose, goals, orchestration, local subagents, user settings and execution. Skills are **advisory methods**, not a second coordinator. Invoke selectively:

- Unknown question → Inquiry; unexpected observation → Discovery.
- Purpose-driven goal → Purpose & Planning; missing capability → Toolcraft.
- Consequential decision → Judgment; partial or reusable outcome → Contribution.
- Results may loop back to any skill. **No mandatory six-step pipeline.**
- A2A peers in the decentralized P2P mesh can offer capabilities, but each node enforces its own authority and validates received evidence. No automatic sharing.

Progress-oriented feedback records **parent outcome, verified milestones, learning, unexpected discoveries, and transferable contributions** separately. Serendipity is explicitly preserved even if unrelated to the parent goal. Avoid reward hacking: no XP merely for retries or manufactured anomalies.

## Install
Extract ZIP and, from this folder, run for Codex installations using the common skills path:
```bash
mkdir -p ~/.agents/skills
cp -R skills/* ~/.agents/skills/
```
Verify your agent host's actual skills directory. Merge optional `AGENTS.md` guidance with existing instructions; do not replace the main agent. Archive older packages to avoid duplicate skill routing.

## Evidence and judgment
D documented; O observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
J0 exploratory; J1 plausible; J2 supported; J3 verified within tested scope; J4 qualified for defined use. These are **not permissions**.

## Validation
Run `python3 tests/validate.py`. This checks structure and JSON data, not behavioral effectiveness. Run scenarios in `tests/acceptance.md` against an unmodified agent baseline to measure actual value and overhead.

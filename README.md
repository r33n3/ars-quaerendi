# Ars Quaerendi Unified v2.1
**The Art of Inquiry**. HCU-inspired, not affiliated with HCU.

An independent collection of seven reusable skills for people and AI agents. Use each skill on its own or combine them as needed, without a required agent framework or peer network. The collection consolidates Ars Quaerendi, Telos, Instrumentum, Judicium, Contribution Harvesting and Anomaly & Serendipity Recognition, with reliability engineering for reusable capabilities.

| Skill | Question |
|---|---|
| inquiry | What do we need to understand? |
| purpose-planning | Which goals serve our authorized purpose? |
| toolcraft | What tool should we reuse, borrow or build? |
| judgment | Is the evidence sufficient for the next use? |
| discovery | What unexpected pattern or serendipitous lead appeared? |
| contribution | What useful value emerged even if the project failed? |
| reliability-by-construction | How do we make a prototype repeatable, robust and resilient for its intended use? |

## Architecture and flows
Skills are **advisory methods** that people can follow directly or use with a compatible AI agent. The person or host agent controls purpose, goals, execution and permissions. Choose skills selectively:

- Unknown question → Inquiry; unexpected observation → Discovery.
- Purpose-driven goal → Purpose & Planning; missing capability → Toolcraft.
- Consequential decision → Judgment; partial or reusable outcome → Contribution.
- Prototype promotion or recurring failures → Reliability by Construction.
- Results may loop back to any skill. **No mandatory pipeline.**
- External tools or collaborators are optional. Validate received evidence and share material only with authorization.

Progress-oriented feedback records **parent outcome, verified milestones, learning, unexpected discoveries, and transferable contributions** separately. Serendipity is explicitly preserved even if unrelated to the parent goal. Avoid reward hacking: no XP merely for retries or manufactured anomalies.

## Install
For manual use, read any `skills/<name>/SKILL.md` and consult the package's `references/` as needed. No installation is required.

Extract ZIP and, from this folder, run for Codex installations using the common skills path:
```bash
mkdir -p ~/.agents/skills
cp -R skills/* ~/.agents/skills/
```
Verify your agent host's actual skills directory. Keep the package's `references/` available alongside your installation; the copy command above installs only the skill folders. Merge optional `AGENTS.md` guidance with existing instructions. Archive older packages to avoid duplicate skill routing.

## Evidence and judgment
D documented; O observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
J0 exploratory; J1 plausible; J2 supported; J3 verified within tested scope; J4 qualified for defined use. These are **not permissions**.

## Validation
Run `python3 tests/validate.py`. This checks structure and JSON data, not behavioral effectiveness. Run scenarios in `tests/acceptance.md` against an unmodified agent baseline to measure actual value and overhead.

## v2.1: Reliability and capability progression

Added `reliability-by-construction` as a seventh optional skill and `references/factory-and-reliability.md` for moving prototypes toward reliable use. Experimental success, engineering repeatability, resilience, and scoped deployment qualification are separate outcomes. People or their chosen host environment control deployment and authorization; no new coordinator or automatic promotion is introduced.

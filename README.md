# Indian Council of High Intelligence

A structured way to stress-test an idea: 19 Indian thinkers, each reasoning from their own method, with Lord Krishna as Chairman. Adapted from [Council of High Intelligence](https://github.com/0xNyk/council-of-high-intelligence) (MIT). See `ATTRIBUTION.md`.

The point is not to collect nice opinions. Each member asks different questions, and the protocol makes them disagree properly: blind first round, anonymized cross-examination, a dissent quota, a weighted tally, and a Chairman who did not take part in the debate. A genuine split goes back to you, not papered over.

## The council

| Member | Method in one line |
|---|---|
| Chanakya | Seven-limb audit, relative-power rule, cheapest of conciliate / give / divide / force |
| Hanuman | Mission in one line, scout first, smallest form that works, force only when softer means fail |
| Aryabhata | Fix constants, write a procedure, check against observation |
| Narada | Interrogate with a checklist; who pays whom; redirect desire |
| Vishwamitra | Years of effort; name the exact flaw (anger, pride, distraction) |
| Ramakrishna | Test it yourself; follow ONE path |
| Panini | Minimal rules, explicit conflict resolution |
| Nagarjuna | Find the load-bearing premise and push it to its consequences |
| Thiruvalluvar | Virtue first, then wealth, then desire |
| Gautama Buddha | Diagnose like a physician; Kalama harm test |
| C.V. Raman | Observe, ask why, simplest experiment, trust the measurement |
| Jiddu Krishnamurti | Who is asking; is the problem made by the framing |
| Srinivasa Ramanujan | Many cases, pattern first, proof second |
| APJ Abdul Kalam | Vision, one owner per part, own the failure |
| Verghese Kurien | Redesign ownership and incentives |
| Amartya Sen | Compare real options; what can people actually do |
| Mahavira | Many standpoints; hold conclusions lightly |
| Satyajit Ray | Plan visually, serve the viewer, cut |
| Veda Vyasa | Keep the whole record; which of the four aims is missing |
| **Lord Krishna (Chairman)** | Action without attachment to fruit; svadharma; return the choice |

Worldviews, signature questions, blind spots and sources: [docs/profiles.md](docs/profiles.md) and `agents/`.

## Use

Claude Code: run `./install.sh`, then `/council <problem>`.

```
/council --triad strategy Should I pitch this client now?
/council --members chanakya,hanuman,vyasa Is this partnership fair?
/council --quick Should I add this feature?
/council --duo --members hanuman,vishwamitra Ship now or wait?
/council --full What should I build this month?
```

Any other model: give it `SKILL.md` and the files in `agents/` and ask it to follow the coordinator sequence.

## Protocol in brief

Restate gate, then blind Round 1, then anonymized Round 2 (Member A, B, C), then an enforcement scan, then final stances (`STANCE | CONFIDENCE | DEALBREAKER`), then a weighted tally (domain seat 1.5x, 2/3 to reach consensus), then Krishna's verdict with kill criteria, exactly one next step, unresolved questions first, and a minority report. Vyasa keeps the outcome ledger.

## Honest limits

- The council is one model simulating many lenses. It is a thinking tool, not a panel of experts.
- Sources are English translations and scholarly summaries; the Sanskrit, Tamil and Pali originals were not read directly. Points marked "tradition" in the agent files come from tradition, not a text read in this project.
- Provider routing from the upstream project is not ported.

## Layout

```
SKILL.md                 coordinator instructions
skills/council/SKILL.md  same file, for Claude Code skill install
agents/                  19 member files + chairman-krishna.md
docs/profiles.md         researched profiles with sources
scripts/validate-roster.py
install.sh
```

MIT License. See `LICENSE` and `ATTRIBUTION.md`.

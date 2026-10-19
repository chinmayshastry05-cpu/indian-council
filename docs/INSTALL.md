# Install and use The Elite Club

Three ways to install. Pick one.

## Option 1: Claude Code plugin (recommended)

You need [Claude Code](https://code.claude.com) installed.

Step 1. In Claude Code, add the marketplace:

```
/plugin marketplace add chinmayshastry05-cpu/the-elite-club
```

Step 2. Install the plugin:

```
/plugin install elite-club@elite-club
```

Pick an installation scope when asked. If the install summary says `Run /reload-plugins to activate.`, run `/reload-plugins`.

Step 3. Run the council:

```
/elite-club:council Should I take this job offer?
```

Plugin commands are namespaced, so the command is `/elite-club:council`, not `/council`. The plugin also adds the 19 members and Chairman Krishna as agents.

## Option 2: Manual install into Claude Code

This gives you the short `/council` command.

Step 1. Clone the repo:

```
git clone https://github.com/chinmayshastry05-cpu/the-elite-club.git
cd the-elite-club
```

Step 2. Run the installer:

```
./install.sh
```

This copies the 19 member files and `chairman-krishna.md` into `~/.claude/agents/` and the council skill into `~/.claude/skills/council/`. It changes nothing else on your machine. To install somewhere else, set `CLAUDE_HOME` first:

```
CLAUDE_HOME=/path/to/dir ./install.sh
```

Step 3. Restart Claude Code, then run:

```
/council Should I take this job offer?
```

## Option 3: Any other model (ChatGPT, Gemini, and so on)

No install. Copy `SKILL.md` and everything in `agents/` into the chat (or attach the files), then say:

> Follow the coordinator sequence in SKILL.md. Here is my problem: ...

The model then plays the Coordinator, the members and the Chairman. Pick a panel in plain words, for example "quick mode" or "triad: strategy".

## First run

Try a small, real question in quick mode:

```
/council --quick Should I add this feature?
```

(With the plugin: `/elite-club:council --quick Should I add this feature?`)

What happens:

1. Each member restates your problem in one line, through their own method.
2. Round 1: every member analyzes independently. They cannot see each other.
3. Round 2: they cross-examine each other anonymously (Member A, B, C).
4. Final stances, then a weighted tally. The most on-domain member's vote counts 1.5x. Consensus needs 2/3 of the total weight.
5. Chairman Krishna, who took no part in the debate, writes the verdict. A real split goes back to you with both sides argued; it is never papered over.

## All the ways to run it

| Command | What you get |
|---|---|
| `/council <problem>` | Auto-picked triad (3 members) based on your problem |
| `/council --full <problem>` | All 19 members |
| `/council --quick <problem>` | Fast version: 200-word analyses, 75-word final positions, short verdict |
| `/council --triad <domain> <problem>` | A named 3-member combination (list below) |
| `/council --members a,b,c <problem>` | Your own pick of 2 to 11 members |
| `/council --duo --members a,b <problem>` | 2 members debate one polarity (no anonymization) |

Member names for `--members`: chanakya, hanuman, aryabhata, narada, vishwamitra, ramakrishna, panini, nagarjuna, thiruvalluvar, buddha, raman, krishnamurti, ramanujan, kalam, kurien, sen, mahavira, ray, vyasa.

Triads for `--triad`: ai, ai-product, ai-safety, architecture, bias, complexity, conflict, debugging, decision, design, dharma-dilemma, economics, ethics, founder, innovation, product, risk, shipping, strategy, synthesis, systems, uncertainty. The membership of each triad is listed in `SKILL.md`.

Examples:

```
/council --triad strategy Should I pitch this client now?
/council --members chanakya,hanuman,vyasa Is this partnership fair?
/council --duo --members hanuman,vishwamitra Ship now or wait?
/council --full What should I build this month?
```

## What the output looks like

The verdict has these sections, in this order:

- Problem
- Council Composition (panel, the 1.5x domain seat, Chairman: Krishna)
- Chairman note
- Acceptable Compromises
- Kill Criteria ("If X observed by DATE, the verdict is invalidated and we should Y")
- Concrete Next Step (exactly one: verb, object, date)
- Unresolved Questions (what the council does NOT know)
- Recommended Next Steps
- Consensus and Agreement
- Vote Tally (option, weight, backers with confidence; threshold 2/3)
- Key Insights by Member
- Points of Disagreement
- Minority Report
- Follow-Up

Quick mode writes a shorter verdict: Problem, Panel, Recommended Action, Kill Criteria, Concrete Next Step, Positions, Vote Tally, Key Disagreement.

After the verdict, Vyasa records the prediction and review date in an outcome ledger, so you can check later whether the council was right.

## Update

Plugin:

```
/plugin marketplace update elite-club
/plugin install elite-club@elite-club
```

Manual install:

```
cd the-elite-club
git pull
./install.sh
```

## Uninstall

Plugin:

```
/plugin uninstall elite-club@elite-club
```

Manual install: delete the copied files:

```
rm ~/.claude/agents/council-*.md ~/.claude/agents/chairman-krishna.md
rm -r ~/.claude/skills/council
```

(If you installed with `CLAUDE_HOME`, delete them from there instead.)

## Troubleshooting

- **`/council` does not exist after the plugin install.** Plugin commands are namespaced. Use `/elite-club:council`. The short `/council` only comes from the manual install (Option 2).
- **The command still does not show up.** Run `/reload-plugins`, or restart Claude Code.
- **`Marketplace "elite-club" not found`.** Do Step 1 first: `/plugin marketplace add chinmayshastry05-cpu/the-elite-club`.
- **`./install.sh: Permission denied`.** Run `chmod +x install.sh` first, or run it with `bash install.sh`.
- **`/council` does not exist after the manual install.** Restart Claude Code so it picks up new agents and skills. Then check the files landed: `ls ~/.claude/agents/ | grep council` should list 20 files (19 members + chairman-krishna.md).
- **Both installs at once.** They coexist (the plugin adds `/elite-club:council`, the manual install adds `/council`), but you do not need both. Pick one.

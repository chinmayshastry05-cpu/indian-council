#!/usr/bin/env python3
"""Check that agents/council-*.md frontmatter and SKILL.md describe the same council.

Usage: validate-roster.py [repo_root]
"""
import re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip3 install --user pyyaml")

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
REQ = {"figure", "domain", "polarity", "polarity_pairs", "triads", "duo_keywords", "reasoning_method"}
fails = []
agents = {}
for p in sorted((root / "agents").glob("council-*.md")):
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    if not m:
        fails.append(f"{p.name}: no frontmatter"); continue
    c = (yaml.safe_load(m.group(1)) or {}).get("council", {})
    miss = REQ - set(c)
    if miss: fails.append(f"{p.name}: missing {sorted(miss)}")
    agents[p.stem.removeprefix("council-")] = c
skill = (root / "SKILL.md").read_text()
for a, c in agents.items():
    if f"`council-{a}`" not in skill: fails.append(f"{a}: not in SKILL.md roster")
    for q in c.get("polarity_pairs", []):
        if q not in agents: fails.append(f"{a}: unknown polarity partner {q}")
if (root / "skills/council/SKILL.md").read_text() != skill:
    fails.append("skills/council/SKILL.md differs from SKILL.md")
if not (root / "agents/chairman-krishna.md").exists(): fails.append("chairman missing")
print(f"{len(agents)} members checked, {len(fails)} failures")
for f in fails: print(" -", f)
sys.exit(1 if fails else 0)

#!/usr/bin/env bash
# Install the Indian Council into Claude Code (~/.claude). Free, local copy only.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="${CLAUDE_HOME:-$HOME/.claude}"
mkdir -p "$dest/agents" "$dest/skills/council"
cp "$here"/agents/*.md "$dest/agents/"
cp "$here/skills/council/SKILL.md" "$dest/skills/council/SKILL.md"
echo "Installed 19 members + Chairman Krishna to $dest. Try: /council --quick <your question>"

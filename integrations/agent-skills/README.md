# Other Agent Skills hosts

The repository root is a valid Agent Skills folder (spec: https://agentskills.io/specification). Copy or clone it into the host's skills directory with the folder name `image-whisperer`:

| Host | Location (check the host's docs, paths can change) |
|---|---|
| Claude Code | `~/.claude/skills/image-whisperer/` or `<project>/.claude/skills/image-whisperer/` |
| Hosts that read `.agents/skills` | `<project>/.agents/skills/image-whisperer/` |
| Claude.ai / Claude apps | upload `dist/image-whisperer.zip` in Skills settings |

```bash
git clone https://github.com/peichh/image-whisperer.git ~/.claude/skills/image-whisperer
```

Validate with the reference tool: `pip install skills-ref && agentskills validate ./image-whisperer` (or run `python3 tests/test_skill.py`).

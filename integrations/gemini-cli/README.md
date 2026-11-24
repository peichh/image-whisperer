# Gemini CLI and Antigravity

Both read the Agent Skills format. Sources: https://geminicli.com/docs/cli/skills/ , https://antigravity.google/docs/skills

## Gemini CLI

```bash
# user-wide
gemini skills install https://github.com/peichh/image-whisperer.git
# or only for one project
gemini skills install https://github.com/peichh/image-whisperer.git --scope workspace
```

Or clone/copy the folder to `~/.gemini/skills/image-whisperer/` (user) or `<project>/.gemini/skills/image-whisperer/` (workspace). `~/.agents/skills/` and `.agents/skills/` also work.

Check with `/skills list`. Gemini asks to activate the skill when a request matches; you can also say "use image-whisperer".

Note: geminicli.com states that unpaid-tier and Google One users were moved from Gemini CLI to Antigravity CLI on 18 Jun 2026.

## Antigravity (app, CLI, IDE)

Copy the folder to one of:

- `<workspace>/.agents/skills/image-whisperer/`
- `~/.gemini/config/skills/image-whisperer/`

## Generating images from the CLI (optional)

Gemini CLI has no built-in image tool in its docs. If you want generation, add an MCP server or script that calls the Gemini image API with **your own** API key (see `../gemini-api/`). The skill works without it: it returns ready-to-paste prompts.

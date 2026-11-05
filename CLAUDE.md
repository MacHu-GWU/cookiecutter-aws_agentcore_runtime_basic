# CLAUDE.md

This is the **tpl repo** of a cookiecutter template for multi-environment AWS Bedrock AgentCore Runtime projects in Python: MCP server and agent runtimes written local first, deployed by the AgentCore CLI next to AWS CDK stacks, run with mise. The template is never edited directly: it is generated from a runnable **seed repo** (path: `CCTPL_SEED_DIR` in `mise.toml`) and published from here.

All maintenance rules live in the `cctpl-*-cn` skill family under `.claude/skills/`. Start with `cctpl-base-cn/SKILL.md`; it is the single source of truth and says which invoker fits which job:

| Job | Skill |
| :--- | :--- |
| Change the template (content or mechanism) | `/cctpl-change-cn` |
| Add, change, or remove a cookiecutter variable | `/cctpl-add-param-cn` |
| Regenerate the template from the seed and run all checks | `/cctpl-sync-cn` |
| Try a generated project locally | `/cctpl-try-cn` |
| Write this repo's changelog section for the current version | `/cctpl-changelog-cn` |
| Prepare a release (user only) | `/cctpl-release-cn` |
| Verify the published template (user only) | `/cctpl-verify-cn` |
| Copy this skill family to another tpl / seed repo pair, once (user only) | `/cctpl-fork-cn` |

Rules that hold even before a skill is loaded (details: `cctpl-base-cn/references/04-safety-rules.md`):

- Never run git write operations, `mise run publish-template` or `mise run publish-presets`; print the commands for the user instead.
- Never edit `cookiecutter.json`, `{{ cookiecutter.package_name }}-project/` or `README.rst` by hand; change the seed (or the parameterization) and run `mise run sync`.
- Never edit the version here: the seed and this repo share one version, its only source is the seed's `pyproject.toml`, and `mise run sync` copies it here.

## Current Status

Open items for this pair (keep this short; delete items when done):

- Bootstrapped from cookiecutter-aws_lbd (structure) and cookiecutter-aws_cdk (parameters, presets). The shared version is the seed's `1.0.0`. The seed tag `1.0.0` is on GitHub. Still to do: commit and push this repo, `/cctpl-release-cn`, `mise run publish-template`, then `/cctpl-verify-cn`.
- `QUICK_LINKS.md` enters the template with the seed's deployed dev runtime ids (such as `-b41N77CsYc`); a generated project fixes it with `mise run gen-quick-links` after its first deploy.

.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**



1.0.0 (2026-11-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Seed repo changes: `1.0.0 (2026-11-05) <https://github.com/MacHu-GWU/cookiecutter_aws_agentcore_runtime_basic_demo-project/blob/1.0.0/release-history-seed-repo.rst#100-2026-11-05>`__

**Features and Improvements**

- First release of the template for multi-environment AWS Bedrock AgentCore Runtime projects in Python: MCP server and agent runtimes written local first, deployed per environment by the AgentCore CLI next to AWS CDK stacks, run with mise.
- Variables: ``package_name``, ``github_username``, ``license`` (``MIT``, ``AGPL-3.0-or-later`` or ``LicenseRef-Proprietary``, written to ``pyproject.toml`` as an SPDX expression), ``author``, ``author_email``, ``version``, ``dev_python_version``, ``aws_region`` (every environment's config and the console URLs in ``mise.toml`` and ``QUICK_LINKS.md``), ``agentcore_project_name`` (the prefix of every AgentCore resource name), the secret fields ``github_token_field``, ``codecov_token_field`` and ``readthedocs_token_field``, and the AWS account ids ``dev_aws_account_id``, ``tst_aws_account_id`` and ``prd_aws_account_id``.
- ``hooks/pre_gen_project.py`` rejects, before anything is written, a ``dev_python_version`` other than ``3.12`` (the Python of every AgentCore runtime), an ``aws_region`` that is not a region code, an ``agentcore_project_name`` that is not a letter followed by letters and digits (at most 23 characters), and an account id that is not 12 digits.
- ``hooks/post_gen_project.py`` writes ``LICENSE.txt`` for the chosen license, copies ``.env`` and ``config/config-*-secret.json5`` from their examples, and fills in the account id of each environment.
- Presets ``bmt`` and ``esc``: use one with ``cookiecutter https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic --checkout preset/<name>``.

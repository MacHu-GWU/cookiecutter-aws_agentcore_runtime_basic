.. This file is the source of README.rst. Do not edit README.rst by hand:
   apply-template (mise run sync) renders it from this file.

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic


``cookiecutter-aws_agentcore_runtime_basic``
==============================================================================


Overview
------------------------------------------------------------------------------
This template provides a ready-to-use structure for a Python code base that builds and deploys `Amazon Bedrock AgentCore Runtime <https://docs.aws.amazon.com/bedrock-agentcore/>`_ runtimes (MCP servers and agents) across several environments (``dev``, ``tst``, ``prd``). The `AgentCore CLI <https://www.npmjs.com/package/@aws/agentcore>`_ deploys the runtimes; what they depend on, and every other AWS resource, is an `AWS CDK <https://docs.aws.amazon.com/cdk/>`_ stack built on `cdk_mate <https://github.com/MacHu-GWU/cdk_mate-project>`_. It generates a complete development environment that allows you to write, test, and deploy runtimes immediately.

**Key Features:**

- **Two sample runtimes that work together**: ``PowerPlantMcp``, an MCP server (FastMCP) with read-only tools over a small database, and ``SiteAgent``, a `Strands <https://strandsagents.com/>`_ agent on a Bedrock model that calls it over MCP and has a tool of its own
- **Local first**: Runtimes are plain Python modules in the package; run and call each one on your machine, run it packaged with ``agentcore dev``, then deploy the same code
- **One runtime registry**: Declare a runtime once; the AgentCore project (``agentcore.json``, ``aws-targets.json``, the CodeZip sources) and the per-environment and per-runtime mise tasks (deploy, destroy, status, invoke, logs, test) are generated from it
- **Multi-environment config**: One JSON5 file per environment plus git-ignored secret files, loaded into a typed config from which every AWS resource name derives; deployed to SSM Parameter Store for the runtimes to read
- **Stacks as code**: CDK stacks for the alerts, the publisher role and the runtimes' dependencies (``agentcore_deps``), with stack exports, synth-only unit tests (no AWS call), and integration tests against deployed stacks and runtimes
- **Modern tooling**: Uses `mise-en-place <https://mise.jdx.dev/>`_ for tools (Python, Node.js, the cdk CLI, the AgentCore CLI, AWS CLI) and tasks, and `uv <https://docs.astral.sh/uv/>`_ for fast Python package management
- **Complete CI/CD**: Pre-configured GitHub Actions, CodeCov, and ReadTheDocs integration, plus Sphinx documentation
- **AI ready**: Ships Claude Code skills that know the project's toolchain, its AgentCore and CDK conventions, and workflows to add, change, deploy and debug runtimes


Disclaimer
------------------------------------------------------------------------------
The best practices implemented in this repository reflect my personal experience from developing `over 150 open source Python libraries <https://pypi.org/user/machugwu/>`_, 200+ proof-of-concept initiatives, 100+ enterprise-grade applications, and 50+ production systems. This workflow enables me to publish a new Python library to PyPI within an hour of conception. While these practices have proven effective for me, please use them at your own discretion.


Usage
------------------------------------------------------------------------------
Enter the following command to use the latest template version:

.. code-block:: bash

    pip install "cookiecutter>=2.6.0,<3.0.0" && cookiecutter https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic

To use a specific released version (see the `full list of releases <https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic/releases>`_):

.. code-block:: bash

    cookiecutter https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic --checkout tags/${version}

For example, to use ``1.0.0``, the latest version:

.. code-block:: bash

    cookiecutter https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic --checkout tags/1.0.0

You'll then be prompted to provide the following information (defaults in parentheses):

.. code-block:: bash

    [1/15] Your Python package name, in snake case (e.g. my_package) (your_package_name): your_package_name
    [2/15] Your GitHub username, the owner of the new repo (your_github_username): your_github_username
    [3/15] Pick a license, as an SPDX expression for pyproject.toml, see https://choosealicense.com/ for details
      1 - MIT
      2 - AGPL-3.0-or-later
      3 - LicenseRef-Proprietary
      Choose from [1/2/3] (1): 1
    [4/15] Author name for pyproject.toml (Firstname Lastname): Firstname Lastname
    [5/15] Author email for pyproject.toml (firstname.lastname@email.com): firstname.lastname@email.com
    [6/15] Semantic Version, in {major}.{minor}.{micro} (e.g. 0.1.1) (0.1.1): 0.1.1
    [7/15] Python version for local development, in {major}.{minor} (e.g. 3.12) (3.12): 3.12
    [8/15] AWS region every environment (dev, tst, prd) deploys to (e.g. us-east-1) (us-east-1): us-east-1
    [9/15] AgentCore CLI project name, the prefix of every AgentCore resource name (such as MyProject_dev_SiteAgent): a letter, then letters and digits, at most 23 characters (MyProject): MyProject
    [10/15] GitHub token field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_github_token_field): your_github_token_field
    [11/15] Codecov.io token field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_codecov_token_field): your_codecov_token_field
    [12/15] Readthedocs.org token field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_readthedocs_token_field): your_readthedocs_token_field
    [13/15] AWS account id of the dev environment (123456789012): 123456789012
    [14/15] AWS account id of the tst environment (123456789012): 123456789012
    [15/15] AWS account id of the prd environment (123456789012): 123456789012

This will generate a repository structure similar to `cookiecutter_aws_agentcore_runtime_basic_demo-project <https://github.com/MacHu-GWU/cookiecutter_aws_agentcore_runtime_basic_demo-project>`_.

Once generated, navigate to your project directory and explore the available automation tasks:

.. code-block:: bash

    cd your_package_name-project
    mise tasks ls  # List all available tasks


Project Maintainer Note
------------------------------------------------------------------------------
**Project Architecture:**

- **Seed Repository**: `cookiecutter_aws_agentcore_runtime_basic_demo-project <https://github.com/MacHu-GWU/cookiecutter_aws_agentcore_runtime_basic_demo-project>`_ - A concrete, runnable project used as the source for template generation
- **Cookiecutter Template**: `cookiecutter-aws_agentcore_runtime_basic <https://github.com/MacHu-GWU/cookiecutter-aws_agentcore_runtime_basic>`_ - This repository

**Maintenance Workflow:**

This template is maintained using a "reverse engineering" approach, driven by Claude Code skills (``.claude/skills/cctpl-*-cn``):

1. Make changes in the Seed project (``cookiecutter_aws_agentcore_runtime_basic_demo-project``)
2. In the Seed, bump the version and record the changes in its own ``release-history-seed-repo.rst``. The Seed and this template share one version number, and the Seed's ``pyproject.toml`` is its only source
3. Run ``mise run e2e``: it converts the Seed into a template, checks it, applies it to this repo (version included), then generates a project and runs its tests and docs build
4. Commit and push the Seed, then tag it with ``mise run release`` in the Seed (push first: the tag goes on the latest commit of the Seed on GitHub)
5. Run ``/cctpl-release-cn`` to write this repo's changelog section, which links to the Seed's section of the same version, then ``mise run publish-template`` to publish the template to GitHub. A published version is never overwritten
6. Run ``/cctpl-verify-cn`` to verify the published template

**Toolchain:**

- **mise-en-place**: Task runner and tool version manager
- **uv**: Fast Python package installer and resolver
- **cookiecutter-maker**: Reverse-engineering tool that converts concrete projects into templates

For the full maintenance specification, see `cctpl-base-cn <./.claude/skills/cctpl-base-cn/SKILL.md>`_.

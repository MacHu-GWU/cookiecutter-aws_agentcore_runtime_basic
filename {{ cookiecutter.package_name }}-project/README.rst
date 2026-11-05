
.. .. image:: https://readthedocs.org/projects/{{ cookiecutter.package_name | slugify }}/badge/?version=latest
    :target: https://{{ cookiecutter.package_name | slugify }}.readthedocs.io/en/latest/
    :alt: Documentation Status

.. .. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/actions?query=workflow:CI

.. .. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project

.. image:: https://img.shields.io/badge/✍️_Release_History!--None.svg?style=social&logo=github
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/⭐_Star_me_on_GitHub!--None.svg?style=social&logo=github
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project

------

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://{{ cookiecutter.package_name | slugify }}.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/issues


Welcome to ``{{ cookiecutter.package_name }}`` Documentation
==============================================================================
.. .. image:: https://{{ cookiecutter.package_name | slugify }}.readthedocs.io/en/latest/_static/{{ cookiecutter.package_name }}-logo.png
    :target: https://{{ cookiecutter.package_name | slugify }}.readthedocs.io/en/latest/

A seed project for a multi-environment AWS Bedrock AgentCore Runtime code base (``dev``, ``tst``, ``prd``), with two sample runtimes that work together: ``PowerPlantMcp``, an MCP server, and ``SiteAgent``, an agent that calls it. The AgentCore CLI deploys the runtimes from ``agentcore/``; what they depend on, and every other AWS resource, is a Python CDK stack. How it is organized and how to work with it: the ``aws-agentcore-base`` skill (runtimes) and the ``pywf-aws-cdk-base`` skill (config, credentials, stacks) in ``.claude/skills/``.

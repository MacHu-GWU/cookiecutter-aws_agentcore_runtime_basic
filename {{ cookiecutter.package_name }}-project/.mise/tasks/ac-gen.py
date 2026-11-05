# -*- coding: utf-8 -*-

"""
Generate agentcore/agentcore.json, agentcore/aws-targets.json, and app/<Runtime>/
from the config, uv.lock, and the package.
"""

from {{ cookiecutter.package_name }}.agentcore_project.gen import main


if __name__ == "__main__":
    main()

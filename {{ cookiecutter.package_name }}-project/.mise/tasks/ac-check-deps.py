# -*- coding: utf-8 -*-

"""
Exit 1 unless what the AgentCore runtimes of the current environment (ENV_NAME)
depend on exists: the policy of the agentcore_deps stack, and the config parameter.
"""

import sys

from {{ cookiecutter.package_name }}.one.api import one

if __name__ == "__main__":
    sys.exit(0 if one.check_agentcore_deps() else 1)

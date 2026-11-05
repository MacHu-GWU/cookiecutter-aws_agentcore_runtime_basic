# -*- coding: utf-8 -*-

"""
Reject inputs the generated project cannot work with, before anything is written.
"""

import re
import sys

# The generated project pins requires-python, its classifiers and its CI matrix
# to these versions; mise.toml must use one of them.
# Every AgentCore runtime runs on one Python (RUNTIME_PYTHON in
# agentcore_project/registry.py), and the dev Python must match it.
SUPPORTED_PYTHON_VERSIONS = ["3.12"]

dev_python_version = "{{ cookiecutter.dev_python_version }}"

if dev_python_version not in SUPPORTED_PYTHON_VERSIONS:
    print(
        f"ERROR: dev_python_version must be one of "
        f"{', '.join(SUPPORTED_PYTHON_VERSIONS)}, got {dev_python_version!r}."
    )
    sys.exit(1)

# An AWS region code such as us-east-1, ap-southeast-2 or us-gov-west-1. It is
# written into config/config-<env>.json5 and the console URLs in mise.toml.
aws_region = "{{ cookiecutter.aws_region }}"

if not re.fullmatch(r"[a-z]{2}(-[a-z]+)+-\d+", aws_region):
    print(f"ERROR: aws_region must be an AWS region code such as us-east-1, got {aws_region!r}.")
    sys.exit(1)

# The AgentCore CLI project name, written into config/config-shared.json5. The
# Config model (config_00_main.py) and the AgentCore CLI accept a letter, then
# letters and digits, at most 23 characters.
agentcore_project_name = "{{ cookiecutter.agentcore_project_name }}"

if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]{0,22}", agentcore_project_name):
    print(
        f"ERROR: agentcore_project_name must be a letter, then letters and digits, "
        f"at most 23 characters, such as MyProject, got {agentcore_project_name!r}."
    )
    sys.exit(1)

# Written into config/config-*-secret.json5; every stack is bound to its account.
aws_account_ids = {
    "dev_aws_account_id": "{{ cookiecutter.dev_aws_account_id }}",
    "tst_aws_account_id": "{{ cookiecutter.tst_aws_account_id }}",
    "prd_aws_account_id": "{{ cookiecutter.prd_aws_account_id }}",
}

for name, value in aws_account_ids.items():
    if not re.fullmatch(r"\d{12}", value):
        print(f"ERROR: {name} must be a 12-digit AWS account id, got {value!r}.")
        sys.exit(1)

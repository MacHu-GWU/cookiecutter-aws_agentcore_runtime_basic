# -*- coding: utf-8 -*-

"""
Exit 0 only if the user answers y or yes:
``confirm.py --action <text> [--skip_var <VAR> ...]``.
"""

import sys

from {{ cookiecutter.package_name }}.confirm import main


if __name__ == "__main__":
    sys.exit(main())

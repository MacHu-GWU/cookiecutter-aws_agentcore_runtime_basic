# -*- coding: utf-8 -*-

"""
Run a runtime of the registry locally, or call it:
``ac-run.py --runtime <Name> --mode local|dev|call``.
"""

import sys

from {{ cookiecutter.package_name }}.devtools.local_run import main


if __name__ == "__main__":
    sys.exit(main())

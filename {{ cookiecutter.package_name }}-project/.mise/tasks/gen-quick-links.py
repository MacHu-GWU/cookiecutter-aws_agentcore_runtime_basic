# -*- coding: utf-8 -*-

"""
Rewrite QUICK_LINKS.md, the console of every AWS resource of every environment.
"""

from {{ cookiecutter.package_name }}.devtools.quick_links import main


if __name__ == "__main__":
    main()

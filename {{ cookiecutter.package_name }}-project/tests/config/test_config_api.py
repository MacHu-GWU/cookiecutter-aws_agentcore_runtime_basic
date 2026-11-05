# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.config import api


def test():
    _ = api
    _ = api.Config


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.config.api",
        preview=False,
    )

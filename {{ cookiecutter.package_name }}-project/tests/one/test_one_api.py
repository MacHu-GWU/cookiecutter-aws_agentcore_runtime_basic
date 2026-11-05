# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.one import api


def test():
    _ = api
    _ = api.One
    _ = api.one


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.one.api",
        preview=False,
    )

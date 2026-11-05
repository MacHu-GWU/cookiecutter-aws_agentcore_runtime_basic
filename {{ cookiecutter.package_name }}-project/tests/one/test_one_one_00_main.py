# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.one.one_00_main import One
from {{ cookiecutter.package_name }}.one.one_00_main import one

from {{ cookiecutter.package_name }}.env import env
from {{ cookiecutter.package_name }}.runtime import runtime


def test_one():
    """
    ``one`` exposes the module-level env and runtime singletons, not copies.
    """
    assert isinstance(one, One)
    assert one.env is env
    assert one.runtime is runtime


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.one.one_00_main",
        preview=False,
    )

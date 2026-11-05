# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.one.one_03_cdk import OneCdkMixin

from {{ cookiecutter.package_name }}.one.api import One
from {{ cookiecutter.package_name }}.cdk.stack_ctx_enum import (
    StackCtxEnum,
)
from {{ cookiecutter.package_name }}.cdk.stack_enum import StackEnum


def test_cdk():
    one = One()
    assert isinstance(one, OneCdkMixin)
    assert isinstance(one.stack_ctx_enum, StackCtxEnum)
    assert isinstance(one.stack_enum, StackEnum)
    assert one.stack_ctx_enum.one is one
    assert one.stack_enum.one is one


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.one.one_03_cdk",
        preview=False,
    )

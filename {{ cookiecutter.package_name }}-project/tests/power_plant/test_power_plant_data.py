# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.power_plant.data import SITES
from {{ cookiecutter.package_name }}.power_plant.data import ASSETS
from {{ cookiecutter.package_name }}.power_plant.data import TECHNICIANS
from {{ cookiecutter.package_name }}.power_plant.data import (
    SITE_TECHNICIANS,
)


def test_ids_are_unique():
    for table in [SITES, ASSETS, TECHNICIANS]:
        ids = [row["id"] for row in table]
        assert len(ids) == len(set(ids))


def test_foreign_keys_resolve():
    """Every asset and link row points at rows that exist."""
    site_ids = {row["id"] for row in SITES}
    technician_ids = {row["id"] for row in TECHNICIANS}
    for row in ASSETS:
        assert row["site_id"] in site_ids
    for row in SITE_TECHNICIANS:
        assert row["site_id"] in site_ids
        assert row["technician_id"] in technician_ids


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.power_plant.data",
        preview=False,
    )

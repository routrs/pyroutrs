import pytest  # noqa

import routrs


def test_it_adds():
    assert routrs.add_numbers(left=1, right=1) == 2


def test_it_calculates_maritime_distance():
    usnyc = (40.6759, -74.0504)
    trist = (41.0067858, 28.9732219)

    distance, path = routrs.maritime_distance(usnyc, trist)

    assert distance == 9224.95741604269
    assert len(path) == 117

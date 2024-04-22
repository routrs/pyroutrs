import pytest  # noqa
from routrs import maritime_distance


def test_it_calculates_maritime_distance():
    usnyc = (40.6759, -74.0504)
    trist = (41.0067858, 28.9732219)

    distance, path = maritime_distance(usnyc, trist)

    assert distance == 9224.95741604269
    assert len(path) == 118

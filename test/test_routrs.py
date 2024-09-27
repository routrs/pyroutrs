import pytest  # noqa
from routrs import (
    highway_distance,
    maritime_distance,
    par_highway_distance,
    par_maritime_distance,
    par_railway_distance,
    railway_distance,
)

Geoloc = tuple[float, float]


@pytest.fixture
def seaports():
    usnyc: Geoloc = (40.6759, -74.0504)  # USNYC port
    trist: Geoloc = (41.0067858, 28.9732219)  # TRIST port
    return usnyc, trist


@pytest.fixture
def cities():
    jiangsu_cn: Geoloc = (31.33068357, 120.902694)  # Jiangsu, China
    shanghai_cn: Geoloc = (31.05287995, 121.2232226)  # Shanghai, China
    return jiangsu_cn, shanghai_cn


@pytest.fixture
def railway_stations():
    gare_est: Geoloc = (48.8768, 2.3592)  # Gare de l'Est, Paris
    gare_msc: Geoloc = (43.3032, 5.3842)  # Gare de Marseille
    return gare_est, gare_msc


def test_it_calculates_maritime_distance(seaports: tuple[Geoloc, Geoloc]):
    distance, path = maritime_distance(*seaports)

    assert distance == 9224.95741604269
    assert len(path) == 118
    assert path[0] == seaports[0]
    assert path[-1] == seaports[1]


def test_it_calculates_par_maritime_distance(seaports: tuple[Geoloc, Geoloc]):
    distance, path = maritime_distance(*seaports)
    distances = par_maritime_distance([seaports] * 10)

    assert len(distances) == 10
    for d, p in distances:
        assert d == distance
        assert p == path


def test_it_calculates_highway_distance(cities: tuple[Geoloc, Geoloc]):
    distance, path = highway_distance(*cities)

    assert distance == 57.237115955889074
    assert len(path) == 39
    assert path[0] == cities[0]
    assert path[-1] == cities[1]


def test_it_calculates_par_highway_distance(cities: tuple[Geoloc, Geoloc]):
    distance, path = highway_distance(*cities)
    distances = par_highway_distance([cities] * 10)

    assert len(distances) == 10
    for d, p in distances:
        assert d == distance
        assert p == path


def test_it_calculates_railway_distance(railway_stations: tuple[Geoloc, Geoloc]):
    distance, path = railway_distance(*railway_stations)

    assert distance == 749.4744344461568
    assert len(path) == 603
    assert path[0] == railway_stations[0]
    assert path[-1] == railway_stations[1]


def test_it_calculates_par_railway_distance(cities: tuple[Geoloc, Geoloc]):
    distance, path = railway_distance(*cities)
    distances = par_railway_distance([cities] * 10)

    assert len(distances) == 10
    for d, p in distances:
        assert d == distance
        assert p == path

import pytest  # noqa
from routrs import highway_distance, maritime_distance, railway_distance


def test_it_calculates_maritime_distance():
    usnyc = (40.6759, -74.0504)
    trist = (41.0067858, 28.9732219)

    distance, path = maritime_distance(usnyc, trist)

    assert distance == 9224.95741604269
    assert len(path) == 118


def test_it_calculates_highway_distance():
    jiangsu_cn = (31.33068357, 120.902694)
    shanghai_cn = (31.05287995, 121.2232226)

    distance, path = highway_distance(jiangsu_cn, shanghai_cn)

    assert distance == 57.237115955889074
    assert len(path) == 39


def test_it_calculates_railway_distance():
    gare_est = (48.8768, 2.3592)  # Gare de l'Est, Paris
    gare_msc = (43.3032, 5.3842)  # Gare de Marseille-Saint-Charles, Marseille

    distance, path = railway_distance(gare_est, gare_msc)

    assert distance == 749.4744344461568
    assert len(path) == 603

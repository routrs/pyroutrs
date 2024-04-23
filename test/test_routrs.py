import pytest  # noqa
from routrs import highway_distance, maritime_distance, railway_distance


def test_it_calculates_maritime_distance():
    usnyc = (40.6759, -74.0504)  # USNYC port
    trist = (41.0067858, 28.9732219)  # TRIST port

    distance, path = maritime_distance(usnyc, trist)

    assert distance == 9224.95741604269
    assert len(path) == 118
    assert path[0] == usnyc
    assert path[-1] == trist


def test_it_calculates_highway_distance():
    jiangsu_cn = (31.33068357, 120.902694)  # Jiangsu, China
    shanghai_cn = (31.05287995, 121.2232226)  # Shanghai, China

    distance, path = highway_distance(jiangsu_cn, shanghai_cn)

    assert distance == 57.237115955889074
    assert len(path) == 39
    assert path[0] == jiangsu_cn
    assert path[-1] == shanghai_cn


def test_it_calculates_railway_distance():
    gare_est = (48.8768, 2.3592)  # Gare de l'Est, Paris
    gare_msc = (43.3032, 5.3842)  # Gare de Marseille-Saint-Charles, Marseille

    distance, path = railway_distance(gare_est, gare_msc)

    assert distance == 749.4744344461568
    assert len(path) == 603
    assert path[0] == gare_est
    assert path[-1] == gare_msc

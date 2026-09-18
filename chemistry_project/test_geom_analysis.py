import geom_analysis_lesson8 as ga
import pytest


def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)
    assert observed == expected


def test_bond_check_true():
    bond_distance = 1.2
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected


def test_bond_check_false():
    bond_distance = 2.0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected


def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected


def test_bond_check_1_5():
    bond_distance = 1.5
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected


def test_bond_check_negative():
    distance = -1
    with pytest.raises(ValueError):
        calculated = ga.bond_check(distance)


def test_open_xyz_wrong_extension():
    with pytest.raises(ValueError):
        ga.open_xyz("water.txt")
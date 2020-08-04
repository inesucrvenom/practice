import pytest
from slice_matrix import initialise, sum_submatrix, elder_age

"""
Tests for single block summation
sum_submatrix
"""

@pytest.mark.parametrize("modulo",[100])
@pytest.mark.parametrize(
    "a, c, r, loss, expected", [
    (0, 1, 1, 0, 0),
    (0, 2, 2, 0, 2),
    (0, 2, 3, 0, 7),
    (0, 5, 8, 0, 40),
    (0, 8, 5, 0, 40),
    (0, 8, 8, 0, 24),
])
def test_blocks(modulo, a, c, r, loss, expected):
    initialise(loss, modulo)
    assert sum_submatrix(a, c, r) == expected

@pytest.mark.parametrize("modulo",[100])
@pytest.mark.parametrize(
    "a, c, r, loss, expected", [
    pytest.param(0, 10, 10, 0, 94, marks=pytest.mark.xfail), # bigger than 8x8
])
def test_blocks_expected_fails(modulo, a, c, r, loss, expected):
    initialise(loss, modulo)
    assert sum_submatrix(a, c, r) == expected

# smaller modulo
@pytest.mark.parametrize("modulo",[10])
@pytest.mark.parametrize(
    "a, c, r, loss, expected", [
    (0, 1, 1, 0, 0),
    (0, 2, 2, 0, 2),
    (0, 2, 3, 0, 7),
    (0, 5, 8, 0, 0),
    (0, 8, 5, 0, 0),
    (0, 8, 8, 0, 4),
])
def test_blocks_small_mod(modulo, a, c, r, loss, expected):
    initialise(loss, modulo)
    assert sum_submatrix(a, c, r) == expected


# bigger loss
@pytest.mark.parametrize("modulo",[10])
@pytest.mark.parametrize(
    "a, c, r, loss, expected", [
    (8, 7, 6, 10, 5),
    (8, 5, 8, 20, 0),
    (16, 2, 3, 5, 3),
    (16, 5, 3, 15, 8),
    (8, 8, 8, 8, 4),
])
def test_blocks_small_mod_big_loss(modulo, a, c, r, loss, expected):
    initialise(loss, modulo)
    assert sum_submatrix(a, c, r) == expected

@pytest.mark.parametrize("modulo",[100])
@pytest.mark.parametrize(
    "a, c, r, loss, expected", [
    (8, 7, 6, 10, 75),
    (8, 5, 8, 20, 0),
    (800, 2, 3, 50, 7),
    (1600, 5, 3, 1500, 33),
    (80, 8, 8, 78, 52),
])
def test_blocks_big_mod_big_loss(modulo, a, c, r, loss, expected):
    initialise(loss, modulo)
    assert sum_submatrix(a, c, r) == expected

"""
Tests for main function
elder_age
"""

@pytest.mark.parametrize(
    "c, r, loss, modulo, expected", [
    (25, 34, 1, 1000, 776),
    (5, 4, 1, 1000, 30),
    (5, 8, 1, 1000, 105),
    (8, 4, 1, 1000, 84),
    (16, 4, 1, 1000, 420),
    (5, 16, 1, 1000, 525),
    (16, 8, 1, 10000, 840),
    (8, 16, 1, 10000, 840),
    (25, 34, 1, 10000, 3776),
    (10, 4, 3, 10000, 92),
    (5, 10, 2, 10000, 156),
    (32, 17, 0, 10000, 8432),
    (25, 34, 30, 10000,726),
    ])
def test_elder_my(c, r, loss, modulo, expected):
    assert elder_age(c, r, loss, modulo) == expected

@pytest.mark.parametrize(
    "c, r, loss, modulo, expected", [
    (8, 5, 1, 100, 5),
    (8, 8, 0, 100007, 224),
    (25, 31, 0, 100007, 11925),
    (5, 45, 3, 1000007, 4323),
    (31, 39, 7, 2345, 1586),
    (545, 435, 342, 1000007, 808451),
    ])
def test_elder_his(c, r, loss, modulo, expected):
    assert elder_age(c, r, loss, modulo) == expected

@pytest.mark.parametrize(
    "c, r, loss, modulo, expected", [
    (28827050410, 35165045587, 7109602, 13719506, 5456283),
    ])
def test_elder_his_tough(c, r, loss, modulo, expected):
    assert elder_age(c, r, loss, modulo) == expected

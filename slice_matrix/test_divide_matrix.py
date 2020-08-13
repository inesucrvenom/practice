import pytest
import mock
from divide_matrix import get_globals, apply_mod, apply_loss_mod
from divide_matrix import initialise, sum_square, sum_split_squares
from divide_matrix import sum_per_offset
from divide_matrix import elder_age

"""check if numeric globals and dict are correctly initialised"""
def test_initialise_globals():
    initialise(4, 22)
    assert get_globals()["LOSS"] == 4
    assert get_globals()["MODULO"] == 22
    assert get_globals()["global_previous"] == {}


"""check if initialise generates correct offset offset matrix of size 8"""
@mock.patch('divide_matrix.OFFSET_SIZE', 8)
def test_initialise_8x8(mocker):
    initialise(3, 10)
    assert get_globals()["OFFSET"] == [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 3, 2, 5, 4, 7, 6],
    [2, 3, 0, 1, 6, 7, 4, 5],
    [3, 2, 1, 0, 7, 6, 5, 4],
    [4, 5, 6, 7, 0, 1, 2, 3],
    [5, 4, 7, 6, 1, 0, 3, 2],
    [6, 7, 4, 5, 2, 3, 0, 1],
    [7, 6, 5, 4, 3, 2, 1, 0]
    ]


@mock.patch('divide_matrix.OFFSET_SIZE', 8)
def test_initialise_8x8_with_loss_and_mod():
    initialise(2, 5)
    assert get_globals()["OFFSET"] == [
    [0, 1, 2, 3, 4, 0, 1, 2],
    [1, 0, 3, 2, 0, 4, 2, 1],
    [2, 3, 0, 1, 1, 2, 4, 0],
    [3, 2, 1, 0, 2, 1, 0, 4],
    [4, 0, 1, 2, 0, 1, 2, 3],
    [0, 4, 2, 1, 1, 0, 3, 2],
    [1, 2, 4, 0, 2, 3, 0, 1],
    [2, 1, 0, 4, 3, 2, 1, 0]
    ]

""" testing correctness of functions """

@pytest.mark.parametrize(
    "first_row_id, first_col_id, dim, loss, mod, expected", [
    (0, 0, 1, 0, 100, 0),
    (0, 0, 8, 0, 1000, 224),
    (0, 0, 32, 0, 100, 72),
    (8, 8, 8, 10, 1000, 0),
    (8, 0, 8, 10, 1000, 120),
    (8, 0, 2, 10, 1000, 0),
])
def test_sum_square(first_row_id, first_col_id, dim, loss, mod, expected):
    initialise(loss, mod)
    assert sum_square(first_row_id, first_col_id, dim) == expected


@pytest.mark.parametrize(
    "first_row_id, first_col_id, dim_rows, dim_cols, loss, mod, expected", [
    (0, 0, 40, 20, 10, 10000, 9724),
])
def test_split_into_squares(first_row_id, first_col_id, dim_rows, dim_cols,
                            loss, mod, expected):
    initialise(loss, mod)
    assert sum_split_squares(first_row_id, first_col_id,
            dim_rows, dim_cols) == expected


@pytest.mark.parametrize(
    "first_row_id, first_col_id, dim_rows, dim_cols, loss, mod, expected", [
    (0, 0, 1, 1, 0, 100, 0),
    (0, 0, 8, 8, 0, 1000, 224),
    (8, 8, 8, 8, 10, 1000, 0),
    (8, 0, 8, 8, 10, 1000, 120), ##
    (8, 0, 2, 2, 10, 1000, 0),
    (0, 0, 5, 8, 1, 1000, 105),
    (0, 0, 8, 5, 1, 100, 5),
    (0, 0, 5, 4, 1, 1000, 30),
    ])
def test_sum_per_offset(first_row_id, first_col_id, dim_rows, dim_cols,
                                loss, mod, expected):
    initialise(loss, mod)
    assert sum_per_offset(first_row_id, first_col_id,
                dim_rows, dim_cols) == expected

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




@pytest.mark.timeout(1)  # expected crash
@pytest.mark.parametrize(
    "c, r, loss, modulo, expected", [
    (28827050410, 35165045587, 7109602, 13719506, 5456283),
    ])
def test_elder_tricky(c, r, loss, modulo, expected):
    assert elder_age(c, r, loss, modulo) == expected

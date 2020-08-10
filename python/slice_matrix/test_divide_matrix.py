import pytest
from unittest import mock
from divide_matrix import get_globals, apply_mod, apply_loss_mod
from divide_matrix import initialise, sum_square, split_into_squares

"""check if numeric globals and dict are correctly initialised"""
def test_initialise_globals():
    initialise(4, 22)
    assert get_globals()["LOSS"] == 4
    assert get_globals()["MODULO"] == 22
    assert get_globals()["global_previous"] == {}


"""check if initialise generates correct OFFLOSS offset matrix of size 8"""
@mock.patch('divide_matrix.SMALLEST_BLOCK_SIZE', 8)
def test_initialise_8x8():
    initialise(0, 10)
    assert get_globals()["OFFLOSS"] == [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 3, 2, 5, 4, 7, 6],
    [2, 3, 0, 1, 6, 7, 4, 5],
    [3, 2, 1, 0, 7, 6, 5, 4],
    [4, 5, 6, 7, 0, 1, 2, 3],
    [5, 4, 7, 6, 1, 0, 3, 2],
    [6, 7, 4, 5, 2, 3, 0, 1],
    [7, 6, 5, 4, 3, 2, 1, 0]
    ]

@mock.patch('divide_matrix.SMALLEST_BLOCK_SIZE', 8)
def test_initialise_8x8_with_loss():
    initialise(5, 10)
    assert get_globals()["OFFLOSS"] == [
    [0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 2, 1, 0, 0],
    [0, 0, 1, 2, 0, 0, 0, 0],
    [0, 0, 2, 1, 0, 0, 0, 0],
    [1, 2, 0, 0, 0, 0, 0, 0],
    [2, 1, 0, 0, 0, 0, 0, 0]
    ]


@mock.patch('divide_matrix.SMALLEST_BLOCK_SIZE', 8)
def test_initialise_8x8_with_loss_and_mod():
    initialise(2, 5)
    assert get_globals()["OFFLOSS"] == [
    [0, 0, 0, 1, 2, 3, 4, 0],
    [0, 0, 1, 0, 3, 2, 0, 4],
    [0, 1, 0, 0, 4, 0, 2, 3],
    [1, 0, 0, 0, 0, 4, 3, 2],
    [2, 3, 4, 0, 0, 0, 0, 1],
    [3, 2, 0, 4, 0, 0, 1, 0],
    [4, 0, 2, 3, 0, 1, 0, 0],
    [0, 4, 3, 2, 1, 0, 0, 0]
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

# def split_into_squares(first_row_id, first_col_id, dim_rows, dim_cols):

@pytest.mark.parametrize(
    "first_row_id, first_col_id, dim_rows, dim_cols, loss, mod, expected", [
    (0, 0, 40, 20, 10, 10000, 9724),
])
def test_split_into_squares(first_row_id, first_col_id, dim_rows, dim_cols,
                            loss, mod, expected):
    initialise(loss, mod)
    assert split_into_squares(first_row_id, first_col_id,
            dim_rows, dim_cols)== expected

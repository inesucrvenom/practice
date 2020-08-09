import pytest
from unittest import mock
from divide_matrix import get_globals, mod
from divide_matrix import initialise, sum_square

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


def helper_generate_matrix(a, r, c, loss, mod):
    mat = []
    for row in range(r):
        line = []
        for col in range(c):
            item = a + (row ^ col) - loss
            item = item % mod if item > 0 else 0
            line.append(item)
        mat.append(line)
    return mat

@pytest.mark.parametrize(
    "mat_params, dim, expected", [
    ([0, 1, 1, 0, 100], 1, 0),
    ([0, 8, 8, 0, 100], 1, 0),
    ([0, 8, 8, 0, 1000], 8, 224),
    ([5, 2, 2, 0, 100], 2, 22),
    ([0, 32, 32, 0, 100], 32, 72),
    ([1, 8, 8, 1, 1000], 8, 224),
])
def test_sum_square_trivial(mat_params, dim, expected):
    initialise(mat_params[3], mat_params[4])
    assert sum_square(helper_generate_matrix(*mat_params), dim) == expected
    # *mat_param will unpack the list

@pytest.mark.parametrize(
    "mat_params, dim, expected", [
    ([0, 8, 8, 5, 100], 8, -1),  # not implemented
])
def test_sum_square(mat_params, dim, expected):
    initialise(mat_params[3], mat_params[4])
    assert sum_square(helper_generate_matrix(*mat_params), dim) == expected
    # *mat_param will unpack the list

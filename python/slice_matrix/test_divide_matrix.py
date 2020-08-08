import pytest
from unittest import mock
from divide_matrix import initialise, get_globals

"""check if numeric globals are correctly initialised"""
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

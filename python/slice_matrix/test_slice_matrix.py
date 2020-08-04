from slice_matrix import sum_submatrix as ssub

def test_less_than_8x8():
    assert ssub(0,1,1,0) == 0, "0"

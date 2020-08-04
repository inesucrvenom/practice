import pytest
from slice_matrix import sum_submatrix as ssub
from slice_matrix import initialise

# sum_submatrix(a, c, r, loss):
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
def test_less_than_8x8(modulo, a, c, r, loss, expected):
    initialise(modulo)
    assert ssub(a, c, r, loss) == expected

@pytest.mark.parametrize("modulo",[100])
@pytest.mark.parametrize(
    "a, c, r, loss, expected", [
    pytest.param(0, 10, 10, 0, 94, marks=pytest.mark.xfail), # bigger than 8x8
])
def test_less_than_8x8_fails(modulo, a, c, r, loss, expected):
    initialise(modulo)
    assert ssub(a, c, r, loss) == expected




# if args.cnt_tests >= 1:
#     print(elder_age(25,34,1,15000),6)
#     print(prev)
#
# if args.cnt_tests >= 2:
#     print(elder_age(5,4,1,1000),30)
#     print(elder_age(5,8,1,1000),105)
#     print(elder_age(8,4,1,1000),84)
#     print(elder_age(16,4,1,1000),420)
#     print(elder_age(5,16,1,1000),525)
#     print(elder_age(16,8,1,10000),840)
#     print(elder_age(8,16,1,10000),840)
#     print(elder_age(25,34,1,10000),3776)
#     print(elder_age(10,4,3,10000),92)
#     print(elder_age(5,10,2,10000),156)
#     print(elder_age(32,17,0,10000),8432)
#     print(elder_age(25,34,30,10000),726)
# if args.cnt_tests >= 3:
#     print(elder_age(8,5,1,100), 5)
#     print(elder_age(8,8,0,100007), 224)
#     print(elder_age(25,31,0,100007), 11925)
#     print(elder_age(5,45,3,1000007), 4323)
#     print(elder_age(31,39,7,2345), 1586)
#     print(elder_age(545,435,342,1000007), 808451)
# #You need to run this test very quickly before attempting the actual tests :)
# if args.cnt_tests >= 4:
#     print(elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283);

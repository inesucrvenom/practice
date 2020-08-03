import argparse

debug = 0

def show_matrix(mat):
    result = '\n'.join([''.join(['{:3}'.format(item) for item in row])
      for row in mat])
    print(result, '\n')

DELTAS = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 3, 2, 5, 4, 7, 6],
    [2, 3, 0, 1, 6, 7, 4, 5],
    [3, 2, 1, 0, 7, 6, 5, 4],
    [4, 5, 6, 7, 0, 1, 2, 3],
    [5, 4, 7, 6, 1, 0, 3, 2],
    [6, 7, 4, 5, 2, 3, 0, 1],
    [7, 6, 5, 4, 3, 2, 1, 0]]

# todo
# save already computed sums
prev = {}
MODULO = 0

def mod(num):
    global MODULO
    return num % MODULO

def initialise(t):
    prev.clear()
    MODULO = t

def sum_submatrix(a, c, r, loss):
    '''
    returns sum of elements of a submatrix of c columns and r rows
    c, r <= 8

    submatrix is made from the matrix where:
    - a is value of element at position (0,0)
    - other elements are defined using following positional formulas

    a    a+1  a+2  a+3  a+4  a+5  a+6  a+7
    a+1  a    a+3  a+2  a+5  a+4  a+7  a+6
    a+2  a+3  a    a+1  a+6  a+7  a+4  a+5
    a+3  a+2  a+1  a    a+7  a+6  a+5  a+4
    a+4  a+5  a+6  a+7  a    a+1  a+2  a+3
    a+5  a+4  a+7  a+6  a+1  a    a+3  a+2
    a+6  a+7  a+4  a+5  a+2  a+3  a    a+1
    a+7  a+6  a+5  a+4  a+3  a+2  a+1  a
    '''
    global prev
    if not ((0 < c <= 8) and (0 < r <= 8)):
        raise ValueError("Row or col values are out of range")

    check = prev.get((a, c, r))
    if check != None:
        return check
    check = prev.get((a, r, c))
    if check != None:
        return check

    sum_a = 0
    if a > loss:
        item = a - loss
        for row in range(r):
            for col in range(c):
                sum_a += (item + DELTAS[row][col]) % mod
                sum_a = sum_a % mod
    else:
        for row in range(r):
            for col in range(c):
                sum_item = a + DELTAS[row][col] - loss
                sum_a += (sum_item % mod) if sum_item > 0 else 0
                sum_a = sum_a % mod

    prev[(a, c, r)] = sum_a
    prev[(a, r, c)] = sum_a
    return sum_a


def sum_split_table(c, r, loss):
    '''
    divide table into 8x8 blocks and the rest
    return its sum

    8x8         8x8         rest_colx8
    8x8         8x8         rest_colx8
    ...
    rest_rowx8  rest_rowx8  rest_row x rest_col
    '''
    total_sum = 0

    blocks_row = r // 8
    row_rest = r % 8
    blocks_col = c // 8
    col_rest = c % 8
    if debug: print('sst r', blocks_row, row_rest, 'c', blocks_col, col_rest)

    # let's do all 8x8 blocks, if they exist
    if blocks_row and blocks_col:
        for row in range(blocks_row):
            for col in range(blocks_col):
                a = (row * 8) ^ (col * 8)
                # todo check dic
                part_sum = sum_submatrix(a, 8, 8, loss)
                total_sum += part_sum % mod
                # if debug: print('8x8#', a, row, col, part_sum, total_sum)

    # the right bottom block, 7x7 or less, if it exists
    # also it's matrix of 7x7 or less, blocks_row and col will be 0
    if row_rest and col_rest:
        a = (blocks_row * 8) ^ (blocks_col * 8)
        part_sum = sum_submatrix(a, row_rest, col_rest, loss)
        total_sum += part_sum % mod
        if debug: print('rest#', a, part_sum, total_sum)

    # rightmost column except last block, size r-rest_row x rest_col
    # it exists if col_rest > 0
    if blocks_row > 1 and col_rest and blocks_col > 0:
        for row in range(blocks_row):
            a = (row * 8) ^ (blocks_col * 8)
            part_sum = sum_submatrix(a, 8, col_rest, loss)
            total_sum += part_sum % mod
            if debug: print('last col#', a, row, part_sum, total_sum)

    # bottom row except last block size rest_row x c-rest_col
    # it exists if row_rest > 0
    if blocks_col > 1 and row_rest:
        for col in range(blocks_col):
            a = (blocks_row * 8) ^ (col * 8)
            part_sum = sum_submatrix(a, row_rest, 8, loss)
            total_sum += part_sum % mod
            if debug: print('last row#', a, col, part_sum, total_sum)

    # matrix is a column of rest_col width, sum all except last block
    if blocks_row and col_rest and blocks_col == 0:
        for row in range(blocks_row):
            a = (row * 8) ^ 0
            part_sum = sum_submatrix(a, 8, col_rest, loss)
            total_sum += part_sum % mod
            if debug: print('single col#', a, row, part_sum, total_sum)

    # matrix is a row of rest_row height, sum all except last block
    if blocks_col and row_rest and blocks_row == 0:
        for col in range(blocks_col):
            a = (blocks_row * 8) ^ (col * 8)
            part_sum = sum_submatrix(a, row_rest, 8, loss)
            total_sum += part_sum % mod
            if debug: print('single row#', a, col, part_sum, total_sum)

    return total_sum % mod


def elder_age(m,n,l,t):
    initialise(t)
    if debug:
        print('---\n',m, n, l, t)
    if debug == 2:
        show_matrix(DELTAS)
        print(VECTOR)
        show_matrix(DELTAS_LOSS)
        print(VECTOR_LOSS)
    return sum_split_table(m, n, l)




parser = argparse.ArgumentParser()
parser.add_argument("debug", type=int, help="debug level")
parser.add_argument("cnt_tests", type=int, help="how many tests to run")
args = parser.parse_args()

debug = args.debug

if args.cnt_tests >= 1:
    print(elder_age(5,4,1,1000),30)
    print(elder_age(5,8,1,1000),105)
    print(elder_age(8,4,1,1000),84)
    print(elder_age(16,4,1,1000),420)
    print(elder_age(5,16,1,1000),525)
    print(elder_age(16,8,1,10000),840)
    print(elder_age(8,16,1,10000),840)
    print(elder_age(25,34,1,10000),3776)
    print(elder_age(10,4,3,10000),92)
    print(elder_age(5,10,2,10000),156)
    print(elder_age(32,17,0,10000),8432)
    print(elder_age(25,34,30,10000),726)
    print(prev)

if args.cnt_tests >= 2:
    print(elder_age(8,5,1,100), 5)
    print(elder_age(8,8,0,100007), 224)
    print(elder_age(25,31,0,100007), 11925)
    print(elder_age(5,45,3,1000007), 4323)
    print(elder_age(31,39,7,2345), 1586)
if args.cnt_tests >= 3:
    print(elder_age(545,435,342,1000007), 808451)
#You need to run this test very quickly before attempting the actual tests :)
if args.cnt_tests >= 4:
    print(elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283);

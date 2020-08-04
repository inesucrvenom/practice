DELTAS = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 3, 2, 5, 4, 7, 6],
    [2, 3, 0, 1, 6, 7, 4, 5],
    [3, 2, 1, 0, 7, 6, 5, 4],
    [4, 5, 6, 7, 0, 1, 2, 3],
    [5, 4, 7, 6, 1, 0, 3, 2],
    [6, 7, 4, 5, 2, 3, 0, 1],
    [7, 6, 5, 4, 3, 2, 1, 0]]

# save already computed sums, defined by largest item in matrix
prev = {}  # key: (a + 7 - LOSS) % time
prev_part = {}  # call by ( min(r,c), max(r,c), (a+7-LOSS) % time ) TUPLE!!!
MODULO = 0
LOSS = 0


def initialise(l, t):
    global MODULO, prev, prev_part, LOSS

    prev = {}
    prev_part = {}
    MODULO = t
    LOSS = l


def mod(num):
    global MODULO
    return num % MODULO


def sum_submatrix(a, c, r):
    """
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
    """
    global prev, prev_part

    if not ((0 < c <= 8) and (0 < r <= 8)):
        raise ValueError("Row or col values are out of range")

    biggest = (a + 7) - LOSS  # bottom right element

    # we have null-matrix if smallest and highest number are 0
    if biggest <= 0:
        return 0

    # matrix with only 1s on reverse diagonal
    if biggest == 1:
        # top part, all 0
        if (r < 8 - c) or (c < 8 - r):
            return 0
        else:
            return min(r, c)  # has only min(r,c) 1s

    # biggest > 1
    biggest_mod = mod(biggest)

    if 8 == r == c:
        check = prev.get(biggest_mod)  # for 8x8 matrix
    elif r < c:  # call for smaller, it's symmetrical
        check = prev_part.get((r, c, biggest_mod))  # it's a tuple!
    else:
        check = prev_part.get((c, r, biggest_mod))  # it's tuple!

    if check is not None:
        return check

    # everything else is when we don't already have it
    sum_a = 0
    for row in range(r):
        for col in range(c):
            # not mod here in case of negatives!
            sum_item = a + DELTAS[row][col] - LOSS
            sum_item = 0 if sum_item <= 0 else mod(sum_item)
            sum_a += sum_item
            sum_a = mod(sum_a)

    if 8 == r == c:
        prev[biggest_mod] = sum_a
    elif r < c:
        prev_part[(r, c, biggest_mod)] = sum_a
    else:
        prev_part[(c, r, biggest_mod)] = sum_a

    return sum_a


def sum_split_table(c, r):
    """
    divide table into 8x8 blocks, rightmost col, last row,  and the rest
    return its sum

    8x8         8x8         rest_colx8
    8x8         8x8         rest_colx8
    ...
    rest_rowx8  rest_rowx8  rest_row x rest_col
    """

    total_sum = 0

    blocks_row = r // 8
    row_rest = r % 8
    blocks_col = c // 8
    col_rest = c % 8

    # let's do all 8x8 blocks, if they exist
    if blocks_row and blocks_col:
        total_sum += all_8x8_blocks(blocks_col, blocks_row)

    # the right bottom block, 7x7 or less, if it exists
    # also it's matrix of 7x7 or less, blocks_row and col will be 0
    if row_rest and col_rest:
        total_sum += rest_block(blocks_col, blocks_row, col_rest, row_rest)

    # rightmost column except last block, size r-rest_row x rest_col
    # it exists if col_rest > 0
    if blocks_row and col_rest:
        total_sum += last_column_blocks(blocks_col, blocks_row, col_rest)

    # bottom row except last block size rest_row x c-rest_col
    # it exists if row_rest > 0
    if blocks_col and row_rest:
        total_sum += last_row_blocks(blocks_col, blocks_row, row_rest)

    return mod(total_sum)


def all_8x8_blocks(blocks_col, blocks_row):
    return_sum = 0
    for row in range(blocks_row):
        for col in range(blocks_col):
            a = (row * 8) ^ (col * 8)
            part_sum = sum_submatrix(a, 8, 8)
            return_sum += mod(part_sum)
            return_sum = mod(return_sum)
    return mod(return_sum)


def rest_block(blocks_col, blocks_row, col_rest, row_rest):
    return_sum = 0
    a = (blocks_row * 8) ^ (blocks_col * 8)
    part_sum = sum_submatrix(a, row_rest, col_rest)
    return_sum += mod(part_sum)
    return mod(return_sum)


def last_column_blocks(blocks_col, blocks_row, col_rest):
    return_sum = 0
    for row in range(blocks_row):
        a = (row * 8) ^ (blocks_col * 8)
        part_sum = sum_submatrix(a, 8, col_rest)
        return_sum += mod(part_sum)
        return_sum = mod(return_sum)
    return mod(return_sum)


def last_row_blocks(blocks_col, blocks_row, row_rest):
    return_sum = 0
    for col in range(blocks_col):
        a = (blocks_row * 8) ^ (col * 8)
        part_sum = sum_submatrix(a, row_rest, 8)
        return_sum += mod(part_sum)
        return_sum = mod(return_sum)
    return return_sum


def elder_age(m, n, l, t):
    initialise(l, t)
    return sum_split_table(m, n)


if __name__ == '__main__':
    assert elder_age(16, 4, 1, 1000) == 420

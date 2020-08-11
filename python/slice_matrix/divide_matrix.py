debug = 1
# pretty print of any matrix
def pretty_print(first_row, first_col, dim):
    print("first_row, first_col, dim", first_row, first_col, dim)
    sum_mat = 0
    for row in range(dim):
        sum_row = 0
        line = ""
        for col in range(dim):
            item = apply_loss_mod((first_row + row) ^ (first_col + col))
            sum_row += item
            line += "{:3}".format(item)
            if col % 8 == 7:
                line += " "
        sum_mat += sum_row
        print(line, " = ", sum_row)
        if row % 8 == 7:
            print()
    print(" == ", sum_mat)

"""
a^b == a XOR b (bitwise XOR) in the code
2**k == pow(2,k) (math exponent 2^k could happen in the comments)

version that uses formula for full square matrices as much as possible
- divides whole table into blocks recursively
- saves intermediary results
- checks for null matrices to return faster


full matrix of 8x8 looks like:

    a    a+1  a+2  a+3  a+4  a+5  a+6  a+7
    a+1  a    a+3  a+2  a+5  a+4  a+7  a+6
    a+2  a+3  a    a+1  a+6  a+7  a+4  a+5
    a+3  a+2  a+1  a    a+7  a+6  a+5  a+4
    a+4  a+5  a+6  a+7  a    a+1  a+2  a+3
    a+5  a+4  a+7  a+6  a+1  a    a+3  a+2
    a+6  a+7  a+4  a+5  a+2  a+3  a    a+1
    a+7  a+6  a+5  a+4  a+3  a+2  a+1  a

If we have full square matrix of any dim = 2**k, with top left element of a
then it's sum is:
sum_full = {all a elements + sum of matrix when a == o }
         = a * dim * dim + (dim / 2) * dim * (dim-1)
         = dim * dim * (a + (dim - 1)/2)


- every matrix split will looks like:
  ```
  A B       top-left = A        top-right = B
  C D       bottom-left = C     bottom-right = D
  ```
  - only A is a guaranteed to be a square matrix
    - until its dimensions are smaller or equal to the SMALLEST_BLOCK_SIZE
"""

# globals defined in the initalise function
global_previous = {}  # (min_dim, max_dim, biggest_element_modulo_LOSS) TUPLE!!!
OFFLOSS = []  # smallest block helper matrix
MODULO = 0
LOSS = 0

from math import log2

def get_globals():
    "function for testing purposes"
    return {
        "global_previous": global_previous,
        "OFFLOSS": OFFLOSS,
        "MODULO": MODULO,
        "LOSS": LOSS
    }

# constant independent of values given during the execution
SMALLEST_BLOCK_SIZE = 8  # todo: see if bigger block makes sense, and which
# todo: check for 32, 64, 128

def initialise(l, t):
    """
    will initialise
    - MODULO, LOSS : int, global constants
    - global_previous : dict, stores intermediary values of matrix sum calculations
        key: (min_dim, max_dim, biggest_element_modulo_LOSS)
            where dim are number of rows or columns
    - OFFLOSS : table, store offset values from a in a square matrix - LOSS
        - a is top left element
        - will be used to calculate sums for smallest non square block matrices
        - current size: SMALLEST_BLOCK_SIZE
    """
    global MODULO, LOSS, OFFLOSS, global_previous

    global_previous = {}
    MODULO = t
    LOSS = l
    OFFLOSS = []

    for row in range(SMALLEST_BLOCK_SIZE):
        new_row = []
        for col in range(SMALLEST_BLOCK_SIZE):
            new_row.append(apply_loss_mod(row ^ col))
        OFFLOSS.append(new_row)

def apply_mod(num):
    """ simplifies writing of modulo num """
    return num % MODULO

def apply_loss_mod(num):
    """ simplifies writing of modulo loss """
    tmp = num - LOSS
    tmp = tmp if tmp > 0 else 0
    return apply_mod(tmp)


def sum_split_loss(first_row_id, first_col_id, dim_rows, dim_cols):
    """
    every matrix split will be top-left A, top-right B, bottom-left C, bottom-right D
    A B
    C D

    based on loss
    find biggest s so that 2**s <= LOSS - that will give 2**s null submatrices A

    returns sum_of_elements
    """

    s = int(log2(LOSS))
    dim_splitter = 2**s

    result = 0

    dim_bottom_rows = dim_rows - dim_splitter
    dim_right_cols = dim_cols - dim_splitter

    # top left is null
    if dim_bottom_rows >= 0 and dim_right_cols >= 0:
        result += 0
    else:  # and there's nothing more beside null top left part
        return 0

    # bottom right is a candidate for repeating
    # but only if residual dimensions are bigger than dim_splitter
    if dim_splitter <= dim_bottom_rows and dim_splitter <= dim_right_cols:
        result += sum_split_loss(first_row_id + dim_splitter,
                                first_col_id + dim_splitter,
                                dim_bottom_rows,
                                dim_right_cols)
    else:
        result += sum_split_squares(first_row_id + dim_splitter,
                                    first_col_id + dim_splitter,
                                    dim_bottom_rows,
                                    dim_right_cols)

    # bottom left, split
    result += sum_split_squares(
            first_row_id + dim_splitter, first_col_id,
            dim_bottom_rows, dim_splitter
            )

    # top right, split
    result += sum_split_squares(
            first_row_id, first_col_id + dim_splitter,
            dim_splitter, dim_right_cols
            )

    return result

def sum_split_squares(first_row_id, first_col_id, dim_rows, dim_cols):
    """
    gets top left element indices, number of rows and columns
    find biggest k so that dim = 2**k <= smallest dim of B
    split B into new AA, BB, CC, DD where you use formula on AA and call split_into_squares on the rest

    returns sum_of_elements
    """

    # we entered too deep, maybe do tests before entering?
    if dim_rows <= 0 or dim_cols <= 0:
        return 0

    # find smallest k that 2**k x 2**k fits into dim_rows x dim_cols matrix
    kr = int(log2(dim_rows))
    kc = int(log2(dim_cols))
    k = min(kr, kc)
    dim_splitter = 2**k

    # not implemented yet
    # if dim_splitter <= SMALLEST_BLOCK_SIZE:
    #     return -1  # use old solutions, but think about narrow ones

    # nothing to split into
    if dim_rows == dim_cols == dim_splitter:
        return sum_square(first_row_id, first_col_id, dim_splitter)

    # else split into kxk, r-kxk, kxc-k, r-kxc-k
    result = 0

     # top left, 2**k x 2**k - sum only here, the rest are a new splits
    result += sum_square(first_row_id, first_col_id, dim_splitter)

    dim_bottom_rows = dim_rows - dim_splitter
    dim_right_cols = dim_cols - dim_splitter

    # bottom_right, 2**(r-k) x 2**(c-k)
    result += sum_split_squares(
                first_row_id + dim_splitter, first_col_id + dim_splitter,
                dim_bottom_rows, dim_right_cols
                )

    # bottom left, 2**(r-k) x 2**k
    result += sum_split_squares(
            first_row_id + dim_splitter, first_col_id,
            dim_bottom_rows, dim_splitter
            )

    # top right, 2**k x 2**(c-k)
    result += sum_split_squares(
            first_row_id, first_col_id + dim_splitter,
            dim_splitter, dim_right_cols
            )

    return result


def sum_square(first_row_id, first_col_id, dim):
    """ returns sum of matrix of dimension 2**k using formula"""
    global global_previous

    if debug: pretty_print(first_row_id, first_col_id, dim)
    smallest_el = apply_loss_mod(first_row_id ^ first_col_id)
    right_neighbour_el = apply_loss_mod(first_row_id ^ (first_col_id + 1))
    biggest_el = apply_loss_mod(first_row_id ^ (first_col_id + dim - 1))

    if smallest_el == 0 and biggest_el == 0:
        if debug: print("mat0", 0)
        return 0

    # already have it
    check = global_previous.get((biggest_el, dim))
    if check is not None:
        if debug: print("mat_have", check)
        return check

    # can use formula for matrix
    if right_neighbour_el == smallest_el + 1:
        tmp = apply_mod(dim * dim * (smallest_el + (dim - 1)/2))
        global_previous[(biggest_el, dim)] = tmp
        if debug: print("mat_full", tmp)
        return tmp

    # the rest has to be summed directly, we don't know how many 0s are there
    # but sum of the rows is the same for the each row
    sum_row = 0
    for col in range(dim):
        sum_row += apply_loss_mod(first_row_id ^ (first_col_id + col))

    tmp = apply_mod(apply_mod(sum_row) * dim)
    global_previous[(biggest_el, dim)] = tmp

    if debug: print("mat_calc", tmp)
    return tmp


def elder_age(m, n, l, t):
    initialise(l, t)
    return sum_split_table(n, m)  # reverse order bc it's easier for me

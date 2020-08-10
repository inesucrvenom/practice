debug = 1
# pretty print of any matrix
def pretty_print(mat):
    result = '\n'.join([''.join(['{:3}'.format(item) for item in row])
                        for row in mat])
    print(result, '\n')

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

# fals, we don't work with matrix itself, but only with indices, since matrix is
# generated - correct this part! and tests!
def split_by_loss(mat, r, c):
    """
    every matrix split will be top-left A, top-right B, bottom-left C, bottom-right D, where only A is a guaranteed square matrix unless it's smaller than SMALLEST_BLOCK_SIZE
    A B
    C D

    starting matrix has dimension row x col and LOSS
    find biggest s so that 2**s <= LOSS - that will give 2**s null submatrices in the main one

    rec_split: split the big one into A of dim 2**s and the rest

    A is zero, skip it
    call the same rec_split on D with same s

    for B and C call split_into_squares

    if any A, B, C, or D <= SMALLEST_BLOCK_SIZE stop and use old solutions


    returns sum_of_elements
    """
    if LOSS == 0: return split_into_squares(mat, r, c)
    pass

def split_into_squares(first_row_id, first_col_id, dim_rows, dim_cols):
    """
    gets matrix, and its dimensions, rows and columns
    find biggest k so that dim = 2**k <= smallest dim of B
    split B into new AA, BB, CC, DD where you use formula on AA and call split_into_squares on the rest

    leave this if needed for optimisation
    if any A, B, C, or D <= SMALLEST_BLOCK_SIZE stop and use old solutions

    returns sum_of_elements
    """

    # we entered too deep, maybe do tests before entering?
    if dim_rows <= 0 or dim_cols <= 0:
        return 0

    kr = int(log2(dim_rows))
    kc = int(log2(dim_cols))
    k = min(kr, kc)  # smallest k that 2**k x 2**k fits into r x c matrix
    dim_splitter = 2**k

    if k == 0: return apply_mod(mat[0][0])

    # early returns
    check = global_previous.get((first_row_id, first_col_id, dim_splitter))
    if check is not None:
        return check

    # nothing to split into
    if dim_rows == dim_cols == dim_splitter:
        return sum_square(first_row_id, first_col_id, dim_splitter)

    # else split into kxk, r-kxk, kxc-k, r-kxc-k
    result = 0

     # k x k - sum only here, the rest are a new splits
    result += sum_square(first_row_id, first_col_id, dim_splitter)

    # r-k x c-k
    result += split_into_squares(
                first_row_id + dim_splitter, first_col_id + dim_splitter,
                dim_rows - dim_splitter, dim_cols - dim_splitter
                )

    # r-k x k
    result += split_into_squares(
            first_row_id + dim_splitter, first_col_id,
            dim_rows - dim_splitter, dim_splitter
            )

    # k x c-k
    result += split_into_squares(
            first_row_id, + dim_splitter,
            dim_splitter, dim_cols - dim_splitter
            )

    return result


def sum_square(first_row_id, first_col_id, dim):
    """ returns sum of matrix of dimension 2**k using formula"""
    global global_previous

    smallest = apply_loss_mod(first_row_id ^ first_col_id)
    next = apply_loss_mod(first_row_id ^ (first_col_id + 1))
    biggest = apply_loss_mod(first_row_id ^ (first_col_id + dim - 1))

    if smallest == 0 and biggest == 0:
        global_previous[(first_row_id, first_col_id, dim)] = 0
        return 0
    if next == smallest + 1:
        tmp = apply_mod(dim * dim * (smallest + (dim - 1)/2))
        global_previous[(first_row_id, first_col_id, dim)] = tmp
        return tmp

    # the rest has to be summed directly, we don't know how many 0s are there
    # but sum of the rows is the same for the each row
    sum_row = 0
    for item in range(dim):
        sum_row += apply_loss_mod(first_row_id ^ item)

    tmp = apply_mod(apply_mod(sum_row) * dim)
    global_previous[(first_row_id, first_col_id, dim)] = tmp

    return tmp


def elder_age(m, n, l, t):
    initialise(l, t)
    return sum_split_table(n, m)  # reverse order bc it's easier for me

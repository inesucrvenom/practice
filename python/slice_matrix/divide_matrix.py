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

# constant independent of values given during the execution
SMALLEST_BLOCK_SIZE = 8  # todo: see if bigger block makes sense, and which

def initialise(l, t):
    """
    will initialise
    - MODULO, LOSS : int, global constants
    - global_previous : dict, stores intermediary values of matrix sum calculations
        key: (min_dim, max_dim, biggest_element_modulo_LOSS)
            where dim are number of rows or columns
    - OFFLOSS : table, store offset values from a (top left) in square matrix, - LOSS
        - will be used to calculate sums for smallest non square block matrices
        - current size: SMALLEST_BLOCK_SIZE
    """
    global MODULO, LOSS, OFFLOSS, global_previous

    prev = {}
    MODULO = t
    LOSS = l

def mod(num):
    """ simplifies writing of modulo num """
    global MODULO
    return num % MODULO


def split_by_loss():
    """
    every matrix split will be top-left A, top-right B, bottom-left C, bottom-right D, where only A is square matrix unless it's smaller than SMALLEST_BLOCK_SIZE
    ```
    A B
    C D
    ```


    starting matrix has dimension row x col and LOSS
    find biggest s so that 2**s <= LOSS - that will give 2**s null submatrices in the main one

    rec_split: split the big one into A of dim 2**s and the rest

    A is zero, skip it
    call the same rec_split on D with same s

    for B and C call split_into_squares

    if any A, B, C, or D <= SMALLEST_BLOCK_SIZE stop and use old solutions


    returns sum_of_elements
    """
    pass

def split_into_squares():
    pass

    """
    find biggest k so that dim = 2**k <= smallest dim of B
    split B into new AA, BB, CC, DD where you use formula on AA and call split_into_squares on the rest
    if any A, B, C, or D <= SMALLEST_BLOCK_SIZE stop and use old solutions

    returns sum_of_elements
    """

debug = 1

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
VECTOR = 28

# will be modified only once, by function make_loss,
# then used as a constant would be
DELTAS_LOSS = []
VECTOR_LOSS = 0


def make_loss(loss):
    '''
    modify helper table DELTAS_LOSS from DELTAS and subtracting loss
    modify helper VECTOR_LOSS
    '''
    global DELTAS_LOSS = [[0 for col in range(8)] for row in range(8)]
    global VECTOR_LOSS = 0

    for row in range(8):
        for col in range(8):
            check = DELTAS[row][col] - loss
            DELTAS_LOSS[row][col] = 0 if check < 0 else check


def sum_submatrix(a, c, r):
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

    if not ((0 < c <= 8) and (0 < r <= 8)):
        #        raise ValueError("Row or col values are out of range")
        print("Row or col values are out of range")

    # each full row/cols is worth 8a + 28
    # just see how many times you have them (col/row times)
    if r == 8:
        return c * (8*a + 28)
    if c == 8:
        return r * (8*a + 28)

    sum_a = 0
    for row in range(r):
        for col in range(c):
            sum_a += a + deltas[row][col]
    return sum_a


def sum_submatrix_loss(c, r, loss):
    '''

    '''
    pass

def subtract_loss(a, c, r, loss):
    '''
    return sum of a table (less or equal to 8x8) where loss is subtracted
    '''
    if loss <= a:
        result = sum_submatrix(a - loss, c, r)
    else:
        result = sum_submatrix_loss(c, r)
    return result

def


def elder_age(m,n,l,t):
    if debug:
        show_matrix(DELTAS)
        print(VECTOR)
        show_matrix(DELTAS_LOSS)
        print(VECTOR_LOSS)

    pass



debug = 1

elder_age(5,5,1,100), 5)
elder_age(8,5,1,100), 5)
elder_age(8,8,0,100007), 224)
elder_age(25,31,0,100007), 11925)
#elder_age(5,45,3,1000007), 4323)
#elder_age(31,39,7,2345), 1586)
#elder_age(545,435,342,1000007), 808451)
#You need to run this test very quickly before attempting the actual tests :)
#elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283);

def slow_print(m, n, l):
    sum_all = 0
    for row in range(n):
        line = ''
        sum_line = 0
        for col in range(m):
            item = row ^ col
            item = item - l if item >= l else 0
            line += '{:>3}'.format(item)
            sum_line += item
            if col % 8 == 7:
                line += '  '
        line += ' = {}'.format(sum_line)
        print(line)
        sum_all += sum_line
        if row % 8 == 7:
            print()
    print('== ', sum_all)
    return

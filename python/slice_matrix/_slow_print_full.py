print_pattern = 0

# dummy version, for testing purposes
def slow_print(m, n, l, t):
    print(m, n, l, t)
    sum_all = 0
    for row in range(n):
        line = ''
        sum_line = 0
        for col in range(m):
            item = row ^ col
            item = item - l if item >= l else 0
            sum_line += item
            if print_pattern:
                print_item = "_" if item == 0 else "#"
                line += '{:>1}'.format(print_item)
            else:
                line += '{:>3}'.format(item)
            if col % 8 == 7:
                line += ' '
        line += ' = {}'.format(sum_line)
        print(line)
        sum_all += sum_line
        if row % 8 == 7:
            print()
    print('== ', sum_all % t)

def slow_print_no_table(m, n, l, t):
    print(m, n, l, t)
    sum_all = 0
    show_lines = ''
    sum_prev_line = 0
    for row in range(n):
        sum_line = 0
        for col in range(m):
            item = row ^ col
            item = item - l if item >= l else 0
            sum_line += item
        if sum_line != sum_prev_line:
            show_lines += '({}) = {}'.format(row, sum_line)
            sum_prev_line = sum_line
        sum_all += sum_line
    print(show_lines)
    print('== ', sum_all % t)
    return sum_all


""" ### testing area """
do_this = 4
""" toggle switch """

if do_this == 1 and __name__ == '__main__':
    dim = 32
    mod = pow(10,5)
    loss = 24
    slow_print(dim, dim, loss, mod)

# print pattern only
if do_this == 3 and __name__ == '__main__':
    print_pattern = 1
    dim = 8*10
    mod = pow(10,5)
    loss = pow(2,5)+2 # 2^6, 64, 8x 8blocks je 64
    slow_print(dim, dim, loss, mod)


if do_this == 2 and __name__ == '__main__':
    for i in range(10):
        dim = pow(2, i)
        formula = (dim / 2) * dim * (dim-1)
        formula = int(formula)
        print("{}x{}={}".format(dim, dim, formula))
        assert formula == slow_print_no_table(dim, dim, 0, pow(10,10))


if do_this == 4 and __name__ == '__main__':
    dim = pow(2, 5) # 
    formula = (dim / 2) * dim * (dim-1)
    formula = int(formula)
    print("{}x{}={}".format(dim, dim, formula))
    assert formula == slow_print_no_table(dim, dim, 0, pow(10,10))

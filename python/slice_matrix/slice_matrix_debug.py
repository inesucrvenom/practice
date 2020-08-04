import argparse

debug = 1

# dummy version, for testing purposes
def slow_print(m, n, l, t):
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
    print('== ', sum_all % t)



parser = argparse.ArgumentParser()
parser.add_argument("fn", type=str, help="which function to call")
parser.add_argument("debug", type=int, help="debug level")
parser.add_argument("col", type=int, help="columns of the matrix")
parser.add_argument("row", type=int, help="rows of the matrix")
parser.add_argument("loss", type=int, help="amount of loss")
parser.add_argument("t", type=int, help="modulo")
args = parser.parse_args()

debug = args.debug


if args.fn == 'slow':
    slow_print(args.col, args.row, args.loss, args.t)

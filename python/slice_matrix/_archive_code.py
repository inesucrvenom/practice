# example usage of command line arguments

import argparse

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


# pretty print of any matrix
def show_matrix(mat):
    result = '\n'.join([''.join(['{:3}'.format(item) for item in row])
                        for row in mat])
    print(result, '\n')

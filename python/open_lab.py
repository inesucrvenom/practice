import random

""" Made in 2015 """

"""Using generative recursion search"""
# all possible moves
moves = {'S': [1, 0], 'N': [-1, 0], 'E': [0, 1], 'W': [0, -1]}
opposite = {'S': 'N', 'N': 'S', 'E': 'W', 'W': 'E'}
SIZE = 9
START = [1, 1]
END = [10, 10]
PIT = 1


def find(path, board):
    """Generating arbitrary arity tree + backtracking search over it"""
    def find__path(path):
        """Search for path that reach the end position,
        else generate new candidates"""
        if is_found(path):
            return path
        else:
            return find__lopath(next_paths(path, board))

    def find__lopath(lopath):
        """Test each path in given list if is it solution"""
        if len(lopath) == 0:
            return False
        else:
            # backtracking search
            test = find__path(lopath[0])
            if test:
                return test
            else:
                return find__lopath(lopath[1:])
    return find__path(path)


def is_found(path):
    """Return True if solution is found - end position is reached"""
    if path == "":
        return False
    else:
        return path_to_pos(path) == END


def path_to_pos(path):
    """Return position that path reached"""
    pos = list(START)
    for d in path:
        pos[0] += moves[d][0]
        pos[1] += moves[d][1]
    return pos


def value_from_pos(pos, board):
    return board[pos[0]][pos[1]]


def next_paths(path, board):
    """Return list of valid next paths from given
    Assume: only move forward, no returning back in same path"""
    # generate path candidates
    candidates = [path + m for m in moves]

    # filter paths that don't fall into PIT
    # and are not going in opposite direction
    valid_paths = []
    for c in candidates:
        if (len(c)) >= 2:
            if ((value_from_pos(path_to_pos(c), board) != PIT)
                    and c[-2] != opposite[c[-1]]):
                valid_paths.append(c)
        elif (value_from_pos(path_to_pos(c), board) != PIT):
            valid_paths.append(c)

    # filter out paths that have cycle
    valid_paths = [c for c in list(valid_paths)
                   if not has_cycle(c, board)]

    return valid_paths


def has_cycle(path, board):
    """Return True if path has cycle - has duplicate positions"""
    sub_paths = [path[:i+1] for i in range(len(path))]
    list_pos = [path_to_pos(p) for p in sub_paths]
    non_unique = [d for d in list_pos if list_pos.count(d) > 1]
    if len(non_unique):
        return True
    else:
        return False


def checkio(maze_map):
    return find("", maze_map)

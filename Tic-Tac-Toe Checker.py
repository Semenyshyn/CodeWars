import numpy as np
import collections
a = [[2, 0, 2, 1],
     [2, 2, 2, 2],
     [1, 0, 1, 2],
     [1, 2, 0, 1]]


def winer_is(board):
    for i in board:
        for j in i:
            if i.count(j) == len(i):
                return j
    x = np.diagonal(board)
    if len(collections.Counter(x).values()) == 1:
        return x[0]
    z = np.diagonal(board[::-1])
    if len(collections.Counter(z).values()) == 1:
        return z[0]


def isSolved(board):
    if winer_is(board):
        return winer_is(board)
    b = np.transpose(board)
    z = np.ndarray.tolist(b)
    if winer_is(z):
        return winer_is(z)
    for i in board:
        for j in i:
            if j == 0:
                return -1
    else:
        return 0

print(isSolved(a))
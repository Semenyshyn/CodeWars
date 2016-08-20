import numpy as np

n = 5
a = np.zeros(shape=(n, n))
m = [[0] * n for i in range(n)]


def spialize(size):
    zer = [[0] * size for i in range(size)]
    l = 0
    while size >= 5:
        for j in range(size):
            zer[l][j] = 1
            zer[j][l] = 1
            size -= 2
            l += 1
    return zer


b = spialize(10)
for i in b:
    print(i)
s = [1, 1, 1, 0, 1, 2, 2, -3, -3, -3]


def sum_consecutives(s):
    prev = None
    x = []
    for i in s:
        if i == prev:
            x[-1] += i
        else:
            x.append(i)
        prev = i
    return x

print(sum_consecutives(s))
def nbr_of_laps(x, y):
    result = []
    i = 1
    z = min(x, y)
    while i < z+1:
        if x % i == 0 and y % i == 0:
            x = x / i
            y = y / i
            i = 1
            print(y, x)
            result = []
            result.append(y)
            result.append(x)
            print(result)
        i += 1
    return result

nbr_of_laps(5, 5)

'''
from fractions import gcd

def nbr_of_laps(x, y):
    return (y / gcd(x,y), x / gcd(x,y))
'''
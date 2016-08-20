x = 'AAAABBBAAAaaabbb111122211'

def unique_in_order(iterable):
    if not iterable:
        return iterable
    d = [iterable[0]]
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i+1]:
            d.append(iterable[i+1])
    return d

print(unique_in_order(x))
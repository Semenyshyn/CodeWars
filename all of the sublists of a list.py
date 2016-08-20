import itertools


def power(stuff):
    d = []
    for L in range(0, len(stuff)+1):
      for subset in itertools.combinations(stuff, L):
          d.append(list(subset))
    return d

print(power([1, 2, 3, 4]))
s = [1, 2, 3]
print(list(itertools.combinations(s, 3)))

'''
def power(s):
  set = [[]]
  for num in s:
    set += [x+[num] for x in set]
  return set
'''

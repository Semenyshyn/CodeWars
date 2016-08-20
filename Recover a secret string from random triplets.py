import numpy as np
triplets = [
  ['t', 'u', 'p'],
  ['w', 'h', 'i'],
  ['t', 's', 'u'],
  ['a', 't', 's'],
  ['h', 'a', 'p'],
  ['t', 'i', 's'],
  ['w', 'h', 's']
]

secret = 'whatisup'


def all_letters(t):
    u = []
    for i in t:
        for j in i:
            u.append(j)
    return list(set(u))


def recoverSecret(triplets):
    secret = ''
    b = all_letters(triplets)
    while b:
        for j in b:
            a = np.transpose(triplets)
            if (j not in a[1]) and (j not in a[2]):
                secret += j
                for i in triplets:
                    if j in i:
                        i[0], i[1], i[2] = i[1], i[2], '0'
                b.remove(j)
    return print(secret)


recoverSecret(triplets)

'''
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)
'''


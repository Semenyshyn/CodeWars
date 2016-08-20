def Paskal(n):
    sp = []
    for o in range(0, n):
        sp.append([])
    sp[0].append(1)
    for i in range(1, n):
        sp[i].append(1)
        for j in range(1, i - 1):
            k = sp[i - 1][j - 1] + sp[i - 1][j]
            sp[i].append(k)
        sp[i].append(1)
    sp.__delitem__(1)
    return sp


def sierpinski(n):
    k = 2 ** n + 1
    s = Paskal(k)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] % 2 == 0:
                s[i][j] = ' '
            else:
                s[i][j] = 'L'
    u = ''
    for i in s:
        u = u[0:len(u)-1]
        u += '\n'
        for j in i:
            u += '{0} '.format(str(j))
    u = u[1:]
    return u.rstrip()

print(sierpinski(11))


def sierpinski1(n):
    r = ['L']
    for i in range(n):
        l = len(r)
        print('l --', l)
        for j in range(l):
            print(j)
            print(r[j].ljust(l * 2)+r[j])
            r.append(r[j].ljust(l * 2) + r[j])
            print(r)
    return '\n'.join(r)



print(sierpinski1(11))
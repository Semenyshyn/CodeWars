a = "abcdef"
b = "acf"


def lcs_adopted(xs, ys):
    if xs and ys:
        *xb, xe = xs
        *yb, ye = ys
        if xe == ye:
            return lcs_adopted(xb, yb) + [xe]
        else:
            return max(lcs_adopted(xs, yb), lcs_adopted(xb, ys), key=len)
    else:
        return []


def lcs(x, y):
    return ''.join(lcs_adopted(x, y))

print(lcs(a, b))


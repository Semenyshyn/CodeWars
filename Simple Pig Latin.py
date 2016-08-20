import string
a = 'Pig latin is cool ?'


def pig_it(text):
    t = text.split()
    s = []
    for o in t:
        if o in string.punctuation:
            s.append(o)
        else:
            i = o[1:]+o[:1]+'ay'
            s.append(i)
    return ' '.join(s)
'''
print(pig_it(a))

exclude = set(string.punctuation)
s = "string. With. Punctuation?"
s = ''.join(ch for ch in s if ch not in exclude)

print(string.punctuation)
_________________________
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''
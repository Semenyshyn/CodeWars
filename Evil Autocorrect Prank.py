import re
x = 'U or You or youuuuuuuuu love youtube'


def autocorrect(input):
    return re.sub(r'\b(?i)(yo[u]+|u)\b', 'your sister', input)


print(autocorrect('U or You or youuuuuuuuu love youtube'))
print(re.sub(r'you', 'your sister', x))
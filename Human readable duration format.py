import math


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    s = seconds % 60
    m = math.floor((seconds - s) / 60) % 60
    h = math.floor(((seconds - s) / 60 - m) / 60) % 24
    d = math.floor((((seconds - s) / 60) / 60 - h) / 24) % 365
    y = math.floor(((((seconds - s) / 60) / 60 - h) / 24 - d)/365)
    val = [y, d, h, m, s]
    names = ['years', 'days', 'hours', 'minutes', 'seconds']
    val1 = []
    nam1 = []
    for i in range(len(val)):
        if val[i] != 0:
            val1.append(val[i])
            nam1.append(names[i])
    res = ''
    l = len(val1)
    for i in range(l):
        if l > 2:
            if val1[i] == 1:
                res += str(val1[i]) + ' ' + nam1[i][:-1] + ', '
            else:
                res += str(val1[i]) + ' ' + nam1[i] + ', '
            l -= 1
        else:
            if val1[i] == 1:
                res += str(val1[i]) + ' ' + nam1[i][:-1] + ' and '
            else:
                res += str(val1[i]) + ' ' + nam1[i] + ' and '
    return print(res[:-5])

format_duration(3662)
format_duration(6034)
format_duration(95634444)

'''import re
def format_duration(seconds):
    if not seconds: return 'now'
    minutes = seconds / 60
    seconds %= 60
    hours = minutes / 60
    minutes %= 60
    days = hours / 24
    hours %= 24
    years = days / 365
    days %= 365
    a = []
    for n, l in zip([years, days, hours, minutes, seconds], ['year', 'day', 'hour', 'minute', 'second']):
        if n == 1:
            a.append('%d %s' % (n, l))
        elif n > 1:
            a.append('%d %ss' % (n, l))
    return re.sub(r', ([^,]*)$', lambda o: ' and ' + o.group(1), ', '.join(a))'''
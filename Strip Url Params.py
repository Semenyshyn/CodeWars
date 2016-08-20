'''stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'''


def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url
    o = url.index('?')
    params_list = str.split(url[o+1:], '&')
    params_list1 = []
    for i in params_list:
        params_list1.append(i[:2])
    params_set = set(params_list1)
    l = url
    for a in params_set:
        n = url.count(a[:2])
        while n > 1:
            k = l.rindex(a[:2])
            l = l[:k - 1] + l[k + 3:]
            n -= 1
    if params_to_strip:
        for i in params_set:
            if i[:1] in params_to_strip:
                k = l.index(i[:2])
                l = l[:k - 1] + l[k + 3:]
    return l

a = 'www.codewars.com?a=1&b=2&a=2'

print(strip_url_params(a, ['a']))

'''def strip_url_params(url, params_to_strip=[]):
    if '?' not in url: return url
    domain, params = url.split('?')
    params = [param.split('=') for param in params.split('&')]
    keys = [k[0] for k in params]
    new_params = []
    for key, _ in params:
        if key not in params_to_strip and key not in dict(new_params).keys():
            new_params.append(params[keys.index(key)])
    return domain + '?' + "&".join("=".join(x) for x in new_params)'''
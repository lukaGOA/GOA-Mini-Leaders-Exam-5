def expanded_form(num):
    res = []
    for i, digit in enumerate(str(num)):
        if digit != '0':
            res.append(digit + '0' * (len(str(num)) - i - 1))
    return ' + '.join(res)
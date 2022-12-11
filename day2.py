import pandas as pd

data = pd.read_csv('input.txt', sep=' ', names=['them', 'result'])


def score(them, result):
    if result == 'X':
        s = 0
        if them == 'A':
            me = 'C'
        if them == 'B':
            me = 'A'
        if them == 'C':
            me = 'B'
    if result == 'Y':
        s = 3
        me = them
    if result == 'Z':
        s = 6
        if them == 'A':
            me = 'B'
        if them == 'B':
            me = 'C'
        if them == 'C':
            me = 'A'

    if me == 'A':
        s += 1
    if me == 'B':
        s += 2
    if me == 'C':
        s += 3
    return s


data['score'] = data.apply(lambda x: score(x.them, x.result), axis = 1)
print(data)
print(sum(data['score']))


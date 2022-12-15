from functools import cmp_to_key
from more_itertools import flatten

with open("day13.txt") as f:
    pairs = [[eval(item) for item in x.split()] for x in f.read().split("\n\n")]

def is_correct_order(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    if type(left) == list and type(right) == list:
        if len(left) == 0 and len(right) == 0: return 0
        if len(left) == 0:                 return -1
        if len(right) == 0:                 return 1
        comp = is_correct_order(left[0], right[0])
        return comp if comp != 0 else is_correct_order(left[1:], right[1:])
    return is_correct_order([left], right) if type(left) == int else is_correct_order(left, [right])

print(sum(i for i, (left, right) in enumerate(pairs, start=1) if is_correct_order(left, right) < 0))

pairs = list(flatten(pairs))
pairs.extend([[[2]],[[6]]])

pairs_sorted = sorted(pairs, key=cmp_to_key(is_correct_order))
i1, i2 = pairs_sorted.index([[2]])+1, pairs_sorted.index([[6]])+1
print(i1*i2)

from itertools import groupby

with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

data = [list(group) for key, group in groupby(lines, key=lambda x: x == '') if not key]

totals = []
for person in data:
    food = [int(i) for i in person]
    total = sum(food)
    totals.append(total)

totals.sort(reverse=True)
best3 = totals[:3]
print(best3)
print(sum(best3))

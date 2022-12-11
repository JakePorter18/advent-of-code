import pandas as pd

data = pd.read_csv('inputitems.txt', names=['input'])
UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWER = [str.lower(char) for char in UPPER]
data['rownumber'] = data.index

def get_priority_of_letter(letter):
    if letter in UPPER:
        return UPPER.index(letter) + 27
    elif letter in LOWER:
        return LOWER.index(letter) + 1


def split_to_compartments(input_string):
    compartment_size = len(input_string) // 2
    return input_string[:compartment_size], input_string[compartment_size:]


data['c1'] = data.apply(lambda x: split_to_compartments(x.input)[0], axis=1)
data['c2'] = data.apply(lambda x: split_to_compartments(x.input)[1], axis=1)


def in_both(lst1, lst2):
    return [value for value in lst1 if value in lst2][0]


data['shared'] = data.apply(lambda x: in_both(x.c1, x.c2), axis=1)

data['priority'] = data.apply(lambda x: get_priority_of_letter(x.shared), axis=1)

data['group'] = data.index // 3
data['t'] = data.index % 3
groups = data[['t', 'group', 'input']].pivot(index='group', columns='t', values='input')


groups['licenses'] = groups.apply(lambda x: set(x[0]).intersection(x[2], x[1]), axis=1)
groups['priority'] = groups.apply(lambda x: get_priority_of_letter(list(x.licenses)[0]), axis=1)
print(sum(groups['priority']))

import re

input = ''

with open('../inputs/day13.txt', 'r') as f:
    input = f.read()

numbers = [int(x) for x in re.findall(r'\d+', input)]


def combinations(a, b, s):
    res = []
    for i in range(100):
        left = i * a
        if left > s:
            continue
        if (s - left) % b == 0:
            j = (s - left) // b
            res += [(i, j)]
    return res

credits = 0

for i in range(0, len(numbers), 6):
    ax, ay, bx, by, px, py = numbers[i:i+6]
    acs = set(combinations(ax, bx, px))
    bcs = set(combinations(ay, by, py))
    possibilities = acs & bcs
    print(possibilities)
    if len(possibilities) > 1:
        raise Exception('Multiple possibilities')
    elif len(possibilities) == 1:
        p = list(possibilities)[0]
        credits += 3 * p[0] + p[1]

print(credits)
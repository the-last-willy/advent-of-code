import json

input = ''

with open('../inputs/day11.txt') as f:
    input = f.read()

input = [int(x) for x in input.split(' ')]


def flat(arr):
    return [e for l in arr for e in l]


def apply(x):
    if x == '*':
        return []
    if x == 0:
        return [1]
    xstr = str(x)
    xlen = len(xstr)
    if xlen % 2 == 0:
        return [int(xstr[:xlen//2]), int(xstr[xlen//2:])]
    return [x * 2024]


def apply_n(x, n):
    arr = [x]
    for i in range(n):
        arr = flat([apply(x) for x in arr])
    return arr

total = 0

for x in input:
    total += len(apply_n(x, 25))

print(total)

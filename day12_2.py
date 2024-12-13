import copy
import json

input = ''

with open('inputs/day12.txt') as f:
    input = f.read().splitlines()

input = ['.' + row + '.' for row in input]
input = ['.' * len(input[0])] + input + ['.' * len(input[0])]

indexes = [[1 if c == '.' else 0 for c in row] for row in input]


def coords(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            yield i, j


def neighbors4(i, j):
    yield i + 0, j + 1  # right
    yield i - 1, j + 0  # top
    yield i + 0, j - 1  # left
    yield i + 1, j + 0  # bottom


idx = 2

# Region

for si, sj in coords(input):
    plant = input[si][sj]
    candidates = [(si, sj)]
    while len(candidates) > 0:
        ci, cj = candidates.pop()
        if indexes[ci][cj] != 0:
            continue
        if input[ci][cj] == plant:
            indexes[ci][cj] = idx
            candidates += neighbors4(ci, cj)
    idx += 1

regions = {}

for i, j in coords(input):
    regions.setdefault(indexes[i][j], [input[i][j], 0, 0])

# Area

for i, j in coords(input):
    regions[indexes[i][j]][1] += 1

# Perimeter

input2 = copy.deepcopy(input)

input2 = [[x.lower() for x in row] for row in input2]

for i in range(len(input) - 1):
    for j in range(len(input[i]) - 1):
        list = [indexes[i][j], indexes[i + 1][j], indexes[i][j + 1], indexes[i + 1][j + 1]]
        count = {}
        for x in list:
            count.setdefault(x, 0)
            count[x] += 1
        for k, v in count.items():
            if v in [1, 3]:
                regions[k][2] += 1
            elif v == 2:
                if indexes[i][j] == indexes[i + 1][j + 1] or indexes[i][j + 1] == indexes[i + 1][j]:
                    regions[k][2] += 2

for row in input2:
    for x in row:
        print(x, end='')
    print()
print()

# Total cost

del regions[1]

for r in regions.items():
    print(r)

total = 0

for r in regions.values():
    if r[0] != 1:
        total += r[1] * r[2]

print(total)

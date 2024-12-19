import copy

input = ''


def coords(input):
    for ri in range(len(input)):
        for ci in range(len(input[0])):
            yield ri, ci


def coords_with_val(input, val):
    for ri, ci in coords(input):
        if input[ri][ci] == val:
            yield ri, ci


def neighs(i, j):
    for cs in [
        (i - 1, j - 0),
        (i + 1, j + 0),
        (i - 0, j - 1),
        (i + 0, j + 1)
    ]:
        yield cs

def count9s(input):
    return sum(sum([1 for x in line if x == '9']) for line in input)


def has_neigh(input, i, j, nval):
    for ni, nj in neighs(i, j):
        if input[ni][nj] == nval:
            return True
    return False





with open('../inputs/day10.txt') as f:
    input = f.read()

input = [['.'] + [c for c in line] + ['.'] for line in input.split('\n')]
input = [['.'] * len(input[0])] + input + [['.'] * len(input[0])]

for line in input:
    print(line)
print()

zeros = []

for ri, row in enumerate(input):
    for ci, d in enumerate(row):
        if input[ri][ci] == str(0):
            zeros += [(ri, ci)]
            input[ri][ci] = '.'

for line in input:
    print(line)
print()

sum9 = 0

for zx, zy in zeros:
    grid = copy.deepcopy(input)
    grid[zx][zy] = '0'
    for i in range(1, 10):
        for ri, ci in coords_with_val(grid, str(i)):
            if not has_neigh(grid, ri, ci, str(i - 1)):
                grid[ri][ci] = '.'
    sum9 += count9s(grid)

# input = [line[1:len(line)-1] for line in input[1:len(input)-1]]
#
# for line in input:
#     print(line)
# print()

print(sum9)

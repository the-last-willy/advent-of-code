import copy


def neighs(i, j):
    for cs in [
        (i - 1, j - 0),
        (i + 1, j + 0),
        (i - 0, j - 1),
        (i + 0, j + 1)
    ]:
        yield cs


def search(grid, path):
    paths = []

    lx, ly = path[len(path) - 1]

    lv = grid[lx][ly]

    if lv == '9':
        return [path]

    for nx, ny in neighs(lx, ly):
        if grid[nx][ny] == str(int(lv) + 1):
            paths += search(grid, path + [(nx, ny)])

    return paths


input = ''

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

c = 0

for z in zeros:
    paths = search(input, [z])
    for p in paths:
        print(p)
        c += 1

print(c)

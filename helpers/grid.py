from copy import deepcopy


def coords(s1, s2):
    for a in range(s1):
        for b in range(s2):
            yield a, b


def size(grid):
    return len(grid), len(grid[0])


def find(grid, pred):
    for a, b in coords(*size(grid)):
        if pred(grid[a][b]):
            return a, b
    return None


def mapp(grid, fn):
    return [[fn(x) for x in row] for row in grid]


def printt(grid):
    for row in grid:
        for x in row:
            print(x, end='')
        print()
    print()


def neighbors4(yx):
    y, x = yx
    return [
        (y - 1, x + 0),
        (y + 0, x - 1),
        (y + 0, x + 1),
        (y + 1, x + 0)
    ]


def at(grid, yx):
    y, x = yx
    return grid[y][x]


def copy(g):
    return deepcopy(g)


def count(g, pred):
    return sum(sum(1 for x in row if pred(x)) for row in g)


def make(height, width, fill):
    return [[fill for x in range(width)] for y in range(height)]


def pad(g, fill):
    g = [[fill] + row + [fill] for row in g]
    rowlen = len(g[0])
    return [[fill] * rowlen] + g + [[fill] * rowlen]


def set(g, yx, val):
    y, x = yx
    g[y][x] = val

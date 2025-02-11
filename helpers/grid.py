import builtins
from copy import deepcopy

import helpers.vec2 as vec2


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


def make(size, fill):
    h, w = size
    return [[fill for i in range(w)] for j in range(h)]


def pad(g, fill):
    g = [[fill] + row + [fill] for row in g]
    rowlen = len(g[0])
    return [[fill] * rowlen] + g + [[fill] * rowlen]


def set(g, yx, val):
    y, x = yx
    g[y][x] = val


def dijkstra(*, start, end, candidates_fn):
    candidates = [[start]]
    visited = builtins.set()

    while len(candidates) > 0:
        path = candidates.pop(0)
        pos = path[len(path) - 1]

        if pos in visited:
            continue
        visited.add(pos)

        if vec2.eq(pos, end):
            return path

        candidates += candidates_fn(path)


def column(g, col):
    return [g[i][col] for i in range(len(g))]


def find_val(g, x):
    s1, s2 = size(g)
    for i in range(s1):
        for j in range(s2):
            if g[i][j] == x:
                return i, j
    return None

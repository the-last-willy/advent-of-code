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


def neighbors4(a, b):
    return [
        (a - 1, b + 0),
        (a + 0, b - 1),
        (a + 0, b + 1),
        (a + 1, b + 0)
    ]


def at(grid, ab):
    a, b = ab
    return grid[a][b]


def copy(g):
    return deepcopy(g)


def count(g, pred):
    return sum(sum(1 for x in row if pred(x)) for row in g)

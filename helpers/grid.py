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

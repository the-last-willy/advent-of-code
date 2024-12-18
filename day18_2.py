import re

import helpers.grid as g
import helpers.vec2 as v

input = []

with open('inputs/day18.txt') as f:
    for line in f.read().splitlines():
        match = re.match(r'(\d+),(\d+)', line)
        input += [(int(match.group(1)), int(match.group(2)))]

grid = g.make(71, 71, ' ')
grid = g.pad(grid, '#')

s = (1, 1)
e = (71, 71)

for x, y in input[:1024]:
    g.set(grid, (y + 1, x + 1), '#')

for x, y in input[1024:]:
    print(x, y)
    g.set(grid, (y + 1, x + 1), '#')

    # (pos, cost, path)
    candidates = [(s, 0, [])]
    visited = set()
    best = None

    # g.printt(grid)

    while len(candidates) > 0:
        pos, cost, path = candidates.pop(0)

        if pos in visited:
            continue
        visited.add(pos)

        if v.eq(pos, e):
            best = path + [pos]
            break

        for n in g.neighbors4(pos):
            if g.at(grid, n) != '#':
                candidates.append([n, cost + 1, path + [pos]])

        candidates = sorted(candidates, key=lambda c: c[1])

    if best is None:
        break

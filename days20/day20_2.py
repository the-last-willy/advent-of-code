import json

import helpers.grid as g
import helpers.input as i
import helpers.vec2 as v

input = i.parse_grid(i.read_file('../examples/day20.txt'))

sy, sx = g.size(input)
for yx in v.range2((1, sy - 1), (1, sx - 1)):
    if g.at(input, yx) == '#':
        g.set(input, yx, '+')

g.printt(input)

s = g.find(input, lambda x: x == 'S')
e = g.find(input, lambda x: x == 'E')


def neighbors_for(grid):
    def f(path):
        ns = []
        for n in g.neighbors4(path[len(path) - 1]):
            if not g.at(grid, n) in ['#', '+']:
                ns += [path + [n]]
        return ns

    return f


legit_path = g.dijkstra(start=s, end=e, candidates_fn=neighbors_for(input))

shortcuts = []

for mid in legit_path:
    candidates = [(1, n) for n in g.neighbors4(mid) if g.at(input, n) == '+']
    visited = set()

    while len(candidates) > 0:
        cheats, pos = candidates.pop(0)

        if pos in visited:
            continue
        visited.add(pos)

        if v.eq(pos, e):
            shortcuts.append(())

        for n in g.neighbors4(pos):
            if g.at(input, n) == '.':
                candidates.append((cheats + 1, n))
            elif cheats <= 2 and g.at(input, n) == '+':
                candidates.append((cheats + 1, n))


# (cheats, pos)
candidates = [(0, s)]
visited = set()

while len(candidates) > 0:
    cheats, pos = candidates.pop(0)

    if pos in visited:
        continue
    visited.add((cheats, pos))

    for n in g.neighbors4(pos):
        if g.at(input, n) == '.':
            pass

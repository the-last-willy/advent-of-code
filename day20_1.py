import json

import helpers.grid as g
import helpers.input as i
import helpers.vec2 as v

input = i.parse_grid(i.read_file('inputs/day20.txt'))

g.printt(input)

s = g.find(input, lambda x: x == 'S')
e = g.find(input, lambda x: x == 'E')

print(s, e)


def neighbors_for(grid):
    def f(path):
        ns = []
        for n in g.neighbors4(path[len(path) - 1]):
            if g.at(grid, n) != '#':
                ns += [path + [n]]
        return ns
    return f


legit_path = g.dijkstra(start=s, end=e, candidates_fn=neighbors_for(input))

shortcuts = []

sz, sx = g.size(input)
for y, x in v.range2((1, sz - 1), (1, sx - 1)):
    if g.at(input, (y, x)) == '#':
        left = y + 0, x - 1
        up = y - 1, x + 0
        bot = y + 1, x + 0
        right = y + 0, x + 1
        if g.at(input, left) != '#' and g.at(input, right) != '#':
            shortcuts.append((left, right))
        elif g.at(input, bot) != '#' and g.at(input, up) != '#':
            shortcuts.append((bot, up))

values = g.copy(input)

for i, p in enumerate(legit_path):
    g.set(values, p, i)

gains = {}

count = 0

for fr, to in shortcuts:
    diff = abs(g.at(values, to) - g.at(values, fr)) - 2

    if diff >= 100:
        count += 1

    gains.setdefault(diff, 0)
    gains[diff] += 1

print(count)

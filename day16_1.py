import helpers.grid as g
import helpers.vec2 as v

input = ''

with open('examples/day16.txt') as f:
    input = f.read().splitlines()

input = [[x for x in row] for row in input]

g.printt(input)

s = g.find(input, lambda x: x == 'S')
e = g.find(input, lambda x: x == 'E')

print(e)

# [(coords, dir, cost)]
candidates = [(s, (0, 1), 0)]
visited = set()

def candidates_for(pos, dir, cost):
    left = +dir[1], -dir[0]
    right = -dir[1], +dir[0]
    return [
        (v.sum(pos, dir), dir, cost + 1),
        (v.sum(pos, left), left, cost + 1001),
        (v.sum(pos, right), right, cost + 1001),
    ]

while len(candidates) > 0:
    c = candidates.pop(0)

    if v.eq(c[0], e):
        print(c)

    if c[0] in visited:
        continue
    visited.add(c[0])

    new_candidates = candidates_for(*c)
    new_candidates = [c for c in new_candidates if g.at(input, c[0]) != '#']
    candidates += new_candidates
    candidates = sorted(candidates, key=lambda x: x[2])

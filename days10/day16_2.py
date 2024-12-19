import helpers.grid as g
import helpers.vec2 as v

input = ''

with open('../inputs/day16.txt') as f:
    input = f.read().splitlines()

input = [[x for x in row] for row in input]

g.printt(input)

s = g.find(input, lambda x: x == 'S')
e = g.find(input, lambda x: x == 'E')

# [(coords, dir, cost, path)]
candidates = [(s, (0, 1), 0, [])]
visited = {}


def candidates_for(pos, dir, cost, path):
    left = +dir[1], -dir[0]
    right = -dir[1], +dir[0]
    path = path + [pos]
    return [
        (v.sum(pos, dir), dir, cost + 1, path),
        (v.sum(pos, left), left, cost + 1001, path),
        (v.sum(pos, right), right, cost + 1001, path),
    ]

best_ones = []
progress = 0
max_cost = 1000000000

while len(candidates) > 0:
    c = candidates.pop(0)

    if c[2] > max_cost:
        continue

    if c[2] >= progress + 1000:
        print(c[2])
        progress = c[2]

    if v.eq(c[0], e):
        max_cost = c[2]
        best_ones.append(c)
        print(c)

    posdir = c[:2]

    if posdir in visited and c[2] > visited[posdir]:
        continue
    visited[posdir] = c[2]

    new_candidates = candidates_for(*c)
    new_candidates = [c for c in new_candidates if g.at(input, c[0]) != '#']
    candidates += new_candidates
    candidates = sorted(candidates, key=lambda x: x[2])


best_ones = sorted(best_ones, key=lambda x: x[2])
best_ones = [x for x in best_ones if x[2] == best_ones[0][2]]

for bo in best_ones:
    for y, x in bo[3]:
        input[y][x] = 'O'

g.printt(input)

print(g.count(input, lambda x: x == 'O') + 1)
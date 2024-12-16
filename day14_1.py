import re

input = ''

with open('inputs/day14.txt') as f:
    input = f.read()

input = re.findall(r'-?\d+', input)
input = [int(x) for x in input]
input = [input[i:i + 4] for i in range(0, len(input), 4)]


def pmod(x, d):
    return (x % d + d) % d


def cmp(a, b):
    return (a > b) - (a < b)


w, h = 101, 103

seconds = 100

grid = [[0] * w for _ in range(h)]

quadrants = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x, y, dx, dy in input:
    print(x, y, dx, dy)
    px = pmod(x + seconds * dx, w)
    py = pmod(y + seconds * dy, h)

    qi = cmp(px, w // 2) + 1
    qj = cmp(py, h // 2) + 1
    quadrants[qj][qi] += 1

    grid[py][px] += 1

for l in grid:
    print(''.join(map(str, l)))
print()

print(quadrants[0][0] * quadrants[0][2] * quadrants[2][0] * quadrants[2][2])

import json

input = ''

with open('../inputs/day08.txt') as f:
    input = f.read().split('\n')
    input = [[c for c in line] for line in input]

for line in input:
    for c in line:
        print(c, end='')
    print()
print()

antennas = {}

for ri, line in enumerate(input):
    for ci, c in enumerate(line):
        if c != '.':
            antennas.setdefault(c, []).append((ri, ci))

antinodes = set()

for type in antennas.values():
    for i in range(len(type)):
        for j in range(i + 1, len(type)):
            xi, yi = type[i]
            xj, yj = type[j]
            dx, dy = (xi - xj), (yi - yj)
            for k in range(200):
                antinodes.add((xi + k * dx, yi + k * dy))
                antinodes.add((xj - k * dx, yj - k * dy))

count = 0

for (x, y) in antinodes:
    if 0 <= x < len(input) and 0 <= y < len(input[x]):
        count += 1
        input[x][y] = '#'

for line in input:
    for c in line:
        print(c, end='')
    print()
print()

print(count)

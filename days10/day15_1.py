from typing import Tuple

import helpers.grid as g
import helpers.list

input = ''

with open('../inputs/day15.txt') as f:
    input = f.read().splitlines()

grid = input[:input.index('')]
grid = [[x for x in line] for line in grid]
commands = input[input.index('')+1:]
commands = helpers.list.flat(commands)

print(commands)

robot = g.find(grid, lambda x: x == '@')
print(robot)

dirs = {
    '<': (-0, -1),
    'v': (+1, -0),
    '^': (-1, -0),
    '>': (-0, +1),
}


def move(grid, pos, dir) -> Tuple[int, int]:
    dy, dx = dir
    py, px = pos
    mx, my = px + dx, py + dy
    if grid[my][mx] == '#':
        return None
    if grid[my][mx] == 'O' and move(grid, (my, mx), dir) is None:
        return None
    grid[my][mx], grid[py][px] = grid[py][px], '.'
    return my, mx


for cmd in commands:
    dir = dirs[cmd]
    print(cmd)
    new_robot = move(grid, robot, dir)
    if new_robot is not None:
        robot = new_robot

for l in grid:
    for x in l:
        print(x, end= '')
    print()
print()

score = 0

for y, x in g.coords(*g.size(grid)):
    if grid[y][x] == 'O':
        score += y * 100 + x

print(score)


from typing import Tuple

import helpers.grid as g
import helpers.list

input = ''

with open('inputs/day15.txt') as f:
    input = f.read().splitlines()


def part2(x):
    if x == '#':
        return ['X', 'X']
    if x == 'O':
        return ['[', ']']
    if x == '.':
        return ['.', '.']
    return ['@', '.']


grid = input[:input.index('')]
grid = [[x for x in line] for line in grid]
grid = g.mapp(grid, part2)
grid = [helpers.list.flat(row) for row in grid]

for l in grid:
    for x in l:
        print(x, end='')
    print()
print()

commands = input[input.index('') + 1:]
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


def can_move_into(grid, pos, dir):
    dy, dx = dir
    py, px = pos
    mx, my = px + dx, py + dy

    e = grid[py][px]

    if e == '.':
        return True
    if e == 'X':
        return False

    m = grid[my][mx]

    if not can_move_into(grid, (my, mx), dir):
        return False

    if m == '[' and dx != -1:
        return can_move_into(grid, (my, mx + 1), dir)
    if m == ']' and dx != +1:
        return can_move_into(grid, (my, mx - 1), dir)

    return True


def move(grid, pos, dir):
    dy, dx = dir
    py, px = pos
    mx, my = px + dx, py + dy
    e = grid[py][px]

    if e in ['.', 'X']:
        return None

    if grid[my][mx] == '[':
        move(grid, (my, mx + 1), dir)
    if grid[my][mx] == ']':
        move(grid, (my, mx - 1), dir)

    move(grid, (my, mx), dir)

    grid[my][mx], grid[py][px] = grid[py][px], '.'

    return my, mx


def try_move(grid, pos, dir):
    if can_move_into(grid, pos, dir):
        return move(grid, pos, dir)
    return None


for cmd in commands[:]:
    dir = dirs[cmd]
    new_robot = try_move(grid, robot, dir)
    if new_robot is not None:
        robot = new_robot

score = 0

for y, x in g.coords(*g.size(grid)):
    if grid[y][x] == '[':
        score += y * 100 + x

print(score)

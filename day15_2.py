from typing import Tuple

import helpers.grid as g
import helpers.list

input = ''

with open('examples/day15.txt') as f:
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


def can_move(grid, pos, dir):
    dy, dx = dir
    py, px = pos
    mx, my = px + dx, py + dy
    e = grid[my][mx]

    if e == '#':
        return False
    if e == '.':
        return True
    if e == '[':
        if dx == 1 and not can_move(grid, (my, mx + 1), dir):
            return False
        return can_move(grid, (my, mx), dir)
    if e == ']':
        if dx == -1 and not can_move(grid, (my, mx - 1), dir):
            return False
        return can_move(grid, (my, mx), dir)


def move(grid, pos, dir) -> Tuple[int, int]:
    dy, dx = dir
    py, px = pos
    mx, my = px + dx, py + dy
    e = grid[my][mx]

    if can_move(grid, pos, dir):
        if e == '[' and dx == 1:
            move(grid, (my, mx + 1), dir)
        elif e == ']' and dx == -1:
            move(grid, (my, mx - 1), dir)
        move(grid, (my, mx), dir)

        grid[my][mx], grid[py][px] = grid[py][px], '.'

        return my, mx

    return None



for cmd in commands:
    dir = dirs[cmd]
    # print(cmd)
    new_robot = move(grid, robot, dir)
    if new_robot is not None:
        robot = new_robot

    for l in grid:
        for x in l:
            print(x, end='')
        print()
    print()

score = 0

for y, x in g.coords(*g.size(grid)):
    if grid[y][x] == 'O':
        score += y * 100 + x

print(score)

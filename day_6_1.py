import json

from helpers import str_cut_insert

cursors = [
    {
        'symbol': '>',
        'dir': (0, +1),
    },
    {
        'symbol': 'v',
        'dir': (+1, 0),
    },
    {
        'symbol': '<',
        'dir': (0, -1),
    },
    {
        'symbol': '^',
        'dir': (-1, 0),
    },
]


def forward_dir(symbol):
    i = 0
    for i in range(len(cursors)):
        if cursors[i]['symbol'] == symbol:
            break
    return cursors[i]['dir']


def turn(symbol):
    i = 0
    for i in range(len(cursors)):
        if cursors[i]['symbol'] == symbol:
            break
    return cursors[(i + 1) % 4]


def find_cursor(map):
    for ri, row in enumerate(map):
        for ci, cell in enumerate(row):
            if cell in [c['symbol'] for c in cursors]:
                return ri, ci


def move_cursor(map):
    x, y = find_cursor(map)
    cursor = map[x][y]
    dirx, diry = forward_dir(cursor)
    nx, ny = x + dirx, y + diry
    if map[nx][ny] == '+':
        map[x][y] = 'X'
        return False
    if map[nx][ny] in ['.', 'X']:
        map[x][y] = 'X'
        map[nx][ny] = cursor
        return True
    if map[nx][ny] == '#':
        turned = turn(cursor)
        tdir = turned['dir']
        tx, ty = x + tdir[0], y + tdir[1]
        map[x][y] = 'X'
        map[tx][ty] = turned['symbol']
        return True


def pad_input(map):
    map = [['+'] + row + ['+'] for row in map]
    return ['+' * len(map[0])] + map + ['+' * len(map[0])]


def print_map(map):
    for row in map:
        for cell in row:
            print(cell, end='')
        print()
    print()


input = ""

with open("day_6_1_input.txt", "r") as f:
    input = f.read()

input = [[e for e in row] for row in input.split('\n')]
input = pad_input(input)

print_map(input)

while move_cursor(input):
    pass
    # print_map(input)

print(sum(sum([1 for x in row if x == 'X']) for row in input))

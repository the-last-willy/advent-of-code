import hashlib
import json

from helpers import cut_insert

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


def map_with_at(map, e, i, j):
    return cut_insert(map, i, [cut_insert(map[i], j, [e])])


def move_cursor(map):
    x, y = find_cursor(map)
    cursor = map[x][y]
    dirx, diry = forward_dir(cursor)
    nx, ny = x + dirx, y + diry
    map = map_with_at(map, 'X', x, y)
    if map[nx][ny] == '+':
        return map, False
    if map[nx][ny] in ['.', 'X']:
        map = map_with_at(map, cursor, nx, ny)
        return map, True
    if map[nx][ny] == '#':
        turned = turn(cursor)
        tdir = turned['dir']
        tx, ty = x + tdir[0], y + tdir[1]
        map = map_with_at(map, turned['symbol'], tx, ty)
        return map, True


def pad_input(map):
    map = [['+'] + row + ['+'] for row in map]
    return ['+' * len(map[0])] + map + ['+' * len(map[0])]


def print_map(map):
    for row in map:
        for cell in row:
            print(cell, end='')
        print()
    print()


def map_hash(map):
    return hashlib.sha256(json.dumps(map).encode('utf-8'))


def compute(map):
    while True:
        map, ok = move_cursor(map)
        if not ok:
            return map


def is_loop(map):
    all_maps = {}

    while True:
        map, ok = move_cursor(map)
        h = map_hash(map)
        print_map(map)
        all_maps[h] = True
        if h in all_maps:
            return True
        if not ok:
            return False



input = ""

with open("day_6_1_example.txt", "r") as f:
    input = f.read()

input = [[e for e in row] for row in input.split('\n')]
input = pad_input(input)

solution = compute(input)

xs = [(ri, ci) for ri in range(len(input)) for ci in range(len(input[ri])) if solution[ri][ci] == 'X']

i = 0

for x, y in xs:
    try:
        map = map_with_at(input, '#', x, y)
        if is_loop(map):
            i+= 1
            print_map(map)
    except:
        pass

print(i)

# print(sum(sum([1 for x in row if x == 'X']) for row in input))

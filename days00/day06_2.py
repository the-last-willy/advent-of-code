import copy

cursors = {
    '>': {
        'fw': lambda x, y: (x + 0, y + 1),
        'right': 'v'
    },
    'v': {
        'fw': lambda x, y: (x + 1, y + 0),
        'right': '<'
    },
    '<': {
        'fw': lambda x, y: (x + 0, y - 1),
        'right': '^'
    },
    '^': {
        'fw': lambda x, y: (x - 1, y + 0),
        'right': '>'
    },
}

input = ""

with open("../inputs/day06.txt", "r") as f:
    input = f.read()

input = [['+'] + [e for e in row] + ['+'] for row in input.split('\n')]

input = [['+'] * len(input[0])] + input + [['+'] * len(input[0])]


def find_cursor(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in cursors.keys():
                return i, j

def printinput(input):
    for line in input:
        for c in line:
            print(c, end='')
        print()
    print()



def move(grid, cursor):
    cx, cy = cursor
    sym = grid[cx][cy]
    fx, fy = cursors[sym]['fw'](cx, cy)

    while grid[fx][fy] == '#':
        sym = cursors[sym]['right']
        fx, fy = cursors[sym]['fw'](cx, cy)

    if grid[fx][fy] == sym:
        return None, True

    if grid[fx][fy] != '+':
        grid[fx][fy] = sym
        return (fx, fy), None

    return None, False


pos = find_cursor(input)

cnt = 0

for x in range(1, len(input) - 1):
    print(x)
    for y in range(1, len(input[x]) - 1):
        if input[x][y] != '.':
            continue

        input2 = copy.deepcopy(input)
        input2[x][y] = '#'
        pos2 = pos

        loop = False

        while pos2 is not None:
            pos2, loop = move(input2, pos2)

        # printinput(input2)

        if loop:
            cnt += 1

print(cnt)

import json


def clip_input(input):
    input = input[3:len(input) - 3]
    input = [row[3:len(row) - 3] for row in input]
    return input


def dirs():
    li = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    for x in li:
        yield x


input = ""

with open("examples/day04.txt", "r") as f:
    input = f.read()

input = input.split('\n')

print(json.dumps(input, indent=4))

input = ["..." + row + "..." for row in input]
input = ["." * len(input[0])] * 3 + input + ["." * len(input[0])] * 3

found = ["." * len(input[0])] * len(input)

count = 0

for i in range(3, len(input) - 3):
    for j in range(3, len(input[i]) - 3):
        for d in dirs():

            yes = True

            for k in range(4):
                x = i + d[0] * k
                y = j + d[1] * k
                if input[x][y] != 'XMAS'[k]:
                    yes = False
                    break

            if yes:
                count += 1
                for k in range(4):
                    x = i + d[0] * k
                    y = j + d[1] * k
                    found[x] = found[x][:y] + 'XMAS'[k] + found[x][y + 1:]

print(json.dumps((found), indent=4))
print(count)

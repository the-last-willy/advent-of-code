import json


patterns = [
    [
        "M.S",
        ".A.",
        "M.S",
    ],
    [
        "M.M",
        ".A.",
        "S.S",
    ],
    [
        "S.M",
        ".A.",
        "S.M",
    ],
    [
        "S.S",
        ".A.",
        "M.M",
    ]
]


def match(input, pattern, x, y, debug):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == '.':
                continue
            if pattern[i][j] != input[x + i][y + j]:
                return False

    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] != '.':
                debug[x + i] = debug[x + i][:y + j] + pattern[i][j] + debug[x + i][y + j + 1:]

    return True


input = ""

with open("day_4_1_input.txt", "r") as f:
    input = f.read()

input = input.split('\n')

debug = ["." * len(input[0])] * len(input)

count = 0

for i in range(len(input) - 2):
    for j in range(len(input[i]) - 2):
        for p in patterns:
            if match(input, p, i, j, debug):
                count += 1

print(json.dumps(input, indent=4))
print(json.dumps(debug, indent=4))
print(count)

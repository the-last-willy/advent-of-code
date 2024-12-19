input = ''

with open('inputs/day19.txt') as file:
    input = file.read().splitlines()

patterns = input[0].split(', ')
designs = input[2:]

print(patterns)
print(designs)

count = 0


def rec(patterns, design):
    for p in patterns:
        if design.startswith(p):
            if design == p or rec(patterns, design[len(p):]):
                return True
    return False

for d in designs:
    if rec(patterns, d):
        count += 1

print(count)

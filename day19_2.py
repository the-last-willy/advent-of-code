input = ''

with open('inputs/day19.txt') as file:
    input = file.read().splitlines()

patterns = input[0].split(', ')
designs = input[2:]

print(patterns)
print(designs)


cache = {}


def rec(patterns, design, depth=0):
    if design in cache:
        return cache[design]

    count = 0
    for p in patterns:
        if design.startswith(p):
            count += int(design == p) + rec(patterns, design[len(p):], depth + 1)
    cache[design] = count
    return count


count = 0

for i, d in enumerate(designs):
    print(f'{i+1}/{len(designs)}: {rec(patterns, d)}')
    count += rec(patterns, d)

print(len(cache))
print(count)

import re

input = ''

with open('../inputs/day13.txt', 'r') as f:
    input = f.read()

numbers = [int(x) for x in re.findall(r'\d+', input)]

credits = 0

for i in range(0, len(numbers), 6):
    ax, ay, bx, by, px, py = numbers[i:i+6]
    px += 10000000000000
    py += 10000000000000
    af = (by * px - bx * py) / (by * ax - bx * ay)
    bf = (py - ay * af) / by

    if af % 1 == 0 and bf % 1 == 0:
        credits += 3 * af + bf

print(credits)

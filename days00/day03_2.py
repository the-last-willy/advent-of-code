import re

input = ""

with open("../inputs/day03.txt", "r") as f:
    input = f.read()

enabled = True
sum = 0

for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input):
    print(match.group(0))
    if match.group(0) == 'do()':
        enabled = True
    elif match.group(0) == 'don\'t()':
        enabled = False
    elif enabled:
        sum += int(match.group(1)) * int(match.group(2))

print(sum)

import re

input = ""

with open("inputs/day03.txt", "r") as f:
    input = f.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", input)

sum = 0

for match in matches:
    sum += int(match[0]) * int(match[1])

print(sum)

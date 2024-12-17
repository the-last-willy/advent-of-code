import re

input = ""

with open("../inputs/day01.txt", "r") as f:
    input = f.read()

numbers = [int(num) for num in re.findall(r'\d+', input)]

first_list = [numbers[i] for i in range(0, len(numbers), 2)]
first_list.sort()
second_list = [numbers[i] for i in range(1, len(numbers), 2)]
second_list.sort()

sum = 0

for a, b in zip(first_list, second_list):
    sum += abs(a - b)

print(sum)

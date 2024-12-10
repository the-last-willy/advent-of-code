import json
import re

input = ""

with open("day_1_2_input.txt", "r") as f:
    input = f.read()

numbers = [int(num) for num in re.findall(r'\d+', input)]

first_list = [numbers[i] for i in range(0, len(numbers), 2)]
first_list.sort()
second_list = [numbers[i] for i in range(1, len(numbers), 2)]
second_list.sort()

second_counts = {}

for num in second_list:
    second_counts[num] = second_counts.get(num, 0) + 1

sum = 0

for num in first_list:
    sum += num * second_counts.get(num, 0)

print(sum)

def differences(list):
    return [list[i] - list[i+1] for i in range(0, len(list) - 1)]

def is_safe(level):
    diffs = differences(level)
    same_sign = all([d >= 0 for d in diffs]) or all([d <= 0 for d in diffs])
    ok_delta = all([abs(d) >= 1 and abs(d) <= 3 for d in diffs])
    return same_sign and ok_delta


input = ""

with open("../inputs/day02.txt", "r") as f:
    input = f.read()

levels = [[int(x) for x in l.split(' ')] for l in input.split('\n')]

count = 0

for level in levels:
    count += is_safe(level)

print(count)

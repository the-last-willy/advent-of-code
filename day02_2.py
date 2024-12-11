def differences(list):
    return [list[i] - list[i + 1] for i in range(0, len(list) - 1)]


def is_safe(level):
    diffs = differences(level)
    same_sign = all([d >= 0 for d in diffs]) or all([d <= 0 for d in diffs])
    ok_delta = all([1 <= abs(d) <= 3 for d in diffs])
    return same_sign and ok_delta


def without_ith(li, i):
    copy = list(li)
    del copy[i]
    return copy


def is_safe_one(level):
    if is_safe(level):
        return True
    for i in range(len(level)):
        if is_safe(without_ith(level, i)):
            return True
    return False


input = ""

with open("day_2_2_input.txt", "r") as f:
    input = f.read()

levels = [[int(x) for x in l.split(' ')] for l in input.split('\n')]

count = 0

for level in levels:
    count += is_safe_one(level)

print(count)

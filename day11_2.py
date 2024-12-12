import time

input = ''

with open('inputs/day11.txt') as f:
    input = f.read()

input = [int(x) for x in input.split(' ')]


def flat(arr):
    return [e for l in arr for e in l]


def apply(x):
    if x == 0:
        return [1]
    xstr = str(x)
    xlen = len(xstr)
    if xlen % 2 == 0:
        return [int(xstr[:xlen // 2]), int(xstr[xlen // 2:])]
    return [x * 2024]


def apply_n(x, n):
    arr = [x]
    for i in range(n):
        arr = flat([apply(x) for x in arr])
    return arr


cache = {}


def count_n(x, n, step):
    if n < step:
        return len(apply_n(x, n))
    if (n, x) in cache:
        return cache[(n, x)]
    cnt = sum([count_n(y, n - step, step) for y in apply_n(x, step)])
    cache[(n, x)] = cnt
    return cnt


tot = 0

start_time = time.time()

for x in input:
    tot += count_n(x, 75, 3)

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")

print(tot)

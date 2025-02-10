import helpers.grid as gr
import helpers.input as i

file = i.read_file('../inputs/day25.txt')

patterns = file.split('\n\n')

keys = []
locks = []

for l in patterns:
    g = i.parse_grid(l)
    code = [sum([1 for x in gr.column(g, i) if x == '#']) - 1 for i in range(5)]
    if g[0][0] == '#':
        locks.append(code)
    else:
        keys.append(code)

print(keys)
print(locks)

count = 0

for k in keys:
    for l in locks:
        s = [lv + kv for lv, kv in zip(l, k)]
        if all([x <= 5 for x in s]):
            count += 1

print(count)

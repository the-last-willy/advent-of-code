import helpers.input as i

input = i.read_file('../inputs/day23.txt')
input = [x.split('-') for x in input.splitlines()]


connections = {}

for a, b in input:
    connections.setdefault(a, [])
    connections[a] += [b]
    connections.setdefault(b, [])
    connections[b] += [a]

for item in sorted(connections.items()):
    print(item)
print()

interconnections = set()

for a, bs in connections.items():
    for b in bs:
        for c in connections[b]:
            if a in connections[c]:
                interconnections.add(tuple(sorted((a, b, c))))

for item in sorted(interconnections):
    print(item)
print()

count = 0

for inter in interconnections:
    if any([x[0] == 't' in x for x in inter]):
        count += 1

print(count)

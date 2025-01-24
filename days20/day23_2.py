import helpers.input as i

input = i.read_file('../inputs/day23.txt')
input = [sorted(x.split('-')) for x in input.splitlines()]
input = sorted(input)

connections = {}

for a, b in input:
    connections.setdefault(a, [])
    connections[a] += [b]
    connections.setdefault(b, [])
    connections[b] += [a]


def are_interconnected(points):
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            if p1 not in connections[p2]:
                return False
    return True


def interconnections(points, k=0):
    if are_interconnected(points):
        return [points]
    res = []
    for i in reversed(range(k, len(points))):
        copy = list(points)
        copy.pop(i)
        res += interconnections(copy, k+1)
    return res

iter = 1

all_of_them = []
for k, v in connections.items():
    print(iter, '/', len(connections))
    iter += 1

    points = [k] + [x for x in v if x > k]
    # print(points)
    # print(interconnections(points))
    all_of_them += interconnections(points)
    # print()

all_of_them.sort(key=lambda x: len(x), reverse=True)

print(','.join(all_of_them[0]))

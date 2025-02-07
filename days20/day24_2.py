import helpers.input as i
import helpers.list as l
import json
import re

inn = i.read_file('../inputs/day24.txt').splitlines()

connections = []

for x in inn:
    assign = re.match(r'^(.*) (.*) (.*) -> (.*)$', x)
    if assign is not None:
        left, op, right, dst = assign.groups()
        left, right = sorted([left, right])
        print(left, op, right, dst)
        connections += [[left, op, right, dst]]

swaps = {
    'cnk': 'qwf',
    'qwf': 'cnk',

    'z14': 'vhm',
    'vhm': 'z14',

    'z27': 'mps',
    'mps': 'z27',

    'z39': 'msq',
    'msq': 'z39',
}

for c in connections:
    if c[3] in swaps:
        c[3] = swaps[c[3]]



mappings = {}

def map(c):
    left, op, right, dst = c
    left = mappings.get(left, left)
    right = mappings.get(right, right)
    dst = mappings.get(dst, dst)
    left, right = sorted([left, right])
    return [left, op, right, dst]

for c in connections:
    left, op, right, dst = c
    if left.startswith('x') and right.startswith('y') and not dst.startswith('z'):
        if op == 'AND':
            mappings[dst] = f'a{left[1:]}'
        elif op == 'XOR':
            mappings[dst] = f'e{left[1:]}'

connections = [map(c) for c in connections]

for c in connections:
    left, op, right, dst = c
    if op == 'OR':
        mappings[dst] = f'c{left[1:]}'

mappings['a00'] = 'c00'

connections = [map(c) for c in connections]

for c in connections:
    left, op, right, dst = c
    if left.startswith('c') and op == "AND" and right.startswith('e'):
        mappings[dst] = 't' + right[1:]

connections = [map(c) for c in connections]


reverse_mapping = {v: k for k, v in mappings.items()}

def encode(name, value):
    d = {}
    for i in range(46):
        d[name + str(i).rjust(2, "0")] = (value >> i) % 2
    return d


def decode(name, di):
    digits = [(k, v) for k, v in di.items() if k[0] == name]
    digits = [value for var, value in sorted(digits)]
    value = sum([1 << i for i, x in enumerate(digits) if x == 1])
    return value


def combine(lv, op, rv):
    if op == 'AND':
        return lv & rv
    if op == 'OR':
        return lv | rv
    if op == 'XOR':
        return lv ^ rv
    raise NotImplemented()


def compute(x, y):
    wires = {**encode('x', x), **encode('y', y)}

    connecs = list(connections)

    while len(connecs) > 0:
        left, op, right, dst = c = connecs.pop(0)
        if left not in wires or right not in wires:
            connecs += [c]
            continue
        wires[dst] = combine(wires[left], op, wires[right])

    return decode('z', wires)


connections_copy = list(sorted(connections))

for i in range(45):
    id = str(i).rjust(2, '0')
    candidates = ['z' + id, 'c' + id]
    cos = []
    while len(candidates) > 0:
        candidate = candidates.pop(0)
        for c in connections_copy:
            left, op, right, dst = c
            if dst == candidate:
                cos += [c]
                candidates += [left, right]
    connections_copy = [c for c in connections_copy if not c in cos]
    print(f'{i}:')
    ops = {}
    for c in cos:
        left, op, right, dst = c
        ops.setdefault(op, 0)
        ops[op] += 1
        print(f'  {left}({reverse_mapping.get(left, "---")}) {op} {right}({reverse_mapping.get(right, "---")}) -> {dst}({reverse_mapping.get(dst, "---")})')

print('rest:')
for c in connections_copy:
    left, op, right, dst = c
    print(
        f'  {left}({reverse_mapping.get(left, "---")}) {op} {right}({reverse_mapping.get(right, "---")}) -> {dst}({reverse_mapping.get(dst, "---")})')

swaps = sorted(swaps.values())
print(",".join(swaps))

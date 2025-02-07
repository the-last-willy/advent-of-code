import helpers.input as i
import json
import re

inn = i.read_file('../inputs/day24.txt').splitlines()

wires = {}
connections = []

for x in inn:
    wire_match = re.match(r'^(.*): (.*)$', x)
    if wire_match is not None:
        var, value = wire_match.groups()
        wires[var] = int(value)

    assign = re.match(r'^(.*) (.*) (.*) -> (.*)$', x)
    if assign is not None:
        left, op, right, dst = assign.groups()
        connections += [[left, op, right, dst]]

print(json.dumps(wires, indent=4))

def combine(left, op, right):
    lv = wires[left]
    rv = wires[right]
    if op == 'AND':
        return lv & rv
    if op == 'OR':
        return lv | rv
    if op == 'XOR':
        return lv ^ rv
    raise NotImplemented()


while len(connections) > 0:
    left, op, right, dst = connections.pop(0)
    if left not in wires or right not in wires:
        connections += [[left, op, right, dst]]
        continue
    wires[dst] = combine(left, op, right)

print(json.dumps(wires, indent=4))

zs = {w: val for w, val in wires.items() if w[0] == 'z'}
zs = sorted(zs.items())

num = 0

for i, x in enumerate([z[1] for z in zs]):
    num += x << i

print(num)

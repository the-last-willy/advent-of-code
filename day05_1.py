import json


def is_rule_followed(update, rule):
    for i in range(len(update) - 1):
        if update[i] != rule[1]:
            continue
        for j in range(i + 1, len(update)):
            if update[j] == rule[0]:
                return False
    return True


input = ""

with open("inputs/day05.txt", "r") as f:
    input = f.read()

[rules, updates] = input.split('\n\n')

rules = [r.split('|') for r in rules.split('\n')]
updates = [u.split(',') for u in updates.split('\n')]

ok_udpdates = []

for u in updates:
    ok = True

    for r in rules:
        if not is_rule_followed(u, r):
            ok = False
            break

    if ok:
        ok_udpdates.append(u)

middles = [int(u[(len(u)) // 2]) for u in ok_udpdates]
print(sum(middles))

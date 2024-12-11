import json


def is_rule_followed(update, rule):
    for i in range(len(update) - 1):
        if update[i] != rule[1]:
            continue
        for j in range(i + 1, len(update)):
            if update[j] == rule[0]:
                return False
    return True


def are_rules_followed(update, rules):
    for rule in rules:
        if not is_rule_followed(update, rule):
            return False
    return True


def apply_rule(update, rule):
    for i in range(len(update) - 1):
        if update[i] != rule[1]:
            continue
        for j in range(i + 1, len(update)):
            if update[j] == rule[0]:
                update[i], update[j] = update[j], update[i]
                return True
    return False


def apply_rules(update, rules):
    while True:
        any_applied = False
        for r in rules:
            any_applied = any_applied or apply_rule(update, r)
        if not any_applied:
            return update


input = ""

with open("inputs/day05.txt", "r") as f:
    input = f.read()

[rules, updates] = input.split('\n\n')

rules = [r.split('|') for r in rules.split('\n')]
updates = [u.split(',') for u in updates.split('\n')]

updates = [apply_rules(u, rules) for u in updates if not are_rules_followed(u, rules)]

middles = [int(u[(len(u)) // 2]) for u in updates]
print(sum(middles))

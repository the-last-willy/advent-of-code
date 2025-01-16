import json

import helpers.input as i
import helpers.list as l


def mix(x, y):
    return x ^ y


def prune(x):
    return x % 16777216


def evolve(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


secrets = i.read_file('../inputs/day22.txt')
secrets = [int(x) for x in secrets.splitlines()]

big_dic = {}

for si, secret in enumerate(secrets):
    print(f"{si+1}/{len(secrets)}")

    dic = {}

    seq = [secret % 10]
    diffs = []

    for i in range(2000):
        secret = evolve(secret)
        seq += [secret % 10]

    for s in l.slide(seq, 1):
        if len(s) < 2:
            break
        diffs += [s[1] - s[0]]

    for i, d in enumerate(l.slide(diffs, 1)):
        if len(d) < 4:
            break
        dic.setdefault(tuple(d[:4]), seq[i+4])

    for k, v in dic.items():
        if k not in big_dic:
            big_dic[k] = v
        else:
            big_dic[k] += v

print(max(big_dic.values()))

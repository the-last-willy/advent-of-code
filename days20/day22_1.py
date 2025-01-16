import helpers.input as i


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


sum = 0

for secret in secrets:
    for i in range(2000):
        secret = evolve(secret)
    sum += secret

print(sum)

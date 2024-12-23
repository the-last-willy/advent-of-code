def sign(x):
    return int(x > 0) - int(x < 0)


def count(iter):
    counts = {}

    for x in iter:
        counts.setdefault(x, 0)
        counts[x] += 1

    return counts

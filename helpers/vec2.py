def sum(a, b):
    return a[0] + b[0], a[1] + b[1]


def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]


def range2(r1, r2):
    for x1 in range(*r1):
        for x2 in range(*r2):
            yield x1, x2

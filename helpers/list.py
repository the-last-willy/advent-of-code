def flat(l):
    return [x for sl in l for x in sl]


def slide(l, offset):
    cnt = (len(l) + offset - 1) // offset
    for i in range(cnt):
        yield l[i * offset:]

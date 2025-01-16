import json

import helpers.input as i
import helpers.num as n
import helpers.vec2 as v

input = i.read_file('../examples/day21.txt').splitlines()


def sym_to_pos(kpd, s):
    for si, pi in kpd:
        if si == s:
            return pi
    raise NotImplementedError(f'{s} not in {[x[0] for x in kpd]}')


def pos_to_sym(kpd, p):
    for si, pi in kpd:
        if v.eq(pi, p):
            return si
    raise NotImplementedError(f'{p} not in {[x[1] for x in kpd]}')


def diff2seq_num(d):
    vs = 'v' if d[0] > 0 else '^'
    hs = '>' if d[1] > 0 else '<'
    return abs(d[1]) * hs + abs(d[0]) * vs


dirs = {
    '^': (-1, +0),
    '<': (-0, -1),
    'v': (+1, +0),
    '>': (+0, +1),
}

dir_to_sym = {
    (-1, +0): '^',
    (-0, -1): '<',
    (+1, +0): 'v',
    (+0, +1): '>',
    (+0, +0): '',
}

dkbd = [
    ('^', (0, 1)),
    ('<', (1, 0)),
    ('v', (1, 1)),
    ('>', (1, 2)),
    ('A', (0, 2)),
]

dkbd_deadkey = (0, 0)

nkbd = [
    ('0', (3, 1)),
    ('1', (2, 0)),
    ('2', (2, 1)),
    ('3', (2, 2)),
    ('4', (1, 0)),
    ('5', (1, 1)),
    ('6', (1, 2)),
    ('7', (0, 0)),
    ('8', (0, 1)),
    ('9', (0, 2)),
    ('A', (3, 2)),
]

paths = {

}

nkbd_deadkey = (3, 0)

paths = {
    (0, 0): '',

    (0, 1): '>A',
    (1, 0): 'vA',
    (0, -1): '<A',
    (-1, 0): '^A',
}


def diff_to_seq(diff):
    dy, dx = diff
    exceptions = {
        (-2, -2): '<<^^A'
    }
    if diff in exceptions:
        return exceptions[diff]
    seq = abs(dy) * dir_to_sym[(n.sign(dy), 0)] + abs(dx) * dir_to_sym[(0, n.sign(dx))] + 'A'
    # print(diff, seq)
    return seq


debug = None


def encode(kbd, input):
    global debug
    output = ''
    pos = sym_to_pos(kbd, 'A')
    for sym in input:
        dest = sym_to_pos(kbd, sym)
        diff = v.diff(dest, pos)
        output += diff_to_seq(diff)
        pos = dest
    # assert (v.eq(pos, sym_to_pos(kbd, 'A')))
    return output


def decode(kbd, input):
    output = ''
    pos = sym_to_pos(kbd, 'A')
    for sym in input:
        if sym == 'A':
            output += pos_to_sym(kbd, pos)
        else:
            pos = v.sum(pos, dirs[sym])
    return output


def special_encode(seq3):
    seq2 = encode(nkbd, seq3)
    seq1 = encode(dkbd, seq2)
    seq0 = encode(dkbd, seq1)
    return [seq0, seq1, seq2, seq3]


def special_decode(seq0):
    seq1 = decode(dkbd, seq0)
    seq2 = decode(dkbd, seq1)
    seq3 = decode(nkbd, seq2)
    return [seq0, seq1, seq2, seq3]


score = 0

for code in input:
    seqs = special_encode(code)
    # print(f'{code}: {seqs[0]}')
    # for s in seqs:
    #     print(s)
    score += int(code[:len(code) - 1]) * len(seqs[0])

print(score)


def cost(seq):
    c = 0
    for i in range(0, len(seq) - 1):
        dy, dx = v.diff(sym_to_pos(dkbd, seq[i]), sym_to_pos(dkbd, seq[i + 1]))
        c += abs(dy) + abs(dx)
    return c

print()

print(special_encode('456A'))
print(special_decode('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A'))

print(encode(dkbd, '<vA'), cost(encode(dkbd, '<vA')))
print(encode(dkbd, 'v<A'), cost(encode(dkbd, 'v<A')))
print(cost('v<A<A>>^A'), cost('v<A<A^>>A'))


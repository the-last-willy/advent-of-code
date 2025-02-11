import unittest

import helpers.input as i
from helpers.grid import *
import helpers.vec2 as vec

num_keypad = ['789', '456', '123', ' 0A']
dir_keypad = [' ^A', '<v>']

directions = {
    '<': (0, -1),
    '>': (0, 1),
    'v': (1, 0),
    '^': (-1, 0),
}


def is_valid_path(keyboard, pos, path):
    for s in path:
        pos = vec.sum(pos, directions[s])
        if at(keyboard, pos) == ' ':
            return False
    return True


def move(keyboard, a, b):
    posa = find_val(keyboard, a)
    posb = find_val(keyboard, b)

    d = vec.diff(posb, posa)

    v = ('v' if d[0] > 0 else '^') * abs(d[0])
    h = ('>' if d[1] > 0 else '<') * abs(d[1])

    paths = [p for p in [h + v, v + h] if is_valid_path(keyboard, posa, p)]
    paths = sorted(paths, key=lambda p: len(encode_dirs(encode_dirs(p))))

    return paths[0]


def encode_dirs(dirs):
    dirs = 'A' + dirs
    code = ''

    for i in range(1, len(dirs)):
        a = dirs[i - 1]
        b = dirs[i - 0]

        code += move(dir_keypad, a, b)

        code += 'A'

    return code


def encode_nums(nums):
    nums = 'A' + nums
    code = ''

    for i in range(1, len(nums)):
        a = nums[i - 1]
        b = nums[i - 0]

        code += move(num_keypad, a, b)

        code += 'A'

    return code


def decode(keypad, dirs):
    pos = find_val(keypad, 'A')
    code = ''
    for d in dirs:
        if d == 'A':
            code += at(keypad, pos)
        else:
            pos = vec.sum(pos, directions[d])
    return code


cache = {}


def dirs_encode_len(dirs, i):
    if (dirs, i) in cache:
        return cache[(dirs, i)]
    if i == 0:
        return len(dirs)
    else:
        pieces = [x + 'A' for x in encode_dirs(dirs).split('A')[:-1]]
        length = cache[(dirs, i)] = sum([dirs_encode_len(p, i-1) for p in pieces])
        return length


def nums_encode_len(nums, count):
    dirs = encode_nums(nums)
    return dirs_encode_len(dirs, count)


class TestDay21Part2(unittest.TestCase):
    def test_029A_0(self):
        self.assertEqual(len('<A^A>^^AvvvA'), nums_encode_len('029A', 0))

    def test_029A_1(self):
        self.assertEqual(len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A'), nums_encode_len('029A', 1))

    def test_029A_2(self):
        self.assertEqual(68, nums_encode_len('029A', 2))

    def test_example(self):
        codes = ['029A', '980A', '179A', '456A', '379A']
        sum = 0
        for c in codes:
            sum += nums_encode_len(c, 2) * int(c[:-1])
        self.assertEqual(126384, sum)

    def test_input(self):
        codes = i.read_file('../inputs/day21.txt').splitlines()
        print(codes)
        sum = 0
        for c in codes:
            sum += nums_encode_len(c, 25) * int(c[:-1])
        print(sum)

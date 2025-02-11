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

        pa = find_val(dir_keypad, a)
        pb = find_val(dir_keypad, b)

        d = vec.diff(pb, pa)
        
        if d[0] > 0:
            code += 'v' * abs(d[0])
        
        if d[1] > 0:
            code += '>' * abs(d[1])

        # ---
            
        if d[0] < 0:
            code += '^' * abs(d[0])

        if d[1] < 0:
            code += '<' * abs(d[1])

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


def encode1(nums):
    return encode_nums(nums)


def encode2(nums):
    return encode_dirs(encode1(nums))


def encode3(nums):
    return encode_dirs(encode2(nums))


def decode1(dirs):
    return decode(dir_keypad, dirs)


def decode2(dirs):
    return decode(dir_keypad, decode1(dirs))


def decode3(dirs):
    return decode(num_keypad, decode2(dirs))


class TestDay21Part1(unittest.TestCase):
    def test_corner_case(self):
        self.assertEqual(
            '^A<<^^A>>AvvvA',
            encode1('379A')
        )

    def subtests_for(self, code, encoded3):
        print(f'Code      : {code}')
        print(f'Actual   1: {encode1(code)}')
        print(f'Expected 1: {decode2(encoded3)}')
        print(f'Actual   2: {encode2(code)}')
        print(f'Expected 2: {decode1(encoded3)}')
        print(f'Actual   3: {encode3(code)}')
        print(f'Expected 3: {encoded3}')

        with self.subTest('encode1'):
            self.assertEqual(
                decode2(encoded3),
                encode1(code))
        with self.subTest('len encode2'):
            self.assertLen(
                decode1(encoded3),
                encode2(code))
        with self.subTest('len encode3'):
            self.assertLen(
                encoded3,
                encode3(code))

    def test_029A(self):
        self.subtests_for('029A', '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')

    def test_980A(self):
        self.subtests_for('980A', '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A')

    def test_179A(self):
        self.subtests_for('179A', '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')

    def test_456A(self):
        self.subtests_for('456A', '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A')

    def test_379A(self):
        self.subtests_for('379A', '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')

    def test_example(self):
        codes = ['029A', '980A', '179A', '456A', '379A']
        sum = 0
        for c in codes:
            sum += len(encode3(c)) * int(c[:-1])
        self.assertEqual(126384, sum)

    def test_input(self):
        codes = i.read_file('../inputs/day21.txt').splitlines()
        print(codes)
        sum = 0
        for c in codes:
            sum += len(encode3(c)) * int(c[:-1])
        print(sum)

    def assertLen(self, expected, actual):
        self.assertEqual(
            len(expected), len(actual),
            f"""
            Expected: {expected}
            Actual:   {actual}
            """)

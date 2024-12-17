class Computer:
    def __init__(self):
        self.reg_a = 0
        self.reg_b = 0
        self.reg_c = 0
        self.ip = 0

        self.program = []
        self.output = []

    def combo(self, x):
        if 0 <= x <= 3:
            return x
        if 4 <= x <= 6:
            return [self.reg_a, self.reg_b, self.reg_c][x - 4]

    def combo_str(self, x):
        if 0 <= x <= 3:
            return f'{x}'
        if 4 <= x <= 6:
            i = x - 4
            letter = ['a', 'b', 'c'][i]
            val = self.combo(x)
            return f'{letter}|{val}'

    def reg_str(self, x):
        if x == 'a':
            return f'reg_a|{self.reg_a}'
        if x == 'b':
            return f'reg_b|{self.reg_b}'
        if x == 'c':
            return f'reg_c|{self.reg_c}'

    def adv(self, combo_op):
        num = self.reg_a
        den = 2 ** self.combo(combo_op)
        res = num // den
        self.debug(
            f'adv({combo_op}) # a|{res} = a|{self.reg_a} / 2**{self.combo_str(combo_op)} = a|{self.reg_a} / {den}')
        self.reg_a = num // den
        self.ip += 2

    def bxl(self, literal_op):
        res = self.reg_b ^ literal_op
        self.debug(f'bxl({literal_op}) # b|{res} = b|{self.reg_b} ^ {literal_op}')
        self.reg_b = res
        self.ip += 2

    def bst(self, combo_op):
        res = self.combo(combo_op) % 8
        self.debug(f'bst({combo_op}) # b|{res} = {self.combo_str(combo_op)} % 8')
        self.reg_b = res
        self.ip += 2

    def jnz(self, literal_op):
        self.debug(f'jnz({literal_op}) # a|{self.reg_a}')
        if self.reg_a != 0:
            self.ip = literal_op
        else:
            self.ip += 2

    def bxc(self, unused):
        res = self.reg_b ^ self.reg_c
        self.debug(f'bst(_) # b|{res} = b|{self.reg_b} ^ c|{self.reg_c}')
        self.reg_b = res
        self.ip += 2

    def out(self, combo_op):
        self.debug(f'== out({combo_op}) # a|{self.reg_a} b|{self.reg_b} c|{self.reg_c}')
        self.output += [self.combo(combo_op) % 8]
        self.ip += 2

    def bdv(self, combo_op):
        num = self.reg_a
        den = 2 ** self.combo(combo_op)
        res = num // den
        self.debug(
            f'bdv({combo_op}) # b|{res} = a|{self.reg_a} / 2**{self.combo_str(combo_op)} = a|{self.reg_a} / {den}')
        self.reg_b = res
        self.ip += 2

    def cdv(self, combo_op):
        num = self.reg_a
        den = 2 ** self.combo(combo_op)
        res = num // den
        self.debug(
            f'cdv({combo_op}) # c|{res} = a|{self.reg_a} / 2**{self.combo_str(combo_op)} = a|{self.reg_a} / {den}')
        self.reg_c = res
        self.ip += 2

    def halted(self):
        return not 0 <= self.ip < len(self.program)

    def execute(self):
        ops = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

        self.ip = 0
        self.output = []

        while not self.halted():
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            ops[opcode](operand)

    def debug(self, str):
        # print(str)
        pass


def program(a):
    i = a % 8
    j = (a >> (i ^ 1)) % 8
    b = i ^ j ^ 4
    # print(a, i, j, b % 8)
    return a // 8, b % 8


def find_a(computer, base, rank):
    if rank < 0:
        return base
    for i in range(8):
        if base == 0 and i == 0:
            continue
        a = base + i * 8 ** rank
        computer.reg_a = a
        computer.execute()
        if computer.output[rank] != computer.program[rank]:
            continue
        a = find_a(computer, a, rank - 1)
        if a is not None:
            return a
    return None


c = Computer()
c.program = [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0]

print(find_a(c, 0, len(c.program) - 1))

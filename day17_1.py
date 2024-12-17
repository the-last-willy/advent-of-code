class Computer:
    reg_a = 0
    reg_b = 0
    reg_c = 0
    ip = 0

    program = []
    output = []

    def combo(self, x):
        if 0 <= x <= 3:
            return x
        if 4 <= x <= 6:
            return [self.reg_a, self.reg_b, self.reg_c][x - 4]


    def adv(self, combo_op):
        print(f'adv({combo_op})')
        num = self.reg_a
        den = 2 ** self.combo(combo_op)
        self.reg_a = num // den
        self.ip += 2


    def bxl(self, literal_op):
        self.reg_b = self.reg_b ^ literal_op
        self.ip += 2


    def bst(self, combo_op):
        print(f'bst({combo_op})')
        self.reg_b = self.combo(combo_op) % 8
        self.ip += 2


    def jnz(self, literal_op):
        print(f'jnz({literal_op})')
        if self.reg_a != 0:
            self.ip = literal_op
        else:
            self.ip += 2


    def bxc(self, unused):
        self.reg_b = self.reg_b ^ self.reg_c
        self.ip += 2


    def out(self, combo_op):
        print(f'out({combo_op})')
        self.output += [self.combo(combo_op) % 8]
        self.ip += 2


    def bdv(self, combo_op):
        num = self.reg_a
        den = 2 ** self.combo(combo_op)
        self.reg_b = num // den
        self.ip += 2


    def cdv(self, combo_op):
        num = self.reg_a
        den = 2 ** self.combo(combo_op)
        self.reg_c = num // den
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

        i = 0
        while not self.halted():
            print(self.ip, self.reg_a, self.reg_b, self.reg_c, self.output)
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            ops[opcode](operand)
            i += 1


c = Computer()
c.program = [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0]
c.reg_a = 56256477

c.execute()

print(','.join([str(x) for x in c.output]))

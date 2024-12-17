input = ''

with open('../inputs/day07.txt') as f:
    input = f.read().splitlines()

input = [line.split(': ') for line in input]
input = [(int(res), [int(x) for x in nums.split(' ')]) for res, nums in input]


def test(res, right0, remainders):
    if len(remainders) == 0:
        return res == right0

    return test(res, right0 + remainders[0], remainders[1:]) \
        or test(res, right0 * remainders[0], remainders[1:]) \
        or test(res, int(str(right0) + str(remainders[0])), remainders[1:])


sum = 0

for r, xs in input:
    if test(r, xs[0], xs[1:]):
        sum += r

print(sum)

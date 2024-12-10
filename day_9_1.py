input = ''

with open('inputs/day9.txt', 'r') as f:
    input = f.read()

size = sum([int(c) for c in input])

print(size)

file = ['.'] * size

print(file)

j = 0
for i, c in enumerate(input):
    for _ in range(int(c)):
        if i % 2 == 0:
            file[j] = i // 2
        j += 1

print(file)

l = 0

beg = 0
end = len(file) - 1

while True:
    print(l)
    l += 1

    while file[beg] != '.':
        beg += 1

    while file[end] == '.':
        end -= 1

    if beg >= end:
        break

    file[beg] = file[end]
    file[end] = '.'

checksum = 0

for i in range(len(file)):
    if file[i] != '.':
        checksum += file[i] * i

print(checksum)

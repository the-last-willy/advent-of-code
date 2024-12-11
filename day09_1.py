input = ''

with open('inputs/day09.txt') as f:
    input = f.read()

# input = input[:5]

file = []

for i, n in enumerate(input):
    id = i // 2 if i % 2 == 0 else '.'
    for j in range(int(n)):
        file += [id]

print(file)

beg = 0
end = len(file) - 1

while True:
    while file[end] == '.':
        end -= 1

    while file[beg] != '.':
        beg += 1

    if beg >= end:
        break

    file[beg] = file[end]
    file[end] = '.'

    end -= 1
    beg += 1

    # print(file)



print(file)

sum = 0

for i in range(len(file)):
    if file[i] != '.':
        sum += i * int(file[i])

print(sum)

input = ''

with open('inputs/day9.txt') as f:
    input = f.read()

# input = input[:5]

file = []

for i, n in enumerate(input):
    id = i // 2 if i % 2 == 0 else '.'
    for j in range(int(n)):
        file += [id]

print(file)

beg = 0
endB = len(file) - 1

while True:
    while file[endB] == '.':
        endB -= 1

    if file[endB] == 0:
        break

    print(f'handling {file[endB]}')

    endA = endB
    while file[endA-1] == file[endB]:
        endA -= 1

    endSz = endB - endA + 1

    begA = 0

    while True:
        while file[begA] != '.':
            begA += 1

        if begA >= endA:
            endB -= endSz
            break

        begB = begA
        while file[begB+1] == '.':
            begB += 1

        begSz = begB - begA + 1

        done = False

        if begSz >= endSz:
            for i in range(endSz):
                file[begA+i], file[endA+i] = file[endA+i], '.'
                done = True
            break

        if done:
            break
        else:
            begA += begSz

    # print(file)

sum = 0

for i in range(len(file)):
    if file[i] != '.':
        sum += i * int(file[i])

print(sum)

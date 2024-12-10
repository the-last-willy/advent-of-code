import json

input = ''

with open('inputs/day9.txt', 'r') as f:
    input = f.read()

# input = input[:64]

def compact(fs):
    endi = len(fs) - 1
    while endi > 0:
        fend = fs[endi]
        if fend['id'] == -1:
            endi -= 1
            continue
        begi = 0
        while begi < endi:
            fbeg = fs[begi]
            if fbeg['id'] != -1 or fend['size'] > fbeg['size']:
                begi += 1
                continue

            fs.insert(begi + 1, {
                'id': -1,
                'offset': fbeg['offset'] + fend['size'],
                'size': fbeg['size'] - fend['size'],
            })

            fbeg['id'] = fend['id']
            fbeg['size'] = fend['size']

            # print(f'move {fend['id']} to {fbeg['offset']}')
            #
            # print(to_str(fs))

            fend['id'] = -1

            begi += 1
            break

        endi -= 1


def checksum(fs):
    sum = 0

    for f in fs:
        if f['id'] != -1:
            for i in range(f['offset'], f['offset'] + f['size']):
                sum += i * int(f['id'])

    return sum


def to_str(fs):
    s = ''
    for f in fs:
        i = f['id']
        if i == -1:
            s += '.'.rjust(3) * f['size']
        else:
            s += str(i).rjust(3) * f['size']

    return s


fs = []

offset = 0
id = 0

for i, size in enumerate(input):
    id = i // 2 if i % 2 == 0 else -1
    size = int(size)
    if size > 0:
        fs.append({
            'id': id,
            'offset': offset,
            'size': size
        })
    offset += size

# print(input)
# print(json.dumps(fs, indent=4))
print(to_str(fs))
compact(fs)

print(checksum(fs))

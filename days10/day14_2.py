import re

from PIL import Image, ImageDraw

input = ''

with open('../inputs/day14.txt') as f:
    input = f.read()

input = re.findall(r'-?\d+', input)
input = [int(x) for x in input]
input = [input[i:i + 4] for i in range(0, len(input), 4)]


def pmod(x, d):
    return (x % d + d) % d


def cmp(a, b):
    return (a > b) - (a < b)


w, h = 101, 103

for seconds in range(27, 10000, w):
    img = Image.new('RGB', (w, h))
    draw = ImageDraw.Draw(img)

    for x, y, dx, dy in input:
        px = pmod(x + seconds * dx, w)
        py = pmod(y + seconds * dy, h)

        draw.point((px, py), fill=(255, 255, 255))

    img.save(f'outputs/{seconds}.png')
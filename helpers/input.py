def read_file(filename):
    content = None
    with open(filename, 'r') as f:
        content = f.read()
    return content


def parse_grid(txt: str):
    return [[c for c in row] for row in txt.splitlines()]

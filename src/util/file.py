def open_file(name):
    file = open(f'./src/{name}.txt')
    lines = []
    for line in file:
        lines.append(line.strip())
    return lines

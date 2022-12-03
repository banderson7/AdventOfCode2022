def open_file(name):
    file = open(f'{name}.txt')
    lines = []
    for line in file:
        lines.append(line.strip())
    return lines

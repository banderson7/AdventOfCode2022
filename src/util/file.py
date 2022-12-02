def open_file(name):
    file = open(f'strategy.txt')
    lines = []
    for line in file:
        lines.append(line.strip())
    return lines

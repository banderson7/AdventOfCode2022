def open_file(name):
    file = open(f'C:/Users/bill/PycharmProjects/AdventOfCode2022/src/{name}.txt')
    lines = []
    for line in file:
        lines.append(line.strip())
    return lines

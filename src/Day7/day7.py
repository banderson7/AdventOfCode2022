from src.Day7.FileSystem import FileSystem
from src.Day7.Terminal import Terminal

if __name__ == '__main__':
    terminal_file = open('terminal.txt')
    lines = []
    for line in terminal_file:
        lines.append(line.strip())
    terminal = Terminal()
    terminal.input_commands(lines)
    directories = terminal.get_directories_under_100000_total()
    # part 1 answer
    print(directories)

    file_system = FileSystem(terminal.root_directory.get_total_size())
    size = file_system.get_smallest_directory_to_clean(terminal.all_directories)
    # part 2 answer
    print(size)
    pass

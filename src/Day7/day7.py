class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent_directory):
        self.name = name
        self.parent_directory = parent_directory
        self.directories = []
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def add_directory(self, directory):
        self.directories.append(directory)

    def get_total_size(self):
        size = 0
        for file in self.files:
            size += int(file.size)
        for directory in self.directories:
            size += directory.get_total_size()
        return size

    def get_child_directory(self, name):
        for directory in self.directories:
            if directory.name == name:
                return directory


class Terminal:
    def __init__(self):
        self.root_directory = Directory('/', None)
        self.current_directory = self.root_directory
        self.all_directories = []

    def get_directories_under_100000_total(self):
        found_directories = []
        for directory in self.all_directories:
            if directory.get_total_size() < 100000:
                found_directories.append(directory)
        total_size = 0
        for directory in found_directories:
            total_size += directory.get_total_size()
        return total_size

    def input_commands(self, commands):
        for command in commands:
            # Input action
            if str.startswith(command, '$'):
                input = command.split()
                input_command = input[1]
                if input_command == 'ls':
                    pass
                elif input_command == 'cd':
                    directory = input[2]
                    if directory == '..':
                        self.current_directory = self.current_directory.parent_directory
                    elif directory == '/':
                        # Skip initial cd
                        pass
                    else:
                        child_directory = self.current_directory.get_child_directory(directory)
                        self.current_directory = child_directory
            elif str.startswith(command, 'dir'):
                output = command.split()
                new_directory = Directory(output[1], self.current_directory)
                self.all_directories.append(new_directory)
                self.current_directory.add_directory(new_directory)
            else:
                output = command.split()
                new_file = File(output[1], output[0])
                self.current_directory.add_file(new_file)

if __name__ == '__main__':
    terminal_file = open('terminal.txt')
    lines = []
    for line in terminal_file:
        lines.append(line.strip())
    terminal = Terminal()
    terminal.input_commands(lines)
    directories = terminal.get_directories_under_100000_total()
    print(directories)
    pass
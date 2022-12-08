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

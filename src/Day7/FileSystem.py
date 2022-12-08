import sys


class FileSystem:
    total_space = 70000000
    required_space = 30000000

    def __init__(self, used_space):
        self.used_space = used_space

    def get_available_space(self):
        return self.total_space - self.used_space

    def get_space_to_be_cleaned(self):
        return self.required_space - self.get_available_space()

    def get_smallest_directory_to_clean(self, all_directories):
        smallest_directory_size = sys.maxsize
        amount_to_clean = self.get_space_to_be_cleaned()
        for directory in all_directories:
            current_directory_size = directory.get_total_size()
            if amount_to_clean <= current_directory_size < smallest_directory_size:
                smallest_directory_size = current_directory_size
        return smallest_directory_size

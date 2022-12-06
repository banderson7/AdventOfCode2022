from src.domain.Reaarange.Group import Group
from src.domain.Reaarange.Rucksack import Rucksack


def get_matching_item_total(data):
    start = 0
    end = len(data)
    step = 3
    total = 0
    for i in range(start, end, step):
        x = i
        group_data = data[x:x + step]
        group = Group(group_data)
        total += group.get_matching_priority()
    return total


class RucksackAnalizer:
    def __init__(self, item_data):
        self.total = 0
        for line in item_data:
            rucksack = Rucksack()
            self.total += rucksack.get_matching_item_priority(line)

    def get_total(self):
        return self.total


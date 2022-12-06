from src.domain.Reaarange.Item import Item
from src.domain.Reaarange.Rucksack import Rucksack


class Group:
    def __init__(self, group_data):
        self.elves_rucksacks = group_data

    def get_matching_priority(self):
        for elf in self.elves_rucksacks[0]:
            for item in elf:
                for elf_two in self.elves_rucksacks[1]:
                    for item_two in elf_two:
                        if item == item_two:
                            for elf_three in self.elves_rucksacks[2]:
                                for item_three in elf_three:
                                    if item == item_three:
                                        matching_item = Item(item)
                                        return matching_item.priority

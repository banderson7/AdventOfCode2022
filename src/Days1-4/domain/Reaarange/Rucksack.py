from src.domain.Reaarange.Compartment import Compartment
from src.domain.Reaarange.Item import Item


class Rucksack:
    def __init__(self):
        self.first_compartment = Compartment()
        self.second_compartment = Compartment()

    def get_matching_item_priority(self, items):
        first_set, second_set = items[:len(items)//2], items[len(items)//2:]
        self.first_compartment.add_items(first_set)
        self.second_compartment.add_items(second_set)

        for item in first_set:
            for other_item in second_set:
                if item == other_item:
                    matching_item = Item(item)
                    return matching_item.priority

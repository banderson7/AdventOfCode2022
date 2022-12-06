from src.domain.Reaarange.Rucksack import Rucksack


class RucksackPrioritizer:
    def __init__(self, item_data):
        self.total = 0
        for line in item_data:
            rucksack = Rucksack()
            self.total += rucksack.get_matching_item_priority(line)

    def get_total(self):
        return self.total

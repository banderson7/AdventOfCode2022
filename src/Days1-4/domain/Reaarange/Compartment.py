from src.domain.Reaarange.Item import Item


class Compartment:
    def __init__(self):
        self.items = []

    def add_items(self, items):
        for item in items:
            new_item = Item(item)
            self.items.append(new_item)

    def contains_item(self, item: Item):
        return self.items.__contains__(item)

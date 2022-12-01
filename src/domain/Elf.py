class Elf:
    def __init__(self, carried_food=None):
        if carried_food is None:
            carried_food = []
        self.carried_food = carried_food

    def food_calorie_total(self):
        total = 0
        for i in range(0, len(self.carried_food)):
            total += self.carried_food[i].get_calories()
        return total

    def add_food(self, food):
        self.carried_food.append(food)

from src.domain.Elf import Elf
from src.domain.Food import Food


class Expedition:
    def __init__(self, calorie_input):
        self.elves = []
        current_elf = Elf()
        for line in calorie_input:
            if line != '':
                current_elf.add_food(Food(int(line)))
            else:
                self.elves.append(current_elf)
                current_elf = Elf()
        self.elves.append(current_elf)

    def get_top_n_elf_calories(self, count):
        calorie_totals = []
        for elf in self.elves:
            calorie_totals.append(elf.food_calorie_total())
        calorie_totals.sort(reverse=True)

        top_calorie_total = 0
        for i in range(0, count):
            top_calorie_total += calorie_totals[i]

        return top_calorie_total

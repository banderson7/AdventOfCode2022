import unittest

from src.domain.CalorieCounting.Elf import Elf
from src.domain.CalorieCounting.Food import Food


class TestElf(unittest.TestCase):
    def test_add_food_adds_food_to_carried_food(self):
        elf = Elf()
        food = Food(500)

        elf.add_food(food)

        self.assertEqual(elf.carried_food[0], food)  # add assertion here

    def test_food_calorie_total_returns_total_of_all_carried_food(self):
        elf = Elf()
        food = Food(500)
        food2 = Food(300)

        elf.add_food(food)
        elf.add_food(food2)

        self.assertEqual(elf.food_calorie_total(), 800)


if __name__ == '__main__':
    unittest.main()

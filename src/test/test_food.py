import unittest

from src.domain.Food import Food


class TestFood(unittest.TestCase):
    def test_get_calories_returns_calories(self):
        food = Food(3000)
        self.assertEqual(food.get_calories(), 3000)  # add assertion here


if __name__ == '__main__':
    unittest.main()

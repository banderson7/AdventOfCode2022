import unittest

from src.domain.Expedition import Expedition


class TestExpeditionGetTopNElfCalories(unittest.TestCase):
    def test_get_top_n_elf_calories_returns_single_highest_calorie_count(self):
        test_data = ['2000', '1000', '', '500', '300', '200', '', '4000']

        expedition = Expedition(test_data)
        self.assertEqual(expedition.get_top_n_elf_calories(1), 4000)

    def test_get_top_n_elf_calories_returns_expected_top_3_calorie_count(self):
        test_data = ['2000', '1000', '', '500', '300', '200', '', '4000', '', '1000', '300']

        expedition = Expedition(test_data)
        self.assertEqual(expedition.get_top_n_elf_calories(3), 8300)


if __name__ == '__main__':
    unittest.main()

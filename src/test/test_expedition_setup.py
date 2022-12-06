import unittest

from src.domain.CalorieCounting.Expedition import Expedition


class TestExpeditionSetup(unittest.TestCase):

    def test_elves_split_by_empty_line(self):
        test_input = ['100', '120', '', '130', '111']
        expedition = Expedition(test_input)

        self.assertEqual(len(expedition.elves), 2)

    def test_all_elves_are_created(self):
        test_input = ['100', '120', '', '130', '111']
        expedition = Expedition(test_input)

        self.assertEqual(len(expedition.elves), 2)

    def test_elves_receive_one_food_for_each_calorie_count(self):
        test_input = ['100', '200']
        expedition = Expedition(test_input)

        self.assertEqual(len(expedition.elves[0].carried_food), 2)


if __name__ == '__main__':
    unittest.main()

import string

from src.domain.Assignment import AssignmentPair
from src.domain.Reaarange.Group import Group
from src.domain.Reaarange.Rucksack import Rucksack

from src.domain.Reaarange.RucksackAnalizer import get_matching_item_total
from src.domain.RockPaperScissors.Tournament import Tournament
from src import file

if __name__ == '__main__':
    # day 1
    # calorie_data = file.open_file('input')
    # expedition = Expedition(calorie_data)
    # print(expedition.get_top_n_elf_calories(3))

    # day 2
    # strategy_data = file.open_file('strategy')
    # tournament = Tournament(strategy_data)
    # print(tournament.get_all_rounds_total())

    # day 3
    # rearrange_data = file.open_file('rearrange')
    # print(get_matching_item_total(rearrange_data))
    # rucksack_prioritizer = RucksackAnalizer(rearrange_data)
    # print(rucksack_prioritizer.get_total())

    cleanup_data = file.open_file('cleanup')
    pairs = []
    total = 0
    for line in cleanup_data:
        split_line = line.split(',')
        pairs.append(split_line)
    for pair in pairs:
        assignments = AssignmentPair(pair)
        if assignments.b_minimum <= assignments.a_minimum <= assignments.b_maximum \
                or assignments.a_minimum <= assignments.b_minimum <= assignments.a_maximum:
            total += 1
    print(total)

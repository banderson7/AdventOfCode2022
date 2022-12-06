import string

from src.domain.Reaarange.Group import Group
from src.domain.Reaarange.Rucksack import Rucksack
from src.domain.Reaarange.RucksackPrioritizer import RucksackPrioritizer
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
    rearrange_data = file.open_file('rearrange')
    start = 0
    end = len(rearrange_data)
    step = 3
    total = 0
    for i in range(start, end, step):
        x = i
        group_data = rearrange_data[x:x + step]
        group = Group(group_data)
        total += group.get_matching_priority()
    print(total)
    # rucksack_prioritizer = RucksackPrioritizer(rearrange_data)
    # print(rucksack_prioritizer.get_total())


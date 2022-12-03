from src.domain.RockPaperScissors.Tournament import Tournament
from src import file

if __name__ == '__main__':
    # calorie_data = file.open_file('input')
    # expedition = Expedition(calorie_data)
    # print(expedition.get_top_n_elf_calories(3))

    strategy_data = file.open_file('strategy')
    tournament = Tournament(strategy_data)
    print(tournament.get_all_rounds_total())


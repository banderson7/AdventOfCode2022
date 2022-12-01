from src.util import file
from src.domain.Expedition import Expedition

if __name__ == '__main__':
    calorie_data = file.open_file('input')
    expedition = Expedition(calorie_data)
    print(expedition.get_top_n_elf_calories(3))

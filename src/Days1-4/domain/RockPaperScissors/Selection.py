from src.domain.RockPaperScissors.Options import Options


class Selection:
    def __init__(self, encrypted_input):
        option = Options.SCISSORS
        if encrypted_input == 'A' or encrypted_input == 'X':
            option = Options.ROCK
        elif encrypted_input == 'B' or encrypted_input == 'Y':
            option = Options.PAPER
        elif encrypted_input == 'C' or encrypted_input == 'Z':
            option = Options.SCISSORS
        self.option = option

    def get_selection_score(self):
        return self.option

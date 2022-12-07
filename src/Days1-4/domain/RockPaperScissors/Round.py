from src.domain.RockPaperScissors.Options import Options
from src.domain.RockPaperScissors.Outcomes import Outcomes
from src.domain.RockPaperScissors.Selection import Selection


class Round:
    lose_input = 'X'
    tie_input = 'Y'
    win_input = 'Z'

    def __init__(self, opponent_input, outcome_input):
        self.opponent_selection = Selection(opponent_input)
        self.outcome_input = outcome_input

    def get_result(self):
        if self.opponent_selection.option == Options.ROCK:
            if self.outcome_input == self.lose_input:
                return Outcomes.LOSE.value + Options.SCISSORS.value
            elif self.outcome_input == self.tie_input:
                return Outcomes.TIE.value + Options.ROCK.value
            elif self.outcome_input == self.win_input:
                return Outcomes.WON.value + Options.PAPER.value
        elif self.opponent_selection.option == Options.PAPER:
            if self.outcome_input == self.lose_input:
                return Outcomes.LOSE.value + Options.ROCK.value
            elif self.outcome_input == self.tie_input:
                return Outcomes.TIE.value + Options.PAPER.value
            elif self.outcome_input == self.win_input:
                return Outcomes.WON.value + Options.SCISSORS.value
        elif self.opponent_selection.option == Options.SCISSORS:
            if self.outcome_input == self.lose_input:
                return Outcomes.LOSE.value + Options.PAPER.value
            elif self.outcome_input == self.tie_input:
                return Outcomes.TIE.value + Options.SCISSORS.value
            elif self.outcome_input == self.win_input:
                return Outcomes.WON.value + Options.ROCK.value

from src.domain.RockPaperScissors.Options import Options
from src.domain.RockPaperScissors.Outcomes import Outcomes
from src.domain.RockPaperScissors.Selection import Selection


class Round:
    def __init__(self, opponent_input, player_input):
        self.opponent_selection = Selection(opponent_input)
        self.player_selection = Selection(player_input)

    def get_round_result(self):
        if self.opponent_selection.option == self.player_selection.option:
            return Outcomes.TIE.value + self.player_selection.option.value
        elif self.opponent_selection.option == Options.ROCK:
            if self.player_selection.option == Options.PAPER:
                return Outcomes.WON.value + self.player_selection.option.value
            else:
                return Outcomes.LOSE.value + self.player_selection.option.value
        elif self.opponent_selection.option == Options.PAPER:
            if self.player_selection.option == Options.SCISSORS:
                return Outcomes.WON.value + self.player_selection.option.value
            else:
                return Outcomes.LOSE.value + self.player_selection.option.value
        elif self.opponent_selection.option == Options.SCISSORS:
            if self.player_selection.option == Options.ROCK:
                return Outcomes.WON.value + self.player_selection.option.value
            else:
                return Outcomes.LOSE.value + self.player_selection.option.value

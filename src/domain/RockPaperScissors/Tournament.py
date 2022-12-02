from src.domain.RockPaperScissors.Round import Round


class Tournament:
    def __init__(self, strategy_input):
        self.rounds = []
        for line in strategy_input:
            split_inputs = line.split()
            new_round = Round(split_inputs[0], split_inputs[1])
            self.rounds.append(new_round)

    def get_all_rounds_total(self):
        running_total = 0
        for round in self.rounds:
            running_total += round.get_round_result()
        return running_total

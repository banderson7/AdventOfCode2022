from src.file import open_file


class Procedure:
    def __init__(self, move_input, from_input, to_input):
        self.move_amount = int(move_input)
        self.from_stack = int(from_input)
        self.to_stack = int(to_input)


class Procedures:
    def __init__(self, procedure_file):
        procedure_lines = []
        for line in procedure_file:
            procedure_lines.append(line.strip())

        self.all_procedures = []
        for procedure_input in procedure_lines:
            procedure_array = procedure_input.split(' ')
            procedure = Procedure(procedure_array[1], procedure_array[3], procedure_array[5])
            self.all_procedures.append(procedure)


class Stacks:
    def __init__(self, stack_file):
        lines = []
        for line in stack_file:
            lines.append(line)

        # Remove Label line
        lines.pop()
        row_data = []
        for line in lines:
            stack_width = 4
            crate_data = [line[i:i + stack_width] for i in range(0, len(line), stack_width)]

            row_data.append(crate_data)

        stack_count = 9
        self.stacks_data = []
        for i in range(stack_count):
            stack = []
            for crate in row_data:
                iteration_crate = crate[i].strip()
                if iteration_crate == '':
                    continue

                stack.append(iteration_crate[1])
            # Reverse the array
            self.stacks_data.append(stack[::-1])

    def apply_procedures(self, procedures_to_apply: Procedures):
        for procedure in procedures_to_apply.all_procedures:
            for i in range(procedure.move_amount):
                crate_to_move = self.stacks_data[procedure.from_stack - 1].pop()
                self.stacks_data[procedure.to_stack - 1].append(crate_to_move)

    def apply_procedures_same_order(self, procedures_to_apply: Procedures):
        for procedure in procedures_to_apply.all_procedures:
            crates_to_move = self.stacks_data[procedure.from_stack - 1][-procedure.move_amount:]
            for crate in crates_to_move:
                self.stacks_data[procedure.from_stack - 1].pop()
                self.stacks_data[procedure.to_stack - 1].append(crate)


if __name__ == '__main__':
    stack_file = open('stacks.txt')
    stacks = Stacks(stack_file)
    procedure_file = open('procedure.txt')
    procedures = Procedures(procedure_file)
    stacks.apply_procedures_same_order(procedures)
    for i in range(len(stacks.stacks_data)):
        print(stacks.stacks_data[i].pop())


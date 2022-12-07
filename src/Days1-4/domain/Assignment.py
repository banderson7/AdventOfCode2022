class AssignmentPair:
    def __init__(self, assignment_data):
        assignment_a = assignment_data[0].split('-')
        assignment_b = assignment_data[1].split('-')
        self.a_minimum = int(assignment_a[0])
        self.a_maximum = int(assignment_a[1])
        self.b_minimum = int(assignment_b[0])
        self.b_maximum = int(assignment_b[1])

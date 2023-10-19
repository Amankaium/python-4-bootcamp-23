class Operation:
    def __init__(self, num_1, operation, num_2):
        if operation == "+":
            self.value = num_1 + num_2
        elif operation == "*":
            self.value = num_1 * num_2

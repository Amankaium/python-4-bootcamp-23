from .operation_class import Operation


class Decision:
    def __init__(self):
        while True:
            n_1 = int(input())

            if n_1 == 0:
                break

            op_1 = input()

            if op_1 == "0":
                break

            n_2 = int(input())

            if n_2 == 0:
                break

            op_object = Operation(n_1, op_1, n_2)
            print(op_object.value)

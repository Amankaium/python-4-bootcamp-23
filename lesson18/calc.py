# from my_lib.operation_class import Operation
# from my_lib.operation_class import *
from my_lib import *

n_1 = int(input())
op_1 = input()
n_2 = int(input())

op_object = Operation(n_1, op_1, n_2)
print(op_object.value)

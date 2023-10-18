'''
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
'''

class Factorial:
    def __init__(self, n):
        # найти произведение чисел от 1 до n
        res = 1
        for i in range(1, n + 1):
            res *= i
        self.value = res
    
    def find_sum_num(self):
        # найти сумму цифр self.value # int
        str_value = str(self.value)  # str # '3628800'
        sm = 0
        for k in str_value:
            sm += int(k) # str # '3'
        return sm

f_10 = Factorial(10)
print(f_10.value)
print(f_10.find_sum_num())

f_100 = Factorial(100)
print(f_100.value)
print(f_100.find_sum_num())

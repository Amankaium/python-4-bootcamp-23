# напишите функцию, 
# которая принимает n
# и возвращает n-ное
# число Фиббоначи

def find_fib(n):
    for i in range(n-1):
        if i == 0:
            fib_1 = 1
            fib_2 = 2
        else:
            fib_3 = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_3
    return fib_3

print(find_fib(6))
print(find_fib(10))

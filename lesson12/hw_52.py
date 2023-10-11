
def calc_deposit(a, years):
    for i in range(years):
        a += a * 0.1
    return a

print(calc_deposit(100, 2))
print(calc_deposit(100, 3))
print(calc_deposit(3512, 5))

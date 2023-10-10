# вызов функции print
print("hello")

# ввод и результат ввода записывается в переменную name
name = input()

# создание функции
def calc():
    a = 7
    b = a + 13
    print(a, b)

# вызов
# calc()
# calc()
print(calc())

# num_1 и num_2 - аргументы (параметры) функции sum_2
def sum_2(num_1, num_2):
    res = num_1 + num_2
    print(res)

# sum_2(4, 6)
# sum_2(777, 333)

def mult_3(z, x, c):
    res = z * x * c
    return res

k = 5 * 3 * 6
o = mult_3(7, 2, 5) # res # 70
print(o)


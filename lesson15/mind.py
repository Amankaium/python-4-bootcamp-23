# пользователь вводит число от 1 до 100,
# вам нужно написать программу которая отгадывает 
# это число, используя функцию и цикл

# Пример:
67

30
# больше

90
# меньше

50
# меньше

k = 10**10

def lucky(num):
    for i in range(1, k):
        if i == num:
            print(i, "Верно")
            break

def binary_search(num):
    q = 0
    c = int(k / 2)
    step = c / 2
    while True:
        print(c)
        if c < num:
            print("Меньше")
            c = round(c + step)
        elif c > num:
            print("Больше")
            c = round(c - step)
        else:
            print(c, f"Верно! Кол-во шагов {q}")
            break
        step /= 2
        q += 1


n = int(input(f"Введите число от 1 до {k}: ")) 
# lucky(n)
binary_search(n)

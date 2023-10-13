def first():
    print("это первая функция")     # 1 # 3 # 6 # 8

def second():
    print("Начало второй функции")  # 2 # 7
    first()
    print("конец второй функции")   # 4 # 9

def three():
    print("функция 3 старт")        # 5
    first()
    second()
    print("функция 3 конец")        # 10

def four():
    print("фантастическая функция 4")
    four()

first()
second()
three()
four()

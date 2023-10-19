'''
Ваша задача - переписать предоставленный код игры "Морской бой": https://clck.ru/368Bmo используя классы и разделяя его на несколько файлов.

Создайте класс Sea, который будет представлять море (игровое поле). У этого класса должны быть методы create_sea, render, и атрибут field, который представляет игровое поле.

Создайте класс Ship, который представляет корабль. У этого класса должны быть атрибуты is_alive, y (координата по вертикали) и x (координата по горизонтали). Метод __repr__ должен отображать корабль как "s" (живой) или " " (потоплен).

Разделите код на отдельные файлы следующим образом:

Основной файл (warship.py), который будет содержать инициализацию игры и игровой цикл.

Файл sea.py, содержащий класс Sea.

Файл ship.py, содержащий класс Ship.

Измените инициализацию игры, чтобы она создавала экземпляр Sea, а также создавала и добавляла корабли (Ship) в море.

Перепишите игровой цикл для взаимодействия с объектами классов Sea и Ship, проверки попаданий и отображения игрового поля.

Запустите игру в файле warship.py. Убедитесь, что она работает так же, как исходный код, но теперь использует классы и разделена на отдельные файлы.
'''

# класс морей
class Sea:
    # создаём пустое поле/море
    def __init__(self, field_size):
        field = [[' ' for j in range(field_size)] for i in range(field_size)]
        self.field = field


#  класс кораблей
class Ship:
    is_alive = True

    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def __repr__(self):
        if self.is_alive:
            return "s"
        else:
            return " "

# функция отрисовки моря (рендер)
def render(sea):
    for row in sea:
        for cell in row:
            print(cell, end='')
        print()


# генерация объектов
sea = Sea(8) # field_size

# добавляем корабли
ships = 3
for k in range(ships):
    y = int(input(f"координата 'y' корабля {k+1}: "))
    x = int(input(f"координата 'x' корабля {k+1}: "))
    ship_object = Ship(y, x)
    sea[y][x] = ship_object

# начинаем игру
while ships:
    # отрисовка моря
    render(sea)
    
    # ход противника
    fire_point = input("Противник стреляет: ") # 2 4
    points_list = fire_point.split() # ['2', '4']
    fire_y = int(points_list[0]) # 2 
    fire_x = int(points_list[1]) # 4

    # проверка попадания
    fired_cell = sea[fire_y][fire_x]
    if isinstance(fired_cell, Ship):
        print("попал")
        fired_cell.is_alive = False
        ships -= 1
    else:
        print("мимо")

print("End Game")

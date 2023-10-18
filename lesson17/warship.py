# создаём пустое поле/море
def create_sea(field_size): # 8
    new_sea = [[' ' for j in range(field_size)] for i in range(field_size)]
    return new_sea

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
sea = create_sea(8) # field_size

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

# создаём пустое поле/море
def create_sea(field_size): # 8
    new_sea = []
    for i in range(field_size): # 8
        new_sea.append([]) # [[]]
        for j in range(field_size): # 8
            new_sea[-1].append(' ')
    return new_sea

sea = create_sea(8) # field_size


# добавляем корабли
ships = 3
for k in range(ships):
    y = int(input(f"координата 'y' корабля {k+1}: "))
    x = int(input(f"координата 'x' корабля {k+1}: "))
    sea[y][x] = "s"

# начинаем игру
while ships:
    # отрисовка моря
    for row in sea:
        for cell in row:
            print(cell, end='')
        print()
    
    # ход противника
    fire_point = input("Противник стреляет: ") # 2 4
    points_list = fire_point.split() # ['2', '4']
    fire_y = int(points_list[0]) # 2 
    fire_x = int(points_list[1]) # 4

    # проверка попадания
    if sea[fire_y][fire_x] == "s":
        print("попал")
        sea[fire_y][fire_x] = " "
        ships -= 1
    else:
        print("мимо")

print("End Game")

from class_ship import Ship
from func_1 import create_sea
from func_2 import render


sea = create_sea(8) 


ships = 3
for k in range(ships):
    y = int(input(f"координата 'y' корабля {k+1}: "))
    x = int(input(f"координата 'x' корабля {k+1}: "))
    ship_object = Ship(y, x)
    sea[y][x] = ship_object


while ships:
    
    render(sea)
    
   
    fire_point = input("Противник стреляет: ") 
    points_list = fire_point.split()
    fire_y = int(points_list[0]) 
    fire_x = int(points_list[1]) 

    
    fired_cell = sea[fire_y][fire_x]
    if isinstance(fired_cell, Ship):
        print("попал")
        fired_cell.is_alive = False
        ships -= 1
    else:
        print("мимо")

print("End Game")
from class_ship import Ship
def render(sea):
    for row in sea:
        for cell in row:
            print(cell, end='')
        print()
# Написать программу season, принимающую 1 аргумент 
# — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень)

# Учитывайте корректность ввода.

month = int(input("Введите месяц: "))

# v1
# if month in [1, 2, 12]:
#     print("Зима")
# elif month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# else:
#     print("Некорректный ввод")



# v2
seasons = ["зима", "зима",
           "весна", "весна", "весна",
           "лето", "лето", "лето",
           "осень", "осень", "осень",  
           "зима"
           ]
if 1 <= month <= 12:
    print(seasons[month-1])
else:
    print("Некорректный ввод")

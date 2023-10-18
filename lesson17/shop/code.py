from laptop import Laptop, Example
from printer import Printer
from computer import Computer
import budget

hp = Laptop(15, 8, "HP Espire 1505", 700)
lenovo = Laptop(16, 32, "Lenovo white 777", 1100)

budget_18 = budget.DayBudget()
print(budget_18.money) # 150

# Человек покупает hp ноутбук
budget_18.sell(hp)
print(budget_18.money) # 850

# создайте по 1 объекту на Computer и Printer
# вызовите sell с этими объектами

printer_1 = Printer("LaserJet 23423", 300)
budget_18.sell(printer_1)
print(budget_18.money) # 1150

budget_18.sell(printer_1)
print(budget_18.money) # 1450
budget_18.sell(printer_1)
print(budget_18.money)
budget_18.sell(printer_1)
print(budget_18.money)
print(printer_1.qty)
budget_18.sell(printer_1)
print(budget_18.money)

comp_1 = Computer(24, 8, "HP bla bla", 1000)

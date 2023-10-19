class DayBudget:
    def __init__(self):
        with open("cash.txt", 'r') as money_file:
            self.money = int(money_file.readline())

    def sell(self, tech_object):
        if tech_object.qty > 0:
            self.money += tech_object.price
            tech_object.qty -= 1
            with open("cash.txt", "w") as money_file:
                money_file.write(str(self.money))
        else:
            print("Ошибка, такого товара не осталось")

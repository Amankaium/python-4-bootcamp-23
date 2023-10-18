class DayBudget:
    money = 150

    def sell(self, tech_object):
        if tech_object.qty > 0:
            self.money += tech_object.price
            tech_object.qty -= 1
        else:
            print("Ошибка, такого товара не осталось")

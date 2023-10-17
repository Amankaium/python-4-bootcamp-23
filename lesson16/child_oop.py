class Dog: # родитель # предок
    tail = 1
    paws = 4
    size = 0.5

    def run(self):
        self.status = "is_running"

    def talk(self):
        print("ГАВ")


class Wolf(Dog): # дочерний # родитель
    size = 1.5
    
    def talk(self):
        print("АУУУ")
    
    def hunt(self):
        self.run()
        # кушает
        self.size += 0.01


class PolarWolf(Wolf): # дочерний # потомок
    color = 'white'

    def run(self):
        super().run()
        self.run_distance = 50

class Cat: 
    paws = 4 
    tail = 1
    status = 'sleeps'

    def talk(self):
        print("Meow")

akela = PolarWolf()
# akela.run()
# print(akela.status) # is running
# print(akela.run_distance) # 50
akela.talk()
print(akela.size) # 1.5
akela.hunt()
print(akela.size) # 1.51
print(akela.status)
print(akela.run_distance)

# sharik = Dog()
# sharik.run()
# print(sharik.status) # is running
# print(sharik.run_distance) # Ошибка


# полиморфизм
barsik = Cat()
animals = [akela, barsik]
for animal in animals:
    animal.talk()

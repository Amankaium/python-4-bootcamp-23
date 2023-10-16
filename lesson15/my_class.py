a = 7
b = 'hello'
c = True
d = {1: 9} # dict
e = [5, 0, 3] # list
e.append(7) # метод
len(e) # функция

# print(type(a))
# print(type(e))

class Cat: # создание класса
    paws = 4 # свойства или аттрибут
    tail = 1
    status = 'sleeps'

    def say(self): # метод say
        print("Meow")


murzik = Cat()
murzik.tail # свойство tail
# print(type(murzik))
print(murzik.tail) 
print(murzik.status) # sleeps
murzik.say()

barsik = Cat()
barsik.status = 'hunting'
print(barsik.status) # hunting
print(murzik.status) # sleeps

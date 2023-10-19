from tech import Tech

# print("hello from file computer")
class Computer(Tech):
    has_keyboard = True
    has_mouse = True

    def __init__(self, screen_size, ram, model, price):
        self.screen_size = screen_size
        self.ram = ram
        self.model = model
        self.price = price
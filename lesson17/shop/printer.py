from tech import Tech


class Printer(Tech):
    is_color = False
    printer_type = 'laser'

    def __init__(self, model, price):
        self.model = model
        self.price = price
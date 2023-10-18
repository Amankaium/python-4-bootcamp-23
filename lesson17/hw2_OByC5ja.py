
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.area())

circle = Circle(5)
print("Площадь круга:", circle.area())


triangle = Triangle(3, 4)
print("Площадь треугольника:", triangle.area())



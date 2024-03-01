from math import pi

class Shapes:
    def calculate_area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 2 * pi * (self.radius ** 2)

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2

def intro(polygon):
    return polygon.calculate_area()

c1 = Circle(5)
r1 = Rectangle(4, 6)
t1 = Triangle(3, 8)

area_circle = intro(c1)
print("Area of the Circle:", area_circle)

area_rectangle = intro(r1)
print("Area of the Rectangle:", area_rectangle)

area_triangle = intro(t1)
print("Area of the Triangle:", area_triangle)


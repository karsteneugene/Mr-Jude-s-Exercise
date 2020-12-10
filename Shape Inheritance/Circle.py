import math
from Shape import Shape


class Circle(Shape):
    def __init__(self, radius=1.0):
        super().__init__()
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius: float):
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius**2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def toString(self):
        return f'A Circle with radius={self.radius}, which is a subclass of {super().toString()}'

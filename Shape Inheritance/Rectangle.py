from Shape import Shape


class Rectangle(Shape):
    def __init__(self, width: float = 1.0, length: float = 1.0):
        super().__init__()
        self.width = width
        self.length = length

    def getWidth(self):
        return self.width

    def setWidth(self, width: float):
        self.width = width

    def getLength(self):
        return self.length

    def setLength(self, length: float):
        self.length = length

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return 2 * (self.length + self.width)

    def toString(self):
        return f'A Rectangle with width={self.width} and length={self.length}, which is a ' \
               f'subclass of {super().toString()} '

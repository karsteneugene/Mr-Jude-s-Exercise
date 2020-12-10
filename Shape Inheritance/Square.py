from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def setWidth(self, side):
        self.width = side

    def setLength(self, side):
        self.length = side

    def toString(self):
        return f'A Square with side={self.side}, which is a subclass of {Rectangle.toString(self)}'

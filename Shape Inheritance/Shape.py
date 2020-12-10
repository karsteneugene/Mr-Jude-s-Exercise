class Shape:
    def __init__(self, color: str = 'green', filled: bool = True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color: str):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled: bool):
        self.filled = filled

    def toString(self):
        if self.filled is True:
            return f'A Shape with color of {self.color} and filled'
        else:
            return f'A Shape with color of {self.color} and not filled'

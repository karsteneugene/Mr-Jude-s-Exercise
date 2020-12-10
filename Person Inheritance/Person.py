class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address: str):
        self.address = address

    def toString(self):
        return f'{self.name}({self.address})'


class Vehicle:
    def __init__(self, color) -> None:
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"This vehicle is {self.getColor()}"

Vehicle1 = Vehicle("Red")

print(Vehicle1.toString())


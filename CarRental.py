# Vehicle class
class Vehicle:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"This vehicle is {self.color}"

# Car class
class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires

    def __str__(self):
        return f"{super().__str__()}\nHas winter tires: {self.has_winter_tires}"

# Truck class
class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def __str__(self):
        return f"{super().__str__()}\nHas trailer: {self.has_trailer}"

# Garage class
class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def set_vehicle(self, vehicle):
        self.parked_vehicle = vehicle

    def __str__(self):
        if self.parked_vehicle is None:
            return "No vehicle is parked in the garage."
        return f"Description of the parked vehicle:\n{self.parked_vehicle}"

# GarageTester class
class GarageTester:
    @staticmethod
    def get_example():
        truck = Truck("black", False)  # Truck is black and has no trailer
        garage = Garage()
        garage.set_vehicle(truck)
        return garage

# Customer class
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer: {self.name}\nAddress: {self.address}"

# Example usage
if __name__ == "__main__":
    garage = GarageTester.get_example()
    print(garage)

from Garage import Garage
from Truck import Truck


class GarageTester(Garage):
    def __init__(self):
        super().__init__()

    def getExample(self):
        truck = Truck('Brown', False)

        my_garage = Garage()
        my_garage.setVehicle(truck)

        return my_garage.toString()


if __name__ == '__main__':
    print(GarageTester().getExample())

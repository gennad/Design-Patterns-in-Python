class Car:
    def __init__(self):
        self.name = None
        self.km = 11100
        self.fuel = 5
        self.oil = 5


def handle_fuel(car):
    if car.fuel < 10:
        print "added fuel"
        car.fuel = 100


def handle_km(car):
    if car.km > 10000:
        print "made a car test."
        car.km = 0


def handle_oil(car):
    if car.oil < 10:
        print "Added oil"
        car.oil = 100


class Garage:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_car(self, car):
        for handler in self.handlers:
            handler(car)

if __name__ == '__main__':
    handlers = [handle_fuel, handle_km, handle_oil]
    garage = Garage()

    for handle in handlers:
        garage.add_handler(handle)
    garage.handle_car(Car())

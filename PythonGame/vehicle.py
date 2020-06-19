class Vehicle:
    def __init__(self):
        raise NotImplelmentedError("You did not enter a vehicle type.")

    def __str__(self):
        return self.name


class Motorcycle(Vehicle):
    def __init__(self):
        self.name = 'Motorcycle'
        self.wheels = 2

    def __str__(self):
        return self.name

class Car(Vehicle):
    def __init__(self):
        self.name = 'Car'
        self.wheels = 4

    def __str__(self):
        return self.name


print(Vehicle())

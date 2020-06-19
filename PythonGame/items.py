class Consumable:
    def __init__(self):
        raise NotImplelmentedError("Do not create raw Consumable objects")
    def __str__(self):
        return "{} (+{}HP)".format(self.name, self.healing_value)

class Item:
    def __init__(self):
            raise NotImplelmentedError("Do not create raw 'Item' objects.")

    def __str__(self):
        return self.name

class Weapon:
    def __init__(self):
            raise NotImplelmentedError("Do not create raw 'Weapon' objects.")

    def __str__(self):
        return self.name
class Inventory:

    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.item.append(item)

class M4(Weapon):
    def __init__(self):
        self.name = "M4"
        self.description = "Standard issue rifle. You're a Red Hatter, so you won't get any of the 'Cool' guy attachements"
        self.damage = 25

class M240B(Weapon):
    def __init__(self):
        self.name = "M240B"
        self.description = "Heavy Machine Gun. Its big, loud and deadly."
        self.damage = 50

class CarlG(Weapon):
    def __init__(self):
        self.name = "Carl Gustav"
        self.description = "This bad boy can take out a tank, car, house, and even person."
        self.damage = 100

class Vrod(Item):
    def __init__(self):
        self.name = "VROD"
        self.description = "The bread and butter to being a decent Red Hatter"
        self.damage = 0

class NVG(Item):
    def __init__(self):
        self.name = "PVS-15s"
        self.description = "Night Vison googles. Bring extra AA batteries.... " \
        "The night is long and full of terrors."
        self.damage = 0
class Medpak(Consumable):
    def __init__(self):
        self.name = "MedPak"
        self.healing_value = 50

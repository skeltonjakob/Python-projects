import random

class Enemy:
    def __init__(self):
        raise NotImplelmentedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def is_dead(self):
        return self.hp == 0

class Spotter(Enemy):
    def __init__(self):
        self.name = "Spotter"
        self.hp = 50
        self.damage = 10

class Regular(Enemy):
    def __init__(self):
        self.name = "Regular Insurgent"
        self.hp = 100
        self.damage = 20
class RPG(Enemy):
    def __init__(self):
        self.name = "RPG Insurgent"
        self.hp = 100
        self.damage = 30

class HVT(Enemy):
    def __init__(self):
        self.name = "Taliban Leader"
        self.hp = 100
        self.damage = 40

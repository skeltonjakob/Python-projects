import random
import enemies
import player



class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplelmentedError("Create a Subclass instead!")
    def modify_player(self, player):
        pass


class BaseTile(MapTile):

    def intro_text(self):
        return """"
    You find yourself at the epicenter of KAF.... Camp Brown.\

    Looking around, you see the Chow hall, the JOC, the Gym, as well as a shuttle to the Flight Line.

             """
class ChowTile(MapTile):
    def intro_text(self):
        return """
            You decide to head towards the Chow Hall.

            """
class JocTile(MapTile):
    def intro_self(self):
        return """
            You decide to head towards the JOC
            """
class GymTile(MapTile):
    def intro_self(self):
        return """
            You decide to head towards the Gym.
            """

class FLineTile(MapTile):
    def intro_self(self):
        return """
            You decide to take the shuttle for the Flight Line.
            """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Spotter()
            self.alive_text = """A Spotter calls in your postion \n
            He moves closer and fires at you!"""
            self.dead_text = "The Spotter was killed."

        elif r < 0.75:
            self.enemy = enemies.Regular()
            self.alive_text = """An Insurgent jumps out and shoots at you \n
            As he shoots he blocks you path!"""
            self.dead_text = "The dead Insurgent lays on the path."

        elif r < 0.95:
            self.enemy = enemies.RPG()
            self.alive_text = """You hear a rocket whizz by \n
            It's and RPG Insurgent! \n
            Take cover!"""
            self.dead_text = "The RPG Insurgent was finally killed"

        else:
            self.enemy = enemies.HVT()
            self.alive_text = "The Taliban Commander reveals himself and attacks!"
            self.dead_text = "The Taliban Commander has been eliminated."

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The enemy hit you for {} damage. You have {} HP remaining".format(self.enemy.damage, player.hp))




world_map = [
        [None,EnemyTile(1,0),None],
        [GymTile(0,1), BaseTile(1,1),JocTile(2,1)],
        [None,FLineTile(1,2),None],

]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

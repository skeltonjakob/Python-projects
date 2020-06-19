import player
import world

player = Player()
class Locations:
    def __init__(self):
        self.base = ['Flight Line'
                        , 'JOC'
                        , 'Chow Hall'
                        , 'Gym'
                        ,]
        self.map = [
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],

    ]

    def print_base(self):
        if action_input in ['Flight Line', 'f', 'F', 'Flight', 'flight', 'flight line']:
            print('Heading to the {}'.format(self.base[0]))

        elif action_input in ['JOC', 'j', 'J', 'joc', 'Joc']:
            print('Heading to the {}'.format(self.base[1]))

        elif action_input in ['Chow Hall', 'c', 'C', 'chow', 'Chow', 'chow hall']:
            print('Heading to the {}'.format(self.base[2]))

        elif action_input in ['Gym', 'g', 'G', 'gym']:
            print('Heading to the {}'.format(self.base[3]))



class FlightLine(Locations):
    def __init__(self):
        self.name = ['Flight Line', 'f', 'F', 'Flight', 'flight', 'flight line']
        self.description = "All flight operations start here. If it flies, you'll find it here"

class JOC(Locations):
    def __init__(self):
        self.name = ['JOC', 'j', 'J', 'joc', 'Joc']

class ChowHall(Locations):
    def __init__(self):
        self.name = ['Chow Hall', 'c', 'C', 'chow', 'Chow', 'chow hall']

class Gym(Locations):
    def __init__(self):
        self.name = ['Gym', 'g', 'G', 'gym']

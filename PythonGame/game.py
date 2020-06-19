###Code base for the "Escape From Kandahar" choose your own adventure game!###
from player import Player
import world
from collections import OrderedDict

#import locations import Locations
#collection of lists and tuples used throughout the "game.py"
nco_rank = ("PVT"
            ,"PV2"
            , "PFC"
            , "SPC"
            , "SGT"
            , "SSG"
            , "SFC"
            , "MSG"
            , "SGM"
            , "CSM"
            , "SMA")
officer_rank = ("1LT"
                , "2LT"
                , "CPT"
                , "MAJ"
                , "LTC"
                , "COL"
                , "BG"
                , "MG"
                , "LG"
                , "GEN"
                , "GOA")

def play():
    #Begining of the game
    print("""
            ESCAPE  \n
                FROM \n
                    KANDAHAR!
                    """)
    player = Player()
    #Player inputs first and last name
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    rank = {}
    player_name = (first_name, last_name, rank)
    #Player chooses location to go to, prints locations from 'base_locations' list


    #list of actions the player can take
    while True:
        #This is assigning the 'world.py' file to the varible "camp_brown"
        camp_brown = world.tile_at(player.x, player.y)
        print(camp_brown.intro_text())
        #This allows the the enemy to attack the player
        camp_brown.modify_player(player)
        #This allows the player to input commands
        choose_actions(camp_brown, player)
        #action_input = get_actions()
        #if action_input in ['Flight Line', 'f', 'F', 'Flight', 'flight', 'flight line']:
        #    player.move_south()
        #elif action_input in ['JOC', 'j', 'J', 'joc', 'Joc']:
        #    player.move_east()
        #elif action_input in ['Chow Hall', 'c', 'C', 'chow', 'Chow', 'chow hall']:
        #    player.move_north()
        #elif action_input in ['Gym', 'g', 'G', 'gym']:
        #    player.move_west()
        #elif action_input in ['i', 'I', 'inventory', 'Inventory']:
        #    player.print_inventory()
        #elif action_input in ['a', 'A', 'attack', 'Attack']:
        #    player.attack()
        #elif action_input in ['h', 'H', 'heal', 'Heal']:
        #    player.heal()
        #elif action_input in ['None', 'none', 'exit', 'Exit', 'leave', 'Leave']:
        #    print("Classic Red Hatter....Pick a place to go....you're probably going to pick the Chow Hall, Fatty.")
        #else:
            #print("What are you doing Red Hatter?! Pick a location.")



####Functions used within the game.py file
def get_actions(room, player):
    actions = OrderedDict()
    print("Choose an Action: ")
    if player.inventory:
        action_adder(actions, 'I', player.print_inventory, "Print Inventory")
        if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
            action_adder(actions, 'A', player.attack, "Attack")
        else:
            if world.tile_at(room.x, room.y -1):
                action_adder(actions, 'C', player.move_north, "Head to the Chow Hall.")
            if world.tile_at(room.x, room.y +1):
                action_adder(actions, 'F', player.move_south, "Head to the Flight Line.")
            if world.tile_at(room.x +1, room.y):
                action_adder(actions, 'J', player.move_east, "Head to the JOC.")
            if world.tile_at(room.x -1, room.y):
                action_adder(actions, 'G', player.move_west, "Head to the Gym.")
        if player.hp < 100:
            action_adder(actions, 'H', player.heal, "Heal")
        return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {} ".format(hotkey, name))

def choose_actions(camp_brown, player):
    action = None
    while not action:
        available_actions = get_actions(camp_brown, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()

        else:
            print("Classic Red Hatter....Pick a place to go....you're probably going to pick the Chow Hall, Fatty.")




def print_pretty(to_print):
    for item in to_print:
        print("* " + str(item))

def print_ordered(to_print):
    for i in range(len(to_print)):
        print(str(i + 1) + ". " +str(to_print[i]))

def print_enu(to_print):
    for i, value in enumerate(to_print, 1):
        print(str(i) + ". " + str(value))









###PLAY!!!####
play()

#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import monsterfight

def show_instructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
RPG Game
========
Commands:
    go [direction]
    get [item]
    ''')

def show_status():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + CURRENT_ROOM)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[CURRENT_ROOM]:
        print('You see a ' + rooms[CURRENT_ROOM]['item'])
    if "trapdoor" in rooms[CURRENT_ROOM]:
        print(rooms[CURRENT_ROOM]['trapdoor'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'west'  : 'Dungeon',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },
            'Dungeon' : {
                  'south' : 'Armory',
                  'item'  : 'monster',
                  'trapdoor' : "Door shut behind you, you cannot return to the hall"
            },
            'Armory'  : {
                  'east'  : 'Kitchen',
                  'north' : 'Dungeon',
                  'item'  : 'sword'
            },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'north' : 'Dining Room'
            }
         }

# monster count
MONSTER = 2

# start the player in the Hall
CURRENT_ROOM = 'Hall'

# show instructions
show_instructions()

# breaking this while loop means the game is over
while True:
    show_status()

    # the player MUST type something in
    # otherwise input will keep asking
    MOVE = ''
    while MOVE == '':
        MOVE = input('>>> ')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    MOVE = MOVE.lower().split(" ", 1)

    #if they type 'go' first
    if MOVE[0] == 'go':
        #check that they are allowed wherever they want to go
        if MOVE[1] in rooms[CURRENT_ROOM]:
            #set the current room to the new room
            CURRENT_ROOM = rooms[CURRENT_ROOM][MOVE[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if MOVE[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[CURRENT_ROOM] and MOVE[1] in rooms[CURRENT_ROOM]['item']:
            #add the item to their inventory
            inventory.append(MOVE[1])
            #display a helpful message
            print(MOVE[1] + ' aquired')
            #delete the item key:value pair from the room's dictionary
            del rooms[CURRENT_ROOM]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + MOVE[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[CURRENT_ROOM] and 'monster' in rooms[CURRENT_ROOM]['item']:
        print("Monster encountered.")
        # Start fight
        X = ''
        X = monsterfight.fight(X)
        if 'sword' in inventory:
            print("You have a sword, which helps you kill the monster")
            del rooms[CURRENT_ROOM]['item']
            MONSTER -= 1
        elif X == 'winner':
            print("Monster killed.")
            del rooms[CURRENT_ROOM]['item']
            MONSTER -= 1
        elif X == 'dead':
            break
        else:
            print("You have the option to flee, or return to kill the monster.")

    ## Define how a player can win
    if CURRENT_ROOM == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If all monsters are dead
    if MONSTER == 0:
        print('You killed all the monsters. YOU WIN!')
        break

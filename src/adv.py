from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Tom', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
command = None

while not command == 'q':
    # Room where player is at
    print(f"\n{player.name} is at: {player.current_room.name}\n")

    # Description of room where player is at
    wrapper = textwrap.TextWrapper(width=50)
    description = wrapper.wrap(text=player.current_room.description)
    print("description:")
    for line in description:
        print(line)

    # list of items present in the room where player is at
    print('\nitems in this room:')
    for item in player.current_room.items:
        print(item.name)
    print("************")

    # linking user input to possible direction from the player current room
    to_room = {
        'n': player.current_room.n_to,
        's': player.current_room.s_to,
        'e': player.current_room.e_to,
        'w': player.current_room.w_to,
    }

# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# if the user enters "q", quit the game.

    command = input(
        "enter directions: (n)orth, (s)outh, (e)ast, (w)est\n"
        "choose action: get/take item, drop item\n"
        "or (q)uit: "
    ).split('')

    # change all commands to lower case
    if command in ['n', 's', 'e', 'w']:
        if(to_room[command] == None):
            print("\nMOVE NOT ALLOWED. TRY AGAIN..")
        else:
            player.current_room = to_room[command]

    # If the user enters "q", quit the game.

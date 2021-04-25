def show_instructions():
    # print a main menu and the commands

    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("-----------------------------------")


def main():
    show_instructions()


rooms = {'Great Hall': {'South': 'Bedroom', 'North': 'Dungeon', 'East': 'Kitchen', 'item': 'Dragon'},
         'Cellar': {'West': 'library', 'item': None},
         'Gallery': {'South': 'Kitchen', 'North': 'library', 'West': 'Bedroom', 'East': 'Father Room',
                     'item': 'Rope'},
         'library': {'South': 'Gallery', 'item': 'Secret passage'},
         'Kitchen': {'East': 'Great Hall', 'North': 'Gallery', 'item': 'Water Tank'},
         'Father Room': {'West': 'Gallery', 'item': 'Ring'},
         'Bedroom': {'East': 'Gallery', 'item': 'Sword'},
         'Dungeon': {'East': 'Gallery', 'item': 'Shield'},
         'Garden': {'West': 'Gallery', 'item': 'Armor'}
         }

# Starting room
current_room = 'Gallery'
# List to store collected items
inventory = []

# Loop to simulate moves between rooms based on the user input
while True:
    # If current_room is Dining Room then breaking the loop
    if current_room == 'Dining Room':
        print("\nYou are in the", current_room)
        print("You see a Dragon!", )
        if len(inventory) == 6:
            print("\nCongrats! You have all items and won against dragon!")
        else:
            print("\nNOM NOM...GAME OVER!")
        break

    # Printing current_room
    print("\nYou are in the", current_room)

    # Taking user opinion to pick the item or not
    if rooms[current_room]['item'] != None:
        print("You see a", rooms[current_room]['item'])
        opinion = input("get " + rooms[current_room]['item'] + "?(Y/N): ").upper()
        # Validating user input
        while opinion not in ['Y', 'N']:
            print("Invalid input. Try again")
            opinion = input("Get " + rooms[current_room]['item'] + "?(Y/N): ").upper()
        if opinion == 'Y':
            inventory.append(rooms[current_room]['item'])
            rooms[current_room]['item'] = None
    else:
        print("Already item collected or nothing in this room")

    # Printing inventory
    print("Inventory:", inventory)

    # Taking user input for direction to move
    direction = input("Direction to move?(East,West,North,South): ").title()
    directions = list(rooms[current_room].keys())
    directions.remove('item')
    # Validating direction
    while direction not in directions:
        print("Invalid direction from " + current_room + ". Try again")
        direction = input("Direction to move?(East,West,North,South): ").title()

    # Setting next_room
    next_room = rooms[current_room][direction]
    print("You have just moved to", next_room)
    print("------------------------------------------------")

    # Updating current_room
    current_room = next_room

# Printing end message
print("\nThanks for playing the game. Hope you enjoyed it.")

# Calling main function




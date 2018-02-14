def get_direction(letter):
    letter = letter.lower()
    if letter == "n":
        return "north"
    elif letter == "e":
        return "east"
    elif letter == "s":
        return "south"
    elif letter == "w":
        return "west"

def print_instructions():
    print("""
How to play:

Press 'n' to move north.
Press 'e' to move east.
Press 's' to move south.
Press 'w' to move west.
Press 'i' to view instructions.
Press 'q' to quit the game.
    """)

ROOMS = (
    # Stucture:
    # (
    #     description,
    #     north of, east of, south of, west of
    # )
    (
        "You're in the second bedroom. The door to the south hall is on the right, and the first bed room is northwards.",
        3, 1, None, None
    ),
    (
        "You're in the south hall. You see a bedroom on your left, the north hall in front of you, and the dining room to your right.",
        4, 2, 8, 0
    ),
    (
        "You're in the dining room. There's a hall to your left. You smell food coming from the kitchen front of you.",
        5, None, None, 1
    ),
    (
        "You're in the first bedroom. Behind you, there is another bedroom. To your right, there is an empty hall.",
        None, 4, 0, None
    ),
    (
        "You're in the north hall. You can walk a bit north and look out the balcony, to the right and eat some food from the kitchen, south to go into the other hall, and left to go to sleep in the first bedroom.",
        6, 5, 1, 3
    ),
    (
        "You're in the kitchen. To the left, there is the north hall, and to the south, there is the dining room.",
        None, 7, 2, 4
    ),
    (
        "You're at the balcony. You can't jump off ;), but you can head southwards into the north hall.",
        None, None, 4, None
    ),
    (
        "You're in the garden now and there's a lot of trees. You can head westwards and go back into the kitchen.",
        None, None, None, 5
    ),
    (
        "You're in the front lawn. Nothing much has happened there! You can head north and back into the house.",
        1, None, None, None
    )
)
current_room = 0
done = False

print("""
Welcome to Victor's Adventure Game!
""")
print_instructions()

while not done:
    print()
    # Print description of room
    print(ROOMS[current_room][0])

    choice = input("Which direction do you want to head into? ")
    choice = choice.lower()

    # Check user choice and perform appropriate actions
    if choice == "n":
        next_room = ROOMS[current_room][1]
    elif choice == "e":
        next_room = ROOMS[current_room][2]
    elif choice == "s":
        next_room = ROOMS[current_room][3]
    elif choice == "w":
        next_room = ROOMS[current_room][4]
    elif choice == "i":
        print_instructions()
        continue
    elif choice == "q":
        print("You decided to abort the adventure. Bye!")
        done = True
        continue
    else:
        print("This doesn't seem to be valid!")
        continue

    # Check if the next room is accessible
    if next_room is None:
        print("There's no place to go in that direction. Can't move there!")
    else:
        current_room = next_room
        print("You moved " + get_direction(choice) + "!")
import random

done = False
player = {
    "camel_tiredness": 0,
    "player_dead": False,
    "player_thirst": 0,
    "total_canteens": 5,
    "total_drank": 0,
    "total_traveled": 0
}
native = {
    # Natives are 20 miles back initially
    "total_traveled": -20
}

def drink_from_canteen():
    if player["total_canteens"] == 0:
        print("You have no more canteens!")
    else:
        player["total_canteens"] -= 1
        player["player_thirst"] = 0
        print("You drank from one of your canteens. Your thirst has been quenched!")

def get_distance_between():
    """
    Calculates the distance between the player and the natives.
    If the returned value is <= 0, the player has been caught up with.
    """
    distance = player["total_traveled"] - native["total_traveled"]
    return distance

def handle_user_choice(choice):
    global done
    choice = choice.upper()

    if choice == "A":
        drink_from_canteen()
        pass
    elif choice == "B":
        move_ahead("player", "moderate")
        pass
    elif choice == "C":
        move_ahead("player", "full")
        pass
    elif choice == "D":
        rest()
        pass
    elif choice == "E":
        print_status()
    elif choice == "Q":
        done = True
    else:
        print("Not a valid choice!")

def move_ahead(who, level = "moderate"):
    """
    Moves either the player or natives ahead
    """
    who = who.lower()
    level = level.lower()

    # Player
    if who == "player":
        # Full speed
        if level == "full":
            to_move = random.randint(10, 21)
            player["total_traveled"] += to_move
            player["player_thirst"] += 1
            player["camel_tiredness"] += random.randint(1, 4)
            move_ahead("native")
            print("Moved forward " + str(to_move) + " miles.")
        # Moderate speed
        else:
            to_move = random.randint(5, 13)
            player["total_traveled"] += to_move
            player["player_thirst"] += 1
            player["camel_tiredness"] += 1
            move_ahead("native")
            print("Moved forward " + str(to_move) + " miles.")

        # 1/20 chance of finding an oasis
        if random.randint(0, 100) < 5:
            print("You've found an oasis! You refilled your canteen, quenched your thirst, and your camel is rested.")
            player["total_canteens"] = 5
            player["player_thirst"] = 0
            player["camel_tiredness"] = 0
    # Natives
    else:
        native["total_traveled"] += random.randint(7, 15)

def notify_user():
    global done

    player_thirst = player["player_thirst"]
    if player_thirst > 6:
        print("You died of thirst!")
        player["player_dead"] = True
        done = True
    elif player_thirst > 4:
        print("You are thirsty.")

    camel_tiredness = player["camel_tiredness"]
    if camel_tiredness > 8:
        print("Your camel is dead.")
        done = True
    elif camel_tiredness > 5:
        print("Your camel is getting tired.")

    distance_between = get_distance_between()
    if distance_between <= 0:
        print("You've been caught by the natives.")
        done = True
    elif distance_between < 15:
        print("The natives are getting close!")

    if player["total_traveled"] >= 200 and not player["player_dead"]:
        print("You've escaped and are alive! You win!")
        done = True

def print_status():
    message = """
Miles traveled: {miles}
Drinks in canteen: {drinks}
The natives are {miles_ahead} mile(s) behind you.
    """
    message = message.format(
        miles = player["total_traveled"],
        drinks = player["total_canteens"],
        miles_ahead = get_distance_between()
    )

    print(message)

def prompt_user():
    """
    Prompts user for choice and returns it in uppercased form
    """
    print("""
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit
    """)
    user_choice = raw_input("Your choice? ")
    return user_choice.upper()

def rest():
    """
    Rests player's camel and moves natives up 7 <= x <= 14
    """
    player["camel_tiredness"] = 0
    print("The camel is happy.")
    move_ahead("native")

# Print introduction
print("""
Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives.
""")
# Main game loop, captures user input
while not done:
    user_choice = prompt_user()
    handle_user_choice(user_choice)
    notify_user()
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy - you win!")
        exit(0)
    else:
        dead("You clown! You've triggered a booby trap!")


def bear_room():
    print("There's a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How will you get the bear to move?")
    print("Your options are TAKE HONEY, TAUNT BEAR, and OPEN DOOR.")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "TAKE HONEY":
            dead("The bear looks at you, then claws your eyes out.")
        elif choice == "TAUNT BEAR" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "TAUNT BEAR" and bear_moved:
            dead("The bear loses its patience and chews your leg off.")
        elif choice == "OPEN DOOR" and bear_moved:
            gold_room()
        else:
            print("Command not recognized. Try again.")

def kos_room():
    print("Here you see the Orphan of Kos, materializing from a withered corpse.")
    print("It stares at you... you begin to go insane.")
    print("Do you FLEE for your life or eat your HEAD?")

    choice = input("> ")

    if "FLEE" in choice:
        start()
    elif "HEAD" in choice:
        dead("Delicious...")
    else:
        kos_room()

        
def dead(why):
    print(why, "Game over!")
    exit(0)

def start():
    print("You are in a dark, dark room.")
    print("There is a door to your RIGHT and another to your LEFT.")
    print("Which door will you take?")

    choice = input("> ")

    if choice == "LEFT":
        bear_room()
    elif choice == "RIGHT":
        kos_room()
    else:
        dead("You stumble around until you starve to death.")


start()
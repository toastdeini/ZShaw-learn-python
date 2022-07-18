from sys import exit

player_health = 50
melee_damage = 5
axe_damage = 50

def start():
    print("'...Where am I?'")
    print("You awaken on a hospital bed in a dimly lit clinic.")
    print("Your torso is bandaged, but you don't recall being injured.")
    print("What's your next move?")
    print("\t1. Leave through the unlocked door.")
    print("\t2. Climb out the window, which is cracked open slightly.")
    print("(Input 1 or 2, then press ENTER)")

    choice = input("> ")
    choice = int(choice)

    if choice == 1:
        wolf_room()
    elif choice == 2:
        rooftop()
    else:
        print("Command not recognized - try again.")
        start()


def wolf_room():
    print("Passing into the next room, you notice a wolf-like beast...")
    print("...who appears to be feasting on a bloodied corpse.")
    print("You try to keep quiet, but a squeaky floorboard gives you away.")
    print("The beast turns to face you. It has picked up your scent.")
    print("\t1. Run like hell.")
    print("\t2. Grab an axe off the wall and fight.")

    wolf_alive = True
    wolf_health = 100

    choice = input("> ")
    choice = int(choice)   

    if choice == 1:
        print("The wolf catches up to you and starts gnawing at your leg.")
        player_health -= 25
        print("Your foot's been torn off, but you can still hobble.")
        print("\t1. Keep it moving - you still have a chance.")
    elif choice == 2:
        print("You snatch the axe and grip it with two hands.")     


def rooftop():
    print("You exit through the window and find yourself on a rooftop.")
    print("An unidentifiable, humanoid creature is patrolling.")
    print("It has tentacles around its mouth and no eyes.")
    print("\t1. Sneak along the ledge.")
    print("\t2. Approach the creature.")

    brainsucker_alive = True
    brainsucker_health = 10

    choice = input("> ")
    choice = int(choice)

    if choice == 1:
        print("After tiptoeing past several windows, you find one")
        print("that's open. You enter - the hallway is dark, but")
        print("there's a light in the distance. With nowhere else")
        print("to go, you walk toward the light.\n")
        lantern_room()
    elif choice == 2:
        print("With trepidation, you start walking toward the creature...")
        print("...which turns its head to meet your gaze and hisses.")
        print("\t1. Take it slow... let it come to you.")
        print("\t2. Pounce on it. Now or never.")

        sub_choice = input("> ")
        sub_choice = int(sub_choice)

        if sub_choice == 1:
            print("The creature's tentacles extend from its face")
            print("and constrict your neck.")
            dead("The creature sucks out your brain.")
        elif sub_choice == 2:
            print("You lunge for the creature. You attempt to grab it by")
            print("its neck, but it clasps your skull in its palms.")
            print("\t1. Shove your fist in the creature's mouth.")
            print("\t2. Tear off one of its mouth tentacles.")

            fight_choice = input("> ")
            fight_choice = int(fight_choice)

            if fight_choice == 1:
                print()
            elif fight_choice == 2:
                print()
            else:
                print("The creature senses your incompetence.")
                dead("From yards away, it sucks out your brain.")                

        else:
            print("The creature senses your incompetence.")
            dead("From yards away, it sucks out your brain.")
    else:
        print("The creature senses your incompetence.")
        dead("From yards away, it sucks out your brain.")


def lantern_room():
    print("Turns out you're not alone...")
    print("It has the torso, the legs, the shape of a human... but it")
    print("has a disgusting, tumor-like blob where a human head would")
    print("be...")
    print("\t1. Walk toward it... slowly...")
    print("\t2. Get outta there!""")

    choice = input("> ")
    choice = int(choice)

    if choice == 1:
        print("As you get closer, you get light-headed.")
        print("Not long after, you find yourself unable to walk.")
        print("Wounds materialize on your body, seemingly")
        print("out of nowhere.")
        dead("Your blood starts gushing out like river rapids.")
    elif choice == 2:
        print("The vile, mutated creature turns its awful head to you.")
        print("Its gaze pierces your skull.")
        dead("You collapse into a pool of your own blood.")
    else:
        print("Crippled with indecision, you begin to go mad.")
        print("Hearing your screams, the creature turns to face you.")
        dead("An arrow-like projectile pierces your skull.")

def dead(cause):
    print(cause, "\nGAME OVER!")
    exit(0)

start()
import time
def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(1)
    print("Do you dare to enter?")
    time.sleep(1)
    print("Type 'yes' to enter the cave or 'no' to run away.")
    choice = input("What will you do? ").lower()
    if choice == 'yes':
        cave()
    elif choice == 'no':
        print("You're too scared to enter. Game Over!")
    else:
        print("Invalid choice. Please try again.")
        intro()


def cave():
    print("You enter the cave and find yourself in a dimly lit tunnel.")
    time.sleep(1)
    print("You see two paths ahead. One is narrow and winding, the other is wide and straight.")
    time.sleep(1)
    print("Which path will you take?")
    time.sleep(1)
    print("Type 'narrow' for the narrow path or 'wide' for the wide path.")
    choice = input("What will you do? ").lower()
    if choice == 'narrow':
        narrow_path()
    elif choice == 'wide':
        wide_path()
    else:
        print("Invalid choice. Please try again.")
        cave()

def narrow_path():
    print("You chose the narrow path.")
    time.sleep(1)
    print("You continue down the path cautiously.")
    time.sleep(1)
    print("Suddenly, you trip over a loose rock and fall into a pit!")
    time.sleep(1)
    print("You're trapped. Game Over!")

def wide_path():
    print("You chose the wide path.")
    time.sleep(1)
    print("You walk confidently down the path.")
    time.sleep(1)
    print("You come across a fork in the road.")
    time.sleep(1)
    print("Do you go left or right?")
    time.sleep(1)
    print("Type 'left' to go left or 'right' to go right.")
    choice = input("What will you do? ").lower()
    if choice == 'left':
        print("You chose to go left.")
        treasure_room()
    elif choice == 'right':
        print("You chose to go right.")
        trap_room()
    else:
        print("Invalid choice. Please try again.")
        wide_path()

def treasure_room():
    print("You enter a room filled with treasure!")
    time.sleep(1)
    print("Congratulations! You've won the game.")

def trap_room():
    print("You enter a room and suddenly the floor gives way beneath you!")
    time.sleep(1)
    print("You fall into a pit of spikes. Game Over!")

# Start the game
intro()

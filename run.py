"""
Dream Mansion - a text based game
"""
# Import Statement for Events, Items and Endings
from game_classes import Event,  Item, Ending

# Stats of the player character
class samurai:
    def __init__(self, constitution, focus, luck, inventory, status):
        self.constitution = 5
        self.focus = 5
        self.luck = 5
        self.inventory = []
        self.status = 

# Status of charater, determines used interface
GAME_STATUS = False
CURRENT_STATUS = "inRoom"

# Inventory List

INVENTORY = []

print("...")
print("...")
print("I'm so tired...")
print("...")
print("...")
initiate_game = input("Do you want to wake up? (Yes = 1; No = 0)")
if initiate_game == "0":
    print("...")
    print("...")
    print("You close your eyes, one last time...")
elif initiate_game == "1":
    print("...")
    print("...")
    print("You wake up in an unknown location...")
    print("...")
    print("...")
    True


# Menu for interacting in rooms
def room_menu():
    print("You are in the 'filler text'")
    print("1. Investigate")
    print("2. Perceive")
    print("3. Rearrange")
    print("0: Change rooms")


def investigate():
    print("You carefully investigate the room...")


def perceive():
    print("You perceive your surroundings, trying to gather information...")


def rearrange():
    print("You rearrange items in the room, looking for hidden clues...")


def change_rooms():
    print("You head to another room...")
    print("You enter...")


while True:
    if CURRENT_STATUS == "inRoom":
        room_menu()
        choice = input("Enter your choice (0-3): ")
        if choice == '0':
            change_rooms()
        elif choice == '1':
            investigate()
        elif choice == '2':
            perceive()
        elif choice == '3':
            rearrange()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

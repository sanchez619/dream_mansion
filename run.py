"""
Dream Mansion - a text based game
"""
class samurai:
    def __init__(self, constitution, focus, luck, inventory):
        self.constitution = 5
        self.focus = 5
        self.luck = 5
        self.inventory = []

    def display_stat(self):
        """
        Displays the character's status and inventory
        """
        print(f"constitution: {self.constitution}")
        print(f"focus: {self.focus}")
        print(f"luck: {self.luck}")
        print(f"inventory: {self.inventory}")

GAME_STATUS = False
CURRENT_STATUS = "inRoom"

INVENTORY = []

def investigate():
    print("You carefully investigate the room...")


def perceive():
    print("You perceive your surroundings, trying to gather information...")


def rearrange():
    print("You rearrange items in the room, looking for hidden clues...")


def change_rooms():
    print("You head to another room...")
    print("You enter...")

def error_input():
    print("Invalid choice. Please enter a number between 1 and 3.")

# Menu for interacting in rooms
def room_menu():
    print("You are in the 'filler text'")
    print("1. Investigate")
    print("2. Perceive")
    print("3. Rearrange")
    print("0: Change rooms")
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
        error_input()
    return choice


def start_floor1():
    choice = room_menu()
    if choice == '1':
        print("As you look around the lobby, you find a small book.")
        print("It says 'Musashi's Diary'.")
        print("Added 'Musashi's Diary' to your inventory.")
    elif choice == '2':
        print("The voices you hear get louder. They say:'Give in, you cannot escape...'")
        print("Focus was lowered by 1.")
    elif choice == '3':
        print("As you move the cupboard, you find a worn-out spear behind it.")
        print("Added 'spear' to inventory.")
    else:
        error_input()

    

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
    start_floor1()
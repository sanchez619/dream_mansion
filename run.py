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
    room_menu()

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
    print("Several doors appear in front of you.")
    print("Which one do you want to enter")
    print("1. The Lounge")
    print("2. The Storage Chamber")
    print("3. The Floor Lobby")
    room_choice = input("Enter your choice (1-3): ")
    if room_choice == '1':
        lounge()
    elif room_choice == '2':
        storage_chamber()
    elif room_choice == '3':
        floor_lobby3()

def lounge():
    print("You enter the floor lobby.")
    print("It contains multiple cupboards.")
    print("They once seemed to contain many different items.")
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

def storage_chamber():
    print("You enter the storage chamber.")
    print("Someone took all consumable items.")
    choice = room_menu()
    if choice == '1':
        print("As you try to inspect the room further, you hear something.")
        print("Lowered focus by 1.")
        print("Luck was increased by 1.")
    elif choice == '2':
        print("The voices you hear get louder. They say:'Give in, you cannot escape...'")
        print("Focus was raised by 2.")
    elif choice == '3':
        print("As you move the cupboard, you find a worn-out spear behind it.")
        print("Constitution was lowered by 3.")
    else:
        error_input()

def floor_lobby3():
    print("You enter the floor lobby.")
    print("As you enter, you see a door leading to a spiraling stairway.")
    choice = room_menu()
    if choice == '1':
        print("As you try to go down the stairs, you hear a voice.")
        print("'Those without identity cannot pass!'")
        print("'Who are you?'")
        solution_1 = input ("I am a...")
        if solution_1 == "samurai":
            print("The powers cannot hold you anymore.")
            print("You descend to the first floor.")
            start_floor2()
        else:
            print("'That is incorrect!'")
            print("'Turn back to the shadows where thou came from!'")
    elif choice == '2':
        print("This room is filled with malice.")
        print("You should not do anything unnecessary")
        print("Luck was increased by 1.")
    elif choice == '3':
        print("You try to move the couch when your leg suddenly starts hurting.")
        print("You have stepped into a beartrap.")
        print("Constitution was decreased by 2")
        print("Luck was decreased by 1")
    else:
        error_input()

def start_floor2():
    print()
    print()
    print("The second floor has an even more ominous feeling.")
    print("This most likely has to do with the large figure.")
    print("It stands at the end of the corridor, waiting...")
    print()
    print()
    print("Which room do you want to enter?")
    print("1. The Gym")
    print("2. The Office")
    print("3. The Bathroom")
    print("4. End of the Corridor")
    room_choice = input("Enter your choice (1-3): ")
    if room_choice == '1':
        gym()
    elif room_choice == '2':
        office()
    elif room_choice == '3':
        bathroom()
    elif room_choice == '4':
        second_floor_boss()
    else:
        error_input

def gym():
    print("You enter the gym.")
    print("Before you can see anything else, a demon appears in front of you!")
    choice = room_menu()
    if choice == '1':
        print("You try finding something to help against the demon.")
        print("However, you cannot spot something in that instance.")
    elif choice == '2':
        print("But before you can even react, the demon strikes you in the head.")
        print("Constitution was decreased by 3")
    elif choice == '3':
        print("You throw a small cupboard in-between you and the demon.")
        print("You ready your weapon as you realize:'He's gone'.")
        print("Instead, you find some bandages, which fell out of the cupboard.")
        print("Constitution was increased by 2.")
    else:
        error_input()

def bathroom():
    print("You enter the bathroom.")
    print("This room is actually lit. You can see the bathtub filled with water.")
    choice = room_menu()
    if choice == '1':
        print("Next to the bathtub is another cupboard.")
        print("In one of the drawers, you find a small book.")
        print("Added 'Fighting demons 101' to your inventory.")
    elif choice == '2':
        print("You feel that the room is devoid of malice.")
        print("You choose to enter the bath and relax")
        print("Constitution was raised by 2")
        print("Luck was raised by 1")
    elif choice == '3':
        print("You throw a small cupboard in-between you and the demon.")
        print("You ready your weapon as you realize:'He's gone'.")
        print("Instead, you find some bandages, which fell out of the cupboard.")
        print("Constitution was increased by 2.")
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
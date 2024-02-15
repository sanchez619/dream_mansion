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

def fight_menu():
    print("You are engaged in a fight.'")
    print("From where do you want to strike?")
    print("1. Strike from above")
    print("2. Strike from left flank")
    print("3. Strike from right flank")
    print("0: Strike from below")
    strike_direction = input("Enter your choice (0-3): ")
    return strike_direction

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
    room_choice = input("Enter your choice (1-4): ")
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

def office():
    print("You enter the office.")
    print("A dark figure sits on a chair behind the desk.")
    choice = room_menu()
    if choice == '1':
        print("You ascertain whether the figure is actually a demon.")
        print("You find that it is only a coat on the chair.")
        print("Focus was decreased by 1.")
        print("Luck was raised by 1.")
    elif choice == '2':
        print("Just as you start listening to your surroundings...")
        print("A dagger pierces your right chest!")
        print("Constitution was decreased by 2")
    elif choice == '3':
        print("You throw a coat rack, which was right next to the door...")
        print("directly in the direction of the chair.")
        print("You hear a terrifying cry.")
        print("Focus was decreased by 2.")
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
        print("Constitution was raised by 2.")
    else:
        error_input()

def second_floor_boss():
    print("You engage a terrifying monster.")
    strike_direction = fight_menu()
    if strike_direction == '0':
        print("You have hit the enemy's weak spot.")
        start_floor3()
    elif strike_direction == '1':
        print("Just before your blade hits...")
        second_floor_gameover()
    elif strike_direction == '2':
        print("Just before your blade hits...")
        second_floor_gameover()
    elif strike_direction == '3':
        print("Just before your blade hits...")
        second_floor_gameover()
    else:
        print("You were too slow to react!")
        second_floor_gameover()

def start_floor3():
    print()
    print()
    print("You arrive at the first floor.")
    print("You feel an overwhelming maelstrom from all directions.")
    print("No place here is safe.")
    print()
    print()
    print("Which room do you want to enter?")
    print("1. The Kitchen")
    print("2. The Living Room")
    print("3. The Guest Room")
    print("4. The Bed Room")
    print("5. The Closet")
    print("6. The Exit")
    room_choice = input("Enter your choice (1-6): ")
    if room_choice == '1':
        kitchen()
    elif room_choice == '2':
        living_room()
    elif room_choice == '3':
        guest_room()
    elif room_choice == '4':
        bed_room()
    elif room_choice == '5':
        closet()
    elif room_choice == '4':
        final_room()
    else:
        error_input

def kitchen():
    print("You enter the kitchen.")
    print("You see a demon eating something red on a plate.")
    print("It has not seen you yet.")
    choice = room_menu()
    if choice == '1':
        print("You find a note.")
        print("It says: 'Keep important things close to your chest.'")
        print("The demon notices you and attacks!")
        print("Focus was decreased by 1")
    elif choice == '2':
        print("You feel the demon's greed for blood.")
        print("He is too entranced to notice you.")
        print("You approach him from behind and slice his throat.")
        print("Luck was raised by 1")
    elif choice == '3':
        print("You try to flip the table onto the demon.")
        print("It is too heavy, and you cannot.")
        print("In the meantime, the demon jumps you!")
        print("Constitution was decreased by 2.")
    else:
        error_input()

def living_room():
    print("You enter the living room.")
    print("It is dark, and you can find nothing of note.")
    print("A radio is placed on a table. It is turned on.")
    choice = room_menu()
    if choice == '1':
        print("On the table, you find some beer bottles.")
        print("You take one that is not empty and drink it.")
        print("Constitution was raised by 1.")
        print("Focus was decreased by 1")
    elif choice == '2':
        print("You listen more closely to the radio.")
        print("Thousands of voices tell you to give in.")
        print("Your mind becomes foggier.")
        print("Focus was decreased by 1.")
    elif choice == '3':
        print("You rearrange the furniture, looking for clues.")
        print("After 15 minutes of dragging large objects, you give up.")
        print("Luck was decreased by 1.")
    else:
        error_input()

def guest_room():
    print("You enter the guest room.")
    print("Something is lurking under the bed sheet.")
    print("You can see two bumps.")
    choice = room_menu()
    if choice == '1':
        print("You pull the sheet from the bed.")
        print("A demon was hidden under the sheet!")
        print("It uses the opportunity to jump you.")
        print("Constitution was decreased by 2")
    elif choice == '2':
        print("You hear a musical box. You decide to turn up the volume.")
        print("The demon under the bed falls asleep.")
        print("You then cleanly slice its neck.")
        print("Focus was raised by 1.")
    elif choice == '3':
        print("You lever the mattress to the right.")
        print("You hear a loud thud. It sounded like someone fell to the floor.")
        print("As you ready yourself, a demon approaches you.")
        print("Luck was decreased by 1.")
    else:
        error_input()

def bed_room():
    print("You enter the bed room.")
    print("You see a silver briefcase lying on the bed.")
    print("Faint voices can be heard.")
    choice = room_menu()
    if choice == '1':
        print("You open the briefcase.")
        print("You find a bottle of sake and a shortsword.")
        print("A note lies next to it.")
        print("Added 'Wakizashi' to inventory.")
        print("Added 'Seppuku Instructions' to inventory.")
    elif choice == '2':
        print("The voices become stronger!")
        print("Why? Why?? Why couldn't you SAVE US???")
        print("You feel as if your head is about to explode.")
        print("Focus was decreased by 2.")
    elif choice == '3':
        print("As you try to push the closet away, it buckles.")
        print("You are buried under the closet.")
        print("You can barely escape your grave.")
        print("Luck was decreased by 2.")
        print("Constitution was decreased by 1.")
    else:
        error_input()

def closet():
    print("There is nothing in the room.")
    print("It is completely empty...")
    print("As you were about to leave the room")
    print("You see something written on the wall:")
    print()
    print("DO NOT FEAR ...!!!")
    print("DO FEAR LIVING AS A PUPPET!!!")
    print()
    print("One word is stained with blood.")
    print("You cannot decipher it.")

def game_start():
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

game_start()
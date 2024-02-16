"""
Dream Mansion - a text based game
"""

#Main Class - Containts player's starting stats
class samurai:
    def __init__(self, constitution, focus, luck, inventory):
        self.constitution = constitution
        self.focus = focus
        self.luck = luck
        self.inventory = inventory

    def display_stat(self):
        """
        Displays the character's status and inventory
        """
        print(f"Constitution: {self.constitution}")
        print(f"Focus: {self.focus}")
        print(f"Luck: {self.luck}")
        print(f"Inventory: {self.inventory}")

    def decrease_stat(self, stat, number):
        """
        Decreases the characters stats after certain events
        """
        if stat == 'constitution':
            self.constitution -= number
        elif stat == 'focus':
            self.focus -= number
        elif stat == 'luck':
            self.luck -= number
        else:
            print("Stat change not valid!")

    def raise_stat(self, stat, number):
        """
        Raises the characters stats after certain events
        """
        if stat == 'constitution':
            self.constitution += number
        elif stat == 'focus':
            self.focus += number
        elif stat == 'luck':
            self.luck += number
        else:
            print("Stat change not valid!")

    def check_stats(self):
        """
        Checks whether one of the player's stats are either 0 or below.
        Triggers Game Over text.
        """
        if self.constitution <= 0:
            print("Constitution Game Over")
        elif self.focus <= 0:
            print("Focus Game Over")
        elif self.luck <= 0:
            print("Luck Game Over")


#Creates a player based on samurai class
player = samurai(constitution = 5, focus = 5, luck = 5, inventory = [])

CHOICES_MADE = set()
IN_ROOM = True

def investigate():
    print("You carefully investigate the room...")


def perceive():
    print("You perceive your surroundings, trying to gather information...")


def rearrange():
    print("You rearrange items in the room, looking for hidden clues...")

def redundant_choice():
    print("You have already taken this action.")
    print("You will not find anything new repeating it.")

def redundant_choice2():
    print("You do not feel an enemy presence anymore.")
    print("There is nothing more to find here...")

def redundant_choice3():
    print("You have already used up the bathroom with your actions.")
    print("Hopefully, you haven't broken it...")

def error_input():
    print("Invalid choice. Please enter a number indicating one of the rooms.")

def second_floor_gameover():
    print("You feel a large object piercing your throat.")
    print("You desperately try to breathe, but the...")
    print(...)
    print(...)
    print("Can't... move...")
    print(...)
    print(...)

# Menu for interacting in rooms
def room_menu():
    print("You are in the 'filler text'")
    print("1. Investigate")
    print("2. Perceive")
    print("3. Rearrange")
    print("4: Change rooms")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        investigate()
    elif choice == '2':
        perceive()
    elif choice == '3':
        rearrange()
    return choice

def fight_menu():
    print("You are engaged in a fight.'")
    print("From where do you want to strike?")
    print("1. Strike from above")
    print("2. Strike from left flank")
    print("3. Strike from right flank")
    print("4: Strike from below")
    strike_direction = input("Enter your choice (1-4): ")
    return strike_direction

# Functions for main story
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
    else:
        error_input()

"""
Lounge Room - on Floor Three (Each event can be triggered)
"""
def lounge():
    print("You enter the floor lobby.")
    print("It contains multiple cupboards.")
    print("They once seemed to contain many different items.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            if 'diary' not in CHOICES_MADE:
                print("As you look around the lobby, you find a small book.")
                print("It says 'Musashi's Diary'.")
                print("Added 'Musashi's Diary' to your inventory.")
                CHOICES_MADE.add('diary')
            else:
                redundant_choice()
        elif choice == '2':
            if 'lounge_voices' not in CHOICES_MADE:
                print("The voices you hear get louder. They say:'Give in, you cannot escape...'")
                print("Focus was lowered by 1.")
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('lounge_voices')
            else:
                redundant_choice()
        elif choice == '3':
            if 'spear' not in CHOICES_MADE:
                print("As you move the cupboard, you find a worn-out spear behind it.")
                print("Added 'Spear' to inventory.")
                CHOICES_MADE.add('spear')
            else:
                redundant_choice()
        elif choice == '4':
            IN_ROOM = False
            start_floor1()
            break
        else:
            error_input()


"""
Storage Chamber - on Floor Three (Only one event can be triggered)
"""
def storage_chamber():
    print("You enter the storage chamber.")
    print("Someone took all consumable items.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            if not any(choice in CHOICES_MADE for choice in ['storage_investigation', 'storage_voices', 'storage ambush']):
                print("As you try to inspect the room further, you hear something!")
                print("As you turn around, you see black smoke a few meters in front of you.")
                print("Focus was decreased by 1.")
                print("Luck was raised by 1.")
                player.decrease_stat('focus', 1)
                player.raise_stat('luck', 1)
                CHOICES_MADE.add('storage_investigation')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(choice in CHOICES_MADE for choice in ['storage_investigation', 'storage_voices', 'storage ambush']):
                print("The voices you hear get louder. They say:'Give in, you cannot escape...'")
                print("You anxiously turn around to see some black some disappearing.")
                print("Focus was decreased by 1.")
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('storage_voices')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(choice in CHOICES_MADE for choice in ['storage_investigation', 'storage_voices', 'storage ambush']):
                print("While rearranging the shelves, a dark figure jumps you!")
                print("You fell hard onto the ground, but you cannot see anyone...")
                print("Constitution was decreased by 2.")
                player.decrease_stat('constitution', 2)
                CHOICES_MADE.add('storage_ambush')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor1()
            break
        else:
            error_input()

def floor_lobby3():
    print("You enter the floor lobby.")
    print("As you enter, you see a door leading to a spiraling stairway.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            print("As you try to go down the stairs, you hear a voice.")
            print("'Those without identity cannot pass!'")
            print("'Who are you?'")
            solution_1 = input ("I am a...")
            if solution_1 == "samurai":
                print("The powers cannot hold you anymore.")
                print("You descend to the first floor.")
                IN_ROOM = False
                start_floor2()
                break
            else:
                print("'That is incorrect!'")
                print("'Turn back to the shadows where thou came from!'")
                floor_lobby3()
        elif choice == '2':
            if 'lobby_warning' not in CHOICES_MADE:
                print("This room is filled with malice.")
                print("You should not do anything unnecessary")
                print("Luck was raised by 1.")
                player.raise_stat('focus', 1)
                CHOICES_MADE.add('lobby_warning')
            else:
                redundant_choice()
        elif choice == '3':
            if 'beartrap' not in CHOICES_MADE:
                print("You try to move the couch when your leg suddenly starts hurting.")
                print("You have stepped into a beartrap.")
                print("Constitution was decreased by 2")
                print("Luck was decreased by 1")
                player.decrease_stat('constitution', 2)
                player.decrease_stat('luck', 1)
                CHOICES_MADE.add('beartrap')
            else:
                redundant_choice()
        elif choice == '4':
            IN_ROOM = False
            start_floor1()
            break
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
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            if not any(choice in CHOICES_MADE for choice in ['gym_approach', 'gym_ambush', 'gym_vanish']):
                print("You try finding something to help against the demon.")
                print("However, you cannot spot something in that instance.")
                print("The demon approaches you!")
                print("Focus was decreased by 1.")
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('gym_approach')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(choice in CHOICES_MADE for choice in ['gym_approach', 'gym_ambush', 'gym_vanish']):
                print("But before you can even react, the demon strikes you in the head.")
                print("Constitution was decreased by 3")
                player.decrease_stat('constitution', 3)
                CHOICES_MADE.add('gym_ambush')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(choice in CHOICES_MADE for choice in ['gym_approach', 'gym_ambush', 'gym_vanish']):
                print("You throw a small cupboard in-between you and the demon.")
                print("You ready your weapon as you realize:'He's gone'.")
                print("Instead, you find some bandages, which fell out of the cupboard.")
                print("Constitution was increased by 2.")
                player.raise_stat('constitution', 2)
                CHOICES_MADE.add('gym_vanish')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor2()
            break
        else:
            error_input()

def office():
    print("You enter the office.")
    print("A dark figure sits on a chair behind the desk.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            if not any(choice in CHOICES_MADE for choice in ['coat_demon', 'dagger_pierce', 'coat_rack']):    
                print("You ascertain whether the figure is actually a demon.")
                print("You find that it is only a coat on the chair.")
                print("Focus was decreased by 1.")
                print("Luck was raised by 1.")
                player.decrease_stat('focus', 1)
                player.raise_stat('luck', 1)
                CHOICES_MADE.add('coat_demon')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(choice in CHOICES_MADE for choice in ['coat_demon', 'dagger_pierce', 'coat_rack']):     
                print("Just as you start listening to your surroundings...")
                print("A dagger pierces your right chest!")
                print("Constitution was decreased by 2")
                player.decrease_stat('constitution', 2)
                CHOICES_MADE.add('dagger_pierce')
            else:
                redundant_choice2()    
        elif choice == '3':
            if not any(choice in CHOICES_MADE for choice in ['coat_demon', 'dagger_pierce', 'coat_rack']): 
                print("You throw a coat rack, which was right next to the door...")
                print("directly in the direction of the chair!")
                print("You hear a terrifying cry.")
                print("Focus was raised by 1.")
                player.raise_stat('focus', 1)
                CHOICES_MADE.add('coat_rack')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor2()
            break
        else:
            error_input()

def bathroom():
    print("You enter the bathroom.")
    print("This room is actually lit. You can see the bathtub filled with water.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu() 
        if choice == '1':
            if not any(choice in CHOICES_MADE for choice in ['demons_101', 'power_out']):
                print("Next to the bathtub is another cupboard.")
                print("In one of the drawers, you find a small book.")
                print("Added 'Fighting demons 101' to your inventory.")
                CHOICES_MADE.add('demons_101')
            else:
                redundant_choice3()
        elif choice == '2':
            if not any(choice in CHOICES_MADE for choice in ['bathtub', 'power_out']):
                print("You feel that the room is devoid of malice.")
                print("You choose to enter the bath and relax.")
                print("Constitution was raised by 2")
                print("Luck was raised by 1")
                player.raise_stat('constitution', 2)
                player.raise_stat('luck', 1)
                CHOICES_MADE.add('bathtub')
            else:
                redundant_choice3()
        elif choice == '3':
            if not 'power_out' in CHOICES_MADE:
                print("You try to move the bathtub, as it suddenly gets dark.")
                print("You feel something crush you feet and")
                print("your body being soaked in water.")
                print("Constitution was decreased by 2.")
                print("Luck was decreased by 2.")
                player.decrease_stat('constitution', 2)
                player.decrease_stat('luck', 2)
                CHOICES_MADE.add('power_out')
            else:
                redundant_choice3()
        elif choice == '4':
            IN_ROOM = False
            start_floor2()
            break
        else:
            error_input()

def second_floor_boss():
    print("You engage a terrifying monster.")
    strike_direction = fight_menu()
    if strike_direction == '1':
        print("Just before your blade hits...")
        second_floor_gameover()
    elif strike_direction == '2':
        print("Just before your blade hits...")
        second_floor_gameover()
    elif strike_direction == '3':
        print("Just before your blade hits...")
        second_floor_gameover()
    elif strike_direction == '4':
        print("You have hit the enemy's weak spot!")
        start_floor3()
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
    elif room_choice == '6':
        final_room()
    else:
        error_input

def kitchen():
    print("You enter the kitchen.")
    print("You see a demon eating something red on a plate.")
    print("It has not seen you yet.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            if not any(choice in CHOICES_MADE for choice in ['kitchen_note', 'kitchen_slice', 'table_flip']):
                print("You find a note.")
                print("It says: 'Keep important things close to your chest.'")
                print("The demon notices you and attacks!")
                print("Luck was decreased by 1.")
                player.decrease_stat('luck', 1)
                CHOICES_MADE.add('kitchen_note')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(choice in CHOICES_MADE for choice in ['kitchen_note', 'kitchen_slice', 'table_flip']):    
                print("You feel the demon's greed for blood.")
                print("He is too entranced to notice you.")
                print("You approach him from behind and slice his throat.")
                print("Focus was raised by 1.")
                player.raise_stat('focus', 1)
                CHOICES_MADE.add('kitchen_slice')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(choice in CHOICES_MADE for choice in ['kitchen_note', 'kitchen_slice', 'table_flip']): 
                print("You try to flip the table onto the demon.")
                print("It is too heavy, and you are unable to.")
                print("In the meantime, the demon jumps you!")
                print("Constitution was decreased by 2.")
                player.decrease_stat('constitution', 2)
                CHOICES_MADE.add('table_flip')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor3()
            break
        else:
            error_input()

def living_room():
    print("You enter the living room.")
    print("It is dark, and you can find nothing of note.")
    print("A radio is placed on a table. It is turned on.")
    IN_ROOM = True
    while IN_ROOM == True:
    choice = room_menu()
        if choice == '1':
            if 'beer_bottle' not in CHOICES_MADE:
                print("On the table, you find some beer bottles.")
                print("You take one that is not empty and drink it.")
                print("Constitution was raised by 1.")
                print("Focus was decreased by 1")
                player.raise_stat('constitution', 1)
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('beer_bottle')
            else:
                redundant_choice()
        elif choice == '2':
            if 'radio' not in CHOICES_MADE:    
                print("You listen more closely to the radio.")
                print("Thousands of voices tell you to give in.")
                print("Your mind becomes foggier.")
                print("Focus was decreased by 1.")
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('radio')
            else:
                redundant_choice()
        elif choice == '3':
            if 'pointless_search' not in CHOICES_MADE:    
                print("You rearrange the furniture, looking for clues.")
                print("After 15 minutes of dragging large objects, you give up.")
                print("Luck was decreased by 1.")
                player.decrease_stat('luck', 1)
                CHOICES_MADE.add('pointless_search')
            else:
                redundant_choice()
        elif choice == '4':
            IN_ROOM = False
            start_floor3()
            break
        else:
            error_input()

def guest_room():
    print("You enter the guest room.")
    print("Something is lurking under the bed sheet.")
    print("You can see two bumps.")
    IN_ROOM = True
    while IN_ROOM == True:
        choice = room_menu()
        if choice == '1':
            if not any(choice in CHOICES_MADE for choice in ['bed_sheet', 'musical_box', 'mattress']): 
                print("You pull the sheet from the bed.")
                print("A demon was hidden under the sheet!")
                print("It uses the opportunity to jump you.")
                print("Constitution was decreased by 2")
                player.decrease_stat('constitution', 2)
                CHOICES_MADE.add('bed_sheet')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(choice in CHOICES_MADE for choice in ['bed_sheet', 'musical_box', 'mattress']):    
                print("You hear a musical box. You decide to turn up the volume.")
                print("The demon under the bed falls asleep.")
                print("You then cleanly slice its neck.")
                print("Focus was raised by 1.")
                player.raise_stat('focus', 1)
                CHOICES_MADE.add('musical_box')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(choice in CHOICES_MADE for choice in ['bed_sheet', 'musical_box', 'mattress']):    
                print("You lever the mattress to the right.")
                print("You hear a loud thud. It sounded like someone fell to the floor.")
                print("As you ready yourself, a demon approaches you.")
                print("Luck was decreased by 1.")
                player.decrease_stat('luck', 1)
                CHOICES_MADE.add('mattress')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor3()
            break
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
        player.decrease_stat('focus', 2)
    elif choice == '3':
        print("As you try to push the closet away, it buckles.")
        print("You are buried under the closet.")
        print("You can barely escape your grave.")
        print("Luck was decreased by 2.")
        print("Constitution was decreased by 1.")
        player.decrease_stat('luck', 2)
        player.decrease_stat('constitution', 1)
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

def final_room():
    print("The door to the outside is sealed.")
    print("On the seal, you can spot one empty circle.")
    print("You hear a voice!")
    print("'You want to leave this place?!'")
    print("'Write the word of your salvation onto the seal!'")
    print("'Accept it, and become a samurai once again!'")
    final_riddle = input ("The salvation of a samurai is...")
    if final_riddle == "death":
        print("After you step away from the seal, it begins to shine.")
        print("Suddenly, everything around you is engulfed in light!")
        print("Congrats! You have beaten 'Dream Mansion'!")
    else:
        print("After you step away from the seal, it begins to wither.")
        print("Suddenly, you and everything around you begins to decay!")
        print("You try to reach...")
        print("...")
        print("...")
        print("...")


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
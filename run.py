"""
Dream Mansion - a text based game
"""

# Main Class - Containts player's starting stats


class samurai:
    def __init__(self, constitution, focus, luck, inventory):
        self.constitution = constitution
        self.focus = focus
        self.luck = luck
        self.inventory = inventory

    def display_stat(self):
        """
        Displays the character's status
        """
        print(f"Constitution: {self.constitution}")
        print(f"Focus: {self.focus}")
        print(f"Luck: {self.luck}")

    def display_inventory(self):
        print("You currently are carrying the following items:")
        for item in self.inventory:
            print(f"- {item.name}")

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
        Triggers stat-based Game Over
        """
        if self.constitution <= 0:
            print("""
            You can barely stand, your wounds are too severe.
            Your sight turns red, you feel your limbs become numb...
            Game Over
            """)
            return_question()
        elif self.focus <= 0:
            print("""
            You cannot form one clear thought, the voices are too loud!
            It hurts!! You beg it to STOP!!!
            Game Over
            """)
            return_question()
        elif self.luck <= 0:
            print("""
            Suddenly, you hear a voice out of nowhere.
            'You know what? I have become weary of you...'
            Game Over
            """)
            return_question()

    def check_final_stats(self):
        """
        Adds the sum of all player character's stats after reaching the final
        scene.
        """
        final_stat = self.constitution + self.focus + self.luck
        return final_stat


class items:
    """
    Class for handling interaction with Items menu
    """
    def __init__(self, name, description, action, content):
        self.name = name
        self.description = description
        self.action = action
        self.content = content

    def display_description(self):
        print(f"You hold a {self.name} in your hand.")
        print(f"{self.description}")

    def use_item(self):
        print(f"You {self.action} the {self.name}.")
        print(self.content)


"""
Instance for samurai class
"""

player = samurai(constitution=5, focus=5, luck=5, inventory=[])


"""
Instances for items class
"""


# Katana Item
katana_descr = "It is a sharp longsword with only one cutting edge."
katana_use = "You feel your own soul reverberating in it."
katana = items(
    "Katana",
    description=katana_descr,
    action="swing",
    content=katana_use
)


# Diary Item
diary_descr = "It contains the daily life stories of an unbeaten swordsman."
diary_cont = """
There is only one readable entry:

I tell Katsuma every day. He won't listen.
Don't act, react!
Mirror the opponent's atttack with the opposite movement.
Still, he does nothing but blindly rush into a fight.
At this rate, he will never be a true samurai...
"""
diary = items(
    "Diary",
    description=diary_descr,
    action="read",
    content=diary_cont
)


# Fighting Demons 101 Item
d101_descr = "They are notes about how to fight demons effectively."
d101_cont = """
Fighting demons in a combat of strength is futile.
Their strength far surpasses anything a human is capable of.
However, they are slow, and they are vunerable to sword slashes.
This means that a swing from the opposite side will always hit a demon.
If a demon attacks from above, hit him from below.
Do the opposite when they try to use their feet for attacks.
Remember though that strike from their one flank
will hit you on the other side...
...
All other notes were ripped out.
"""
demons_101 = items(
    "Fighting Demons 101",
    description=d101_descr,
    action="read",
    content=d101_cont
)


# Wakizashi Item
waki_descr = "It is a shortsword used for rituals. You cannot fight with it."
waki_use = """
While you take a closer look at it, you remember something.
Centuries ago, wakizashis were used for ritual suicide.
Samurai were not to bring their master shame.
They would serve their lord until the bitter end.
Sacrificing their lives to protect their own
and their lord's honor was seen as a virtue.
"""
wakizashi = items(
    "Wakizashi",
    description=waki_descr,
    action="look at",
    content=waki_use
)


# 'Key' Item
key_descr = "It is a short key, probably for one of the mansion's rooms."
key_use = """
Weird. There were no rooms locked in this mansion until now.
This probably does not open one of the bigger rooms then.
"""
key = items(
    "Key",
    description=key_descr,
    action="grab",
    content=key_use
)

"""
Constants for Maintaining Menu Choices and Navigation
"""


CHOICES_MADE = set()
IN_FLOOR = False
IN_ROOM = False
IN_INVENTORY = False


"""
Functions for Describing Player Actions
"""


def investigate():
    """
    Reminder Text for Option 1
    """
    print("You carefully investigate the room...")


def perceive():
    """
    Reminder Text for Option 2
    """
    print("You perceive your surroundings, trying to gather information...")


def rearrange():
    """
    Reminder Text for Option 3
    """
    print("You rearrange items in the room, looking for hidden clues...")


"""
Redundancy and error messages - Tell the user that a input the did was either
not valid or cannot be triggered anymore
"""


def redundant_choice():
    """
    Redundancy message for normal room
    """
    print("You have already taken this action.")
    print("You will not find anything new repeating it.")


def redundant_choice2():
    """
    Redundancy message for fight room
    """
    print("You do not feel an enemy presence anymore.")
    print("There is nothing more to find here...")


def redundant_choice3():
    """
    Redundancy message for exception - bathroom
    """
    print("You have already used up the bathroom with your actions.")
    print("Hopefully, you haven't broken it...")


def error_input():
    """
    User message in case of irregular input
    """
    print("Invalid choice. Please enter a valid input.")


"""
Game Overs and Endings - Lists all messages after ending the game (except stat-
based Game Overs)
"""


def second_floor_gameover():
    """
    Gained after losing to Monster on 2nd floor
    """
    print("""
    A large force hits your body.
    You feel your bones split, and your flesh tearing!
    You almost pass out from the pain.

    However, there is nothing that you can do.
    Your body does not listen to you anymore.
    You cannot even breathe...

    Game Over
    """)
    return_question()


def bad_ending():
    """
    Gained after finishing game with final_stat <= 5
    """
    print("""


    You want to reach out to grab your blade, but your powers are waning.
    In desparation, you barely manage to unsheathe the blade.
    But in exactly that moment you hear Maboroshi's voice.
    '...you are mine...'

    Six months later:
    'Samurai, our attack on Kyoto is imminent.
    Signal the other demons that the end of dusk is the starting point.
    Turn as many people as possible into demons.
    Let the rest perish...'

    You answer: '... as you wish...'

    End - Bad Ending
    """)
    return_question()


def neutral_ending():
    """
    Gained after finishing game with final_stat <= 10
    """
    print("""


    The illusion has taken a toll on you. You are not at your best.
    Still, you have to try. You cannot let Maboroshi get away.
    You prepare your katana for a counterattack.
    You swing your blade, as you feel...

    In a graveyard in Kyoto, stones are laid upon a grave.
    It reads: 'Here rests the slayer of Maboroshi'
    It is a symbol of hope in trying times.
    Without you, who will stand up to the demons?

    End - Neutral Ending
    """)
    return_question()


def true_ending():
    """
    Gained after finishing game with final_stat > 10
    """
    print("""


    This is your moment. You know Maboroshi is bluffing.
    He casted the illusion because he cannot defeat you directly.
    You approach him with silence, but also with determination.
    He screams: "Begone!"

    In a flash, you behead Maboroshi. He could not even react.
    You finally relax: A big threat of demonkind has vanished.
    Surely, many other challenges wait for you.
    But if you stay true to yourself, you are sure to overcome...
    every challenge on your path.

    End - True Ending
    """)
    return_question()


def return_question():
    """
    Return function - Sends user to title screen
    """
    IN_ROOM = True
    while IN_ROOM:
        return_answer = input(
            "Return to title screen (Yes = 1; No = 0):\n"
        )
        if return_answer == "0":
            exit()
        elif return_answer == "1":
            player = samurai(constitution=5, focus=5, luck=5, inventory=[])
            title_screen()
        else:
            error_input()


"""
Menus - Two Menus - User interfaces for fighting and exploring
"""


def room_menu():
    """
    Menu for room interaction
    """
    print("What would you like to do?")
    print("1. Investigate")
    print("2. Perceive")
    print("3. Rearrange")
    print("4: Change rooms")
    print("5: Display items")
    print("6. Display stats")
    choice = input("Enter your choice (1-6):\n")
    if choice == '1':
        investigate()
    elif choice == '2':
        perceive()
    elif choice == '3':
        rearrange()
    elif choice == '4':
        pass
    elif choice == '5':
        print("You take a look at your equipment.")
        print("What do you want to do?")
        print("1.List collected items")
        print("2.Take closer look at an item")
        item_input = input("Enter your choice (1-2):\n")
        if item_input == "1":
            player.display_inventory()
        elif item_input == "2":
            print("You take out the...")
            select_item = input("Write out the item you want to use:\n")
            for item in player.inventory:
                if select_item.lower() == item.name.lower():
                    print("What would you want to do with it?")
                    print("1.Remember what it is")
                    print("2.Use it")
                    item_detail = input("Enter your choice (1-2):\n")
                    if item_detail == "1":
                        item.display_description()
                    elif item_detail == "2":
                        item.use_item()
                    else:
                        error_input()
                else:
                    print("This item is currently not in your possession.")
        else:
            error_input()
    elif choice == "6":
        player.display_stat()
    else:
        error_input()
    return choice


def fight_menu():
    """
    Menu for fight scenarios
    """
    print("You are engaged in a fight.'")
    print("From where do you want to strike?")
    print("1. Strike from above")
    print("2. Strike from left flank")
    print("3. Strike from right flank")
    print("4: Strike from below")
    strike_direction = input("Enter your choice (1-4):\n")
    return strike_direction


"""
Title Screen Functions
"""


def title_screen():
    """
    Starting screen
    """
    print("Ladies and gentleman!")
    print("I welcome you to...")
    print()
    print()
    print("""
██████╗ ██████╗ ███████╗ █████╗ ███╗   ███╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗ ████║
██║  ██║██████╔╝█████╗  ███████║██╔████╔██║
██║  ██║██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║
██████╔╝██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

███╗   ███╗ █████╗ ███╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗
████╗ ████║██╔══██╗████╗  ██║██╔════╝██║██╔═══██╗████╗  ██║
██╔████╔██║███████║██╔██╗ ██║███████╗██║██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║██║╚██╗██║╚════██║██║██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║███████║██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    """)
    print()
    print("What would you like to do?")
    print("1.Start game")
    print("2.How to play")
    print("3.Credits")
    print("4.Exit Game")
    title_choice = input("Enter your choice (1-4):")
    if title_choice == "1":
        game_start()
    elif title_choice == "2":
        display_faq()
    elif title_choice == "3":
        display_credits()
    elif title_choice == "4":
        exit()
    else:
        error_input()


def display_faq():
    print("""
    About Dream Mansion:
    This program is a text-based game. Its story plays out in a mansion.
    It does look eerie, and many dangers lie ahead...
    Can you find the exit?

    General Gameplay:
    While traversing the mansion, you will explore different rooms.
    After most events, you will be shown a list of options.
    To take actions in this game, simply put in a number
    You will the do the action for this specific room.

    User Input:
    There will be times when the game requires you to put in a word.
    In that case, fill in the word or phrase.
    Please watch out for spelling errors.

    Your Character:
    The player character starts with five points in each of their stats.
    If any of these stats fall to zero, the game ends.
    Try maintaining each stat, and avoid scenarios which might seem dangerous.

    Your Inventory:
    In the game, you will find many items.
    Some are neccessary to proceed, some provide very important information.
    You can check your inventory whenever you are in a room.
    """)
    print()
    print("What would you like to do?")
    print("1.Start game")
    print("2.How to play")
    print("3.Credits")
    print("4.Exit Game")
    title_choice = input("Enter your choice (1-4):")
    if title_choice == "1":
        game_start()
    elif title_choice == "2":
        display_faq()
    elif title_choice == "3":
        display_credits()
    elif title_choice == "4":
        exit()
    else:
        error_input()


def display_credits():
    print("Creator: Sebastian Bucher")
    print("Mentor: Richard Wells")
    print("Code Institute")
    print()
    print("What would you like to do?")
    print("1.Start game")
    print("2.How to play")
    print("3.Credits")
    print("4.Exit Game")
    title_choice = input("Enter your choice (1-4):")
    if title_choice == "1":
        game_start()
    elif title_choice == "2":
        display_faq()
    elif title_choice == "3":
        display_credits()
    elif title_choice == "4":
        exit()
    else:
        error_input()


"""
Functions for Main Story
"""


# Functions for 1st floor
def start_floor1():
    """
    Floor Menu for 1st floor
    """
    print("Several doors appear in front of you.")
    print("Which one do you want to enter?")
    print("1. The Lounge")
    print("2. The Storage Chamber")
    print("3. The Floor Lobby")
    IN_FLOOR = True
    while IN_FLOOR:
        room_choice = input("Enter your choice (1-3):\n")
        if room_choice == '1':
            IN_FLOOR = False
            lounge()
        elif room_choice == '2':
            IN_FLOOR = False
            storage_chamber()
        elif room_choice == '3':
            IN_FLOOR = False
            floor_lobby()
        else:
            error_input()


def lounge():
    """
    Lounge Room - normal room
    """
    print("You enter the floor lobby.")
    print("It contains multiple cupboards.")
    print("They once seemed to contain many different items.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if 'diary' not in CHOICES_MADE:
                print("As you look around the lobby, you find a small book.")
                print("It says 'Musashi's Diary'.")
                print("Added 'Diary' to your inventory.")
                CHOICES_MADE.add('diary')
                player.inventory.append(diary)
            else:
                redundant_choice()
        elif choice == '2':
            if 'lounge_voices' not in CHOICES_MADE:
                print("The voices you hear get louder.")
                print("They say:'Give in, you cannot escape...'")
                print("Focus was lowered by 1.")
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('lounge_voices')
            else:
                redundant_choice()
        elif choice == '3':
            if 'katana' not in CHOICES_MADE:
                print("As you move the cupboard, you find a katana behind it.")
                print("Added 'Katana' to inventory.")
                CHOICES_MADE.add('katana')
                player.inventory.append(katana)
            else:
                redundant_choice()
        elif choice == '4':
            IN_ROOM = False
            start_floor1()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def storage_chamber():
    """
    Storage Chamber - fight room (but no fight menu)
    """
    print("You enter the storage chamber.")
    print("Someone took all consumable items.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if not any(
                choice in CHOICES_MADE
                for choice in
                ['storage_investigation', 'storage_voices', 'storage_ambush']
            ):
                print("As you try to inspect the room further...")
                print("...you hear something!")
                print("You see black smoke a few meters in front of you.")
                print("Focus was raised by 1.")
                print("Luck was raised by 1.")
                player.raise_stat('focus', 1)
                player.raise_stat('luck', 1)
                CHOICES_MADE.add('storage_investigation')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(
                choice in CHOICES_MADE
                for choice in
                ['storage_investigation', 'storage_voices', 'storage_ambush']
            ):
                print("The voices you hear get louder.")
                print("They say:'Give in, you cannot escape...'")
                print("You anxiously turn around to see...")
                print("some black smoke disappearing.")
                print("Focus was decreased by 1.")
                player.decrease_stat('focus', 1)
                CHOICES_MADE.add('storage_voices')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(
                choice in CHOICES_MADE
                for choice in
                ['storage_investigation', 'storage_voices', 'storage_ambush']
            ):
                print("While rearranging the shelves, a silhouette jumps you!")
                print("While rearranging the shelves, a silhouette jumps you!")
                if katana in player.inventory:
                    print("Instinctively, you grab your katana...")
                    print("and slash towards the figure!")
                    print("However, the only thing you see...")
                    print(" after your attack is black smoke.")
                    CHOICES_MADE.add('storage_ambush')
                else:
                    print("You fell hard onto the ground, but...")
                    print("nobody else seems to be here but you...")
                    print("Constitution was decreased by 2.")
                    player.decrease_stat('constitution', 2)
                    CHOICES_MADE.add('storage_ambush')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor1()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def floor_lobby():
    """
    Floor Lobby - 1st player riddle (checks also if Katana is in inventory)
    """
    print("You enter the floor lobby.")
    print("As you enter, you see a door leading to a spiraling stairway.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            print("As you try to go down the stairs, you hear a voice.")
            print("'Those without identity cannot pass!'")
            print("'Who are you?'")
            solution_1 = input("I am a...\n")
            if solution_1.lower() == "samurai":
                if katana in player.inventory:
                    print("The powers cannot hold you anymore.")
                    print("You descend to the first floor.")
                    IN_ROOM = False
                    start_floor2()
                else:
                    print("You feel that you have given the correct answer...")
                    print("However, you seem to lack something important!")
                    print("You should go back and check the other rooms...")
            else:
                print("'That is incorrect!'")
                print("'Turn back to the shadows where thou came from!'")
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
                print("You try to move the couch.")
                print("Suddenly your leg starts hurting.")
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
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


# Functions for Second Floor
def start_floor2():
    """
    Floor Menu for 2nd floor
    """
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
    IN_FLOOR = True
    while IN_FLOOR:
        room_choice = input("Enter your choice (1-4):\n")
        if room_choice == '1':
            IN_FLOOR = False
            gym()
        elif room_choice == '2':
            IN_FLOOR = False
            office()
        elif room_choice == '3':
            IN_FLOOR = False
            bathroom()
        elif room_choice == '4':
            IN_FLOOR = False
            second_floor_boss()
        else:
            error_input()


def gym():
    """
    Gym - Fight Room
    """
    print("You enter the gym.")
    print("Before you can see anything else, a demon appears in front of you!")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if not any(
                choice in CHOICES_MADE
                for choice in ['gym_approach', 'gym_ambush', 'gym_vanish']
            ):
                print("You try finding something to help against the demon.")
                print("However, you cannot find anything useful.")
                print("The demon attacks you with a right hook!")
                strike_direction = fight_menu()
                if strike_direction == "3":
                    print("Your blade is faster than your opponnent's attack!")
                    print("After hitting your opponent...")
                    print("it vanishes into thin air...")
                    print("Focus was raised by 1.")
                    player.raise_stat('focus', 1)
                    CHOICES_MADE.add('gym_approach')
                else:
                    print("You feel a hit to your left cheek!")
                    print("You fall to the ground!")
                    print("As you get back up, the demon is gone...")
                    print("Constitution was decreased by 2.")
                    player.decrease_stat('constitution', 2)
                    CHOICES_MADE.add('gym_approach')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(
                choice in CHOICES_MADE
                for choice in ['gym_approach', 'gym_ambush', 'gym_vanish']
            ):
                print("But before you can even react...")
                print("the demon strikes you in the head!")
                print("Constitution was decreased by 3.")
                player.decrease_stat('constitution', 3)
                CHOICES_MADE.add('gym_ambush')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(
                choice in CHOICES_MADE
                for choice in ['gym_approach', 'gym_ambush', 'gym_vanish']
            ):
                print("You throw a small cupboard between you and the demon.")
                print("You ready your weapon as you realize:'He's gone!'")
                print("You find some first aid hidden in the cupboard.")
                print("Constitution was increased by 2.")
                player.raise_stat('constitution', 2)
                CHOICES_MADE.add('gym_vanish')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor2()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def office():
    """
    Office - Fight Room
    """
    print("You enter the office.")
    print("A dark figure sits on a chair behind the desk.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if not any(
                choice in CHOICES_MADE
                for choice in ['coat_demon', 'dagger_pierce', 'coat_rack']
            ):
                print("You ascertain whether the figure is actually a demon.")
                print("You find that it is only a coat on the chair.")
                print("Luck was raised by 1.")
                player.raise_stat('luck', 1)
                CHOICES_MADE.add('coat_demon')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(
                choice in CHOICES_MADE
                for choice in ['coat_demon', 'dagger_pierce', 'coat_rack']
            ):
                print("Just as you start listening to your surroundings...")
                print("A dagger pierces your right chest!")
                print("Constitution was decreased by 2.")
                player.decrease_stat('constitution', 2)
                CHOICES_MADE.add('dagger_pierce')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(
                choice in CHOICES_MADE
                for choice in ['coat_demon', 'dagger_pierce', 'coat_rack']
            ):
                print("You throw a coat rack placed next to the door...")
                print("directly in the direction of the chair!")
                print("You hear a terrifying cry.")
                print("Before you can even blink, a demon attemps...")
                print("... to kick you from below!")
                strike_direction = fight_menu()
                if strike_direction == "1":
                    print("You strike at the demon from above!")
                    print("As your slash comes to an end...")
                    print("Only black smoke remains...")
                    print("Focus was raised by 1.")
                    player.raise_stat('focus', 1)
                    CHOICES_MADE.add('coat_rack')
                else:
                    print("You feel a hit to your stomach!")
                    print("You stumble backwards!")
                    print("As you get back up, the demon is gone...")
                    player.decrease_stat('constitution', 2)
                    CHOICES_MADE.add('coat_rack')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor2()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def bathroom():
    """
    Bathroom - Special Trigger Room
    """
    print("You enter the bathroom. It actually has working lights!")
    print("The bathtub filled with water.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if not any(
                choice in CHOICES_MADE for choice in
                ['demons_101', 'power_out']
            ):
                print("Next to the bathtub is another cupboard.")
                print("In one of the drawers, you find a small book.")
                print("Added 'Fighting Demons 101' to your inventory.")
                CHOICES_MADE.add('demons_101')
                player.inventory.append(demons_101)
            else:
                redundant_choice3()
        elif choice == '2':
            if not any(
                choice in CHOICES_MADE for choice in
                ['bathtub', 'power_out']
            ):
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
            if 'power_out' not in CHOICES_MADE:
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
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def second_floor_boss():
    """
    Second Floor Boss - Fight with Game Over Potential
    """
    print("You see a large monster.")
    print("You won't be able to run from it!")
    IN_ROOM = True
    while IN_ROOM:
        val_answer = input(
            "Proceed? (Yes = 1; No = 0):\n"
        )
        if val_answer == '0':
            start_floor2()
        elif val_answer == '1':
            print("You engage a terrifying monster in battle.")
            print("It tries to headbutt you!")
            strike_direction = fight_menu()
            if strike_direction == '4':
                print("You have hit the enemy's weak spot!")
                print("You hear a loud shriek.")
                print("The monster staggers, but goes back on the attack...")
                print("with a haymaker from its left side.")
                strike_direction2 = fight_menu()
                if strike_direction2 == '2':
                    print("The monster can't keep up with your speed.")
                    print("You wound it once more. It can barely stand.")
                    print("It uses its remaining power to punch you...")
                    print("...in the gut.")
                    strike_direction3 = fight_menu()
                    if strike_direction3 == '1':
                        print("Once more, your blade strikes true.")
                        print("You hit the monster the third time.")
                        print("It shrieks loudly one more time...")
                        print("...before turning into black smoke.")
                        print("You descend another spiraling staircase.")
                        IN_ROOM = False
                        start_floor3()
                    else:
                        IN_ROOM = False
                        second_floor_gameover()
                else:
                    IN_ROOM = False
                    second_floor_gameover()
            else:
                IN_ROOM = False
                second_floor_gameover()
        else:
            error_input()


# Functions for Floor 3:
def start_floor3():
    """
    Floor Menu for 3rd floor
    """
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
    IN_FLOOR = True
    while IN_FLOOR:
        room_choice = input("Enter your choice (1-6):\n")
        if room_choice == '1':
            IN_FLOOR = False
            kitchen()
        elif room_choice == '2':
            IN_FLOOR = False
            living_room()
        elif room_choice == '3':
            IN_FLOOR = False
            guest_room()
        elif room_choice == '4':
            IN_FLOOR = False
            bed_room()
        elif room_choice == '5':
            IN_FLOOR = False
            closet()
        elif room_choice == '6':
            IN_FLOOR = False
            final_room()
        else:
            error_input()


def kitchen():
    """
    Kitchen - Demon Fight (Only one choice possible)
    """
    print("You enter the kitchen.")
    print("You see a demon eating something red on a plate.")
    print("It has not seen you yet.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if not any(
                choice in CHOICES_MADE for choice in
                ['kitchen_note', 'kitchen_slice', 'table_flip']
            ):
                print("You find a note.")
                print("It says: 'Keep important things close to your chest.'")
                print("The demon notices you and attacks!")
                print("It tries to kick you.")
                strike_direction = fight_menu()
                if strike_direction == '1':
                    print("You successfully slice the demon in half.")
                    print("The two halves turn into black smoke.")
                    print("Focus was raised by 1.")
                    player.raise_stat('focus', 1)
                    CHOICES_MADE.add('kitchen_note')
                else:
                    print("You feel a sharp pain between your legs")
                    print("As you shortly look up from your wimpering...")
                    print("the demon is nowhere to be found!")
                    print("Constitution was decreased by 2.")
                    player.decrease_stat('constitution', 2)
                    CHOICES_MADE.add('kitchen_note')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(
                choice in CHOICES_MADE for choice in
                ['kitchen_note', 'kitchen_slice', 'table_flip']
            ):
                print("You feel the demon's greed for blood.")
                print("He is too entranced to notice you.")
                print("You approach him from behind and slice his throat.")
                print("Luck was raised by 1.")
                player.raise_stat('luck', 1)
                CHOICES_MADE.add('kitchen_slice')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(
                choice in CHOICES_MADE for choice in
                ['kitchen_note', 'kitchen_slice', 'table_flip']
            ):
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
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def living_room():
    """
    Living Room - fight room
    """
    print("You enter the living room.")
    print("It is dark, and you can find nothing of note.")
    print("A radio is placed on a table. It is turned on.")
    IN_ROOM = True
    while IN_ROOM:
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
                print("After 15 minutes, completely exhausted, you give up.")
                print("Luck was decreased by 1.")
                player.decrease_stat('luck', 1)
                CHOICES_MADE.add('pointless_search')
            else:
                redundant_choice()
        elif choice == '4':
            IN_ROOM = False
            start_floor3()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def guest_room():
    """
    Guest Room - fight room
    """
    print("You enter the guest room.")
    print("Something is lurking under the bed sheet.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if not any(
                choice in CHOICES_MADE
                for choice in ['bed_sheet', 'musical_box', 'mattress']
            ):
                print("You pull the sheet from the bed.")
                print("A demon was hidden under the sheet.")
                print("It uses the opportunity to jump you!")
                print("Constitution was decreased by 2")
                player.decrease_stat('constitution', 2)
                CHOICES_MADE.add('bed_sheet')
            else:
                redundant_choice2()
        elif choice == '2':
            if not any(
                choice in CHOICES_MADE
                for choice in ['bed_sheet', 'musical_box', 'mattress']
            ):
                print("You hear a musical box.")
                print("You decide to turn up the volume.")
                print("The demon under the bed falls asleep.")
                print("You then cleanly slice its neck.")
                print("Focus was raised by 1.")
                player.raise_stat('focus', 1)
                CHOICES_MADE.add('musical_box')
            else:
                redundant_choice2()
        elif choice == '3':
            if not any(
                choice in CHOICES_MADE
                for choice in ['bed_sheet', 'musical_box', 'mattress']
            ):
                print("You lever the mattress to the right.")
                print("You hear a loud thud.")
                print("It sounded like someone fell to the floor.")
                print("As you ready yourself, a demon approaches you.")
                print("It tries to attack you with a haymaker from the right.")
                strike_direction = fight_menu()
                if strike_direction == '3':
                    print("You anticipate the demon's attack.")
                    print("Cut in upper and lower halves...")
                    print("The demon's remains vanish.")
                    print("Focus was raised by 1.")
                    player.raise_stat('focus', 1)
                    CHOICES_MADE.add('mattress')
                else:
                    print("The impact of the strike is strong.")
                    print("It makes you writhe in pain")
                    print("Yet again, you do not know...")
                    print("Why the demons keep disappearing.")
                    print("Constitution was decreased by 2.")
                    player.decrease_stat('constitution', 2)
                    CHOICES_MADE.add('mattress')
            else:
                redundant_choice2()
        elif choice == '4':
            IN_ROOM = False
            start_floor3()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def bed_room():
    """
    Bed Room - Demon Fight (Contains Key for Closet)
    """
    print("You enter the bed room.")
    print("You see a silver chest lying on the bed.")
    print("Faint voices can be heard.")
    IN_ROOM = True
    while IN_ROOM:
        choice = room_menu()
        if choice == '1':
            if 'wakizashi' not in CHOICES_MADE:
                print("You open the briefcase.")
                print("You find a shortsword.")
                print("A key lies next to it")
                print("Added 'Wakizashi' to inventory.")
                print("Added 'Key' to inventory.")
                CHOICES_MADE.add('wakizashi')
                player.inventory.append(wakizashi)
                player.inventory.append(key)
            else:
                redundant_choice()
        elif choice == '2':
            if 'head_explosion' not in CHOICES_MADE:
                print("The voices become stronger!")
                print("Why? Why?? Why couldn't you SAVE US???")
                print("You feel as if your head is about to explode.")
                print("Focus was decreased by 2.")
                player.decrease_stat('focus', 2)
                CHOICES_MADE.add('head_explosion')
            else:
                redundant_choice()
        elif choice == '3':
            if 'closet_burial' not in CHOICES_MADE:
                print("As you try to push the closet away, it buckles.")
                print("You are buried under the closet.")
                print("You can barely escape your grave.")
                print("Luck was decreased by 2.")
                print("Constitution was decreased by 1.")
                player.decrease_stat('luck', 2)
                player.decrease_stat('constitution', 1)
                CHOICES_MADE.add('closet_burial')
            else:
                redundant_choice()
        elif choice == '4':
            IN_ROOM = False
            start_floor3()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            error_input()
        player.check_stats()


def closet():
    """
    Closet - Vital Hint for Final Riddle (No Player Interaction)
    """
    if key in player.inventory:
        print("There is nothing in the room.")
        print("It is completely empty...")
        print("As you were about to leave the room...")
        print("You see something written on the wall:")
        print()
        print("DO NOT FEAR ...!!!")
        print("DO FEAR LIVING AS A PUPPET!!!")
        print()
        print("One word is stained with blood.")
        print("You cannot decipher it.")
        print("You leave the closet.")
    else:
        print("The door is locked.")
        print("You leave the closet be...")
    start_floor3()


def final_room():
    """
    Guest Room - Demon Fight
    """
    print("You fear a dark aura, pulling you in.")
    print("If you go now, you cannot turn back!")
    final_check = input(
        "Proceed? (Yes = 1; No = 0):\n"
    )
    if final_check == '0':
        start_floor3()
    elif final_check == '1':
        print("The door to the outside is sealed.")
        print("On the seal, you can spot one empty circle.")
        print("You hear a voice!")
        print("'You want to leave this place?!'")
        print("'Write the word of your salvation onto the seal!'")
        print("'Accept it, and become a samurai once again!'")
        final_riddle = input("The salvation of a samurai is...\n")
        if final_riddle.lower() == "death":
            print("After you step away from the seal, it begins to shine.")
            print("Suddenly, everything around you is engulfed in light!")
            final_scene()
        else:
            print("After you step away from the seal, it begins to wither.")
            print("Suddenly, you and everything around you begins to decay!")
            print("You try to reach...")
            print("...")
            print("...")
            print("Game Over")
            return_question()
    else:
        error_input()
        start_floor3()


def final_scene():
    """
    Final Scene - Epilogue and Determination of Player Ending
    """
    print("You have done it! You have broken the illusion!")
    print("Your opponent, the demon Maboroshi, stands before you.")
    print("'It seems this illusion could not bend you to my will...'")
    print("'Whatever! Face me, samurai!'")
    print("'You can struggle as much as you want...'")
    print("'But in the end, you will still become my puppet!'")
    end_stat = player.check_final_stats()
    if end_stat <= 5:
        bad_ending()
    elif end_stat <= 10:
        neutral_ending()
    elif end_stat >= 11:
        true_ending()
    else:
        print("Unknown error! Start from the beginning!")
        return_question()


def game_start():
    """
    Function to start game
    """
    print("...")
    print("...")
    print("I'm so tired...")
    print("...")
    print("...")
    IN_FLOOR = True
    while IN_FLOOR:
        initiate_game = input("Do you want to wake up? (Yes = 1; No = 0)")
        if initiate_game == "0":
            print("...")
            print("...")
            print("You close your eyes, one last time...")
            exit()
        elif initiate_game == "1":
            print("...")
            print("...")
            print("You wake up in an unknown location...")
            print("...")
            print("...")
            IN_FLOOR = False
            start_floor1()
        else:
            error_input()


title_screen()

# Dream Mansion

Dream Mansion is a text-based game. It is inspired by the Animation Series "Kimetsu no Yaiba".
Similar to the Episodes 10-14, the player is trapped in a mansion.

The player's goal is to escape the mansion and find out who they really are.


## Index

1. [How to play](#How-to-play)
2. [Planning Stages](#planning-stages)
3. [Structure](#structure)
4. [Testing](#testing)
5. [Deployment] (#deployment)
6. [Credits](#credits)

## **How to play**

As a player, your main choice of interacting with the game is structured in two ways.

### Number Input

In most cases, after displaying a story text, the game will display a menu.
Each item in that menu is listed with a number.
The player puts that number into that console.
If the string match, the chosen action will be executed.
Any other inputs will result in an error message and replay the last menu.

#### Floor Menus

The game consists of three floors. Each floor has its own floor menu.
In that menu, the player can choose which room to enter.
The number is at least three, at most 6 options.

In most cases, the player can return to the floor menu.
However, in the case of the Second Floor Boss, they cannot return if they chose that room.
In contrast, the player will be looped back to the floor menu if they do not have the key to the closet.

#### Fight Menus

After the first floor, the player can engage in combat scenarios against demon illusions.
These are triggered when choosing certain options in new rooms.
In that case, the player is redirected to the fight menu.

The player can choose to attack the demons from above, the left, the right or below.
In each scenario, the idea is to mirror the attack of the demon illusion.
Each attack direction is linked with a certain button.

If the player is successful, the focus of the player will rise by 1.
If the player is unsuccessful, the constitution of the player will decrease by 2.
Each battle can only be triggered once.

#### Room Menu

In each room, the player has access to the Room Menu. This menu offers six options.
The first three - Investigate, Perceive and Rearrange - trigger interactions and progress the story.
The fourth option allows players to switch room. They will be redirected to the floor menu.
The fifth option enables the player to see all items and use them to gain further information.
Finally, option number 6 displays the stats to the character.

### Text Input

#### Item Menu

In order to access their collected Items, the player has to type in their name.
In this case, the console will check whether an entry in the inventory matches the player input.
They then can decide whether to get a general description of it or interact with it.
Some items describe a general use of the weapon and have no further usage.
Other items contain text which reveal vital hints on clues or advice for combat situations.

If the player does not know which items he has, they can display them by choosing the first option in the items menu.

#### Riddles

After picking certain options in the room menu, the player is asked to input certain words.
These generally check if the player has understood the general motive of the samurai.
The first solution is 'samurai' and the second is 'death'.

The player is given hints in form of the items and also the message hidden in the closet.
The first riddle can be redone infinitely, while failing the second riddle results in a game over.

### Player Goals

#### Stats

When entering the mansion, the code contains a player instance.
The instance has three stats: Constitution, Focus and Luck. Their starting value is 5 for each of them.
Depending on the actions the player takes, these will either rise or decrease.
The stats determine what ending the player will experience.

#### Stat Game Over

If any stat should fall below 1, the player is shown a short statement in which they perish.
The game then starts anew.
The player is thus incentivised to keep up any stat below one and avoid scenarios that will lower these stats.

#### Endings

The ending of the game is also inspired by "Kimetsu no Yaiba".
If the player manages to get to the end, they find out the truth.
The mansion was a dream, an illusion cast by a demon they were fighting, Maboroshi.
The program will determine which ending the player gets based on the final stats.

1. Bad Ending (5 or below): The player is taken over by Maboroshi and helps their new master conquer Kyoto.
2. Neutral Ending (6 to 10): The player takes down Maboroshi, but dies in the process.
3. Good Ending(11+): The player defeats Maboroshi and lives on to fight other demons.

## **Planning Stages**

### General Idea:

One goal of entering the Code Institute program was for me to program a video game.
A recommended idea I found while researching for possible projects was to create a text-based game.
While not my favourite genre of games, I have played many different visual novels.
As such, I had experience of how to envision the progression of such a game.

The only step from there was to envision a setting.
The

### Target Audience(s):

The player:

- enjoys visual novels or text-based games.
- is interested in historical or modern Japan.
- enjoys solving puzzles.
- likes dark stories.
- is ideally above 16 years.

### Site Aims

Dream Mansion:

- tells a concise, but captivating story.
- tasks the player with solving riddles around the samurai.
- provides insight into samurai mentality.
- presents simple fighting scenarios.
- tasks the player with a simple, yet all-present stat management challenge.

### User Expericence:

As a user:

- I want to get a short overview about the game.
- I want to know which action I can take at any point.
- I want to know what items I have collected along the way.
- I want to be given clues with which to solve the game.
- I want to know how I am doing.
- I want to experience a tension-filled story.
- I want to know what happens to my character in the end.

## **Structure**

### First Floor

The first floor is an introductory stage of the game. 
The player obtains important items and gets a feeling for the mechanics. 
At this stage, there is no combination of events that could lead to a game over.

The floor consists of three rooms:

#### Lounge

- The player can find two items: the Katana and Musashi's Diary
- The player can only decrease his focus by one.
- Each event can be triggered once.
- Note: The katana is necessary for the player to proceed. If the player does not have it in their inventory, the start_floor2 function cannot be accessed.

#### Storage Room

- The player can raise their luck and focus or decrease their focus and constitution.
- The player encounters their first demon illusion. This encounter will not yet trigger the fight_menu.
- Only one event can be triggered.

#### Floor Lounge

- The player can raise their luck or decrease their constitution.
- From this floor, the player proceeds to the second floor. Two requirements need to be met.
- The player solves the ridde about their identity.
- The player has the katana in their inventory.

### Second Floor

The second floor has the most fights in the game. 
The player experiences and learns to master the fights with demon illusions.
From this stage on, the player's action can result in a game over.

The floor consists of four rooms:

#### Gym

- The player can raise all stats or decrease their focus and constitution.
- For the first time, the player can trigger a fight with a demon illusion.
- Only one event can be triggered.

#### Office

- 
- This room triggers another fight.
- Once more, only one event can be triggered.

#### Bathroom

- In this room, the player does not encounter enemies.
- The player can raise their focus and constitution and decrease their luck and constitution.
- Each event can be triggered.
- Should the player decide to rearrange the objects in the room, the other option cannot be triggered.

#### End of the Corridor

- The player encounters a monster. The player needs to win three stages of the battle to proceed.
- There are no second chances. If the player chooses a wrong option, they trigger a game over.
- To have the best chances, the player needs to understand the fighting system. The best chance of understanding so is to find the "Demon Fighting 101" in the bathroom and reading its content.

### Third Floor

On the third floor, the player needs to solve one more puzzle.
At this stage, the potential to have low constitution is high. Thus, the player needs to carefully access their options.
There are only two fights on this floor, but the amount of stat-decreasing events was increased.

A total of six rooms can be accessed:

#### Kitchen

- Another demon encounter is waiting for the player here.
- While this hint is not displayed as an item, one event hints the player to open the chest in the bedroom.
- 

#### Living Room

- In essence, this room is a trap. The player is hinted at that there is nothing to find here.
- If they choose to interact, they in most cases lose focus or luck. The only neutral interaction is a swap for constitution with focus. This might help in a situation where the player has depleted their constitution too much.
- Each event can be triggered once.

#### Guest Room

- This room contains the final demon encounter. 
- In the best case, the player can get focus without fighting. On the other hand, they can lose focus by

#### Bed Room

- This room contains the chest hinted at in the kitchen. It contains the two items which give the player access to the two hints about the 

#### Closet

- There are no events in the room.
- The player cannot access the room without finding the key in the bedroom first.
- If accessed, the player can read a message with the word for the final riddle. 
- However, the word is not visible. The player has to deduce the word from its context.

#### The Exit

- This room riddle triggers as soon as you enter.
- The player has to enter the keyword "death".
- If the player does so, they witness the final scene.
- If not, they get a game over screen.

### Final Scene

- The player alr

## **Testing**

### Bugs

- One big issue arose from the coordination of how the program would check which events were triggered. The idea of a list was considered first, but it turned out to be impractical. The events could be saved twice.
- Instead of a list, the set() function was used to save which options the player has already selected. Then, each branch of the conditional statements uses lists to check whether an event has already been triggered.

<hr>

- Due to the implementation of different menus, the loops for rooms and floors would interact with each other. This would lead to the console jumping to options between different menus.
- The while loops are linked to a constant IN_FLOOR or IN_ROOM. This way, only the code from each respective loop executes.

<hr>

- The first ASCIII Logo would not be displayed on the console correctly. One of the lines would shift drastically to the right. This would lead to numerous errors on the validator
- Another font was used and all whitespaces were removed.

## Deployment

In order to deploy Dream Mansion to Heroku, the following steps were taken.

1. Deploy the prototype version on Github
2. Log in to Heroku
3. Use an unused name
4. Create a key for PORT with the value 8000
5. Deploy the Node.js to the already activated Python Buildpack
6. Choose Github in the Deploy Menu
7. Select "Automatically Deploy"

After taking these steps, the project was successfully deployed on Heroku.


## **Credits**

- "Kimetsu no Yaiba" serves as the biggest inspration for the
- The title screen logo was created with the help from "patorjk.com".
- The insight into
- As starting point for programming a text-based game, I consulted the following two videos:
"Simple Python Project | Text-Based Adventure Game: Time Unraveled" by Comp Sci Central
"How To Code A Python Text-Based Adventure Game In 11 Minutes | Programming Tutorial For Beginners" by Shaun Halverson




Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly


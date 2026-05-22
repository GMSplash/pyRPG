# Imports:
import random

# game state
game_running = True

# Character information:
char_name = ""
char_class = "Peasant"
char_level = 1
char_exp = 0

# Character stats:
char_health = 10
char_mana = 5
char_str = 0
char_dex = 0
char_int = 0
char_wis = 0
char_con = 0

# Character Spells:

# Character Skills:

# Inventory:
gold = 0
current_weapon = "Unarmed"
weapon_stash = []

# exploration:
current_room = "entryway"

char_name = input("Enter your name: ")

print("Select your class:")
print("1. Warrior")
print("2. Mage")
print("3. Rogue")
print("4. Archer")
print("5. Cleric")

class_choice = input("Enter the number of your chosen class: ")

if class_choice == "1":
    char_class = "Warrior"
    char_str += 5
    char_con += 3

elif class_choice == "2":
    char_class = "Mage"
    char_int += 5
    char_wis += 3
    mana_bonus_roll = random.randint(1, 20)
    char_mana += mana_bonus_roll + char_wis

elif class_choice == "3":
    char_class = "Rogue"
    char_str += 3
    char_dex += 5

elif class_choice == "4":
    char_class = "Archer"
    char_dex += 5
    char_wis += 3
    char_mana += char_wis


elif class_choice == "5":
    char_class = "Cleric"
    char_wis += 5
    char_con += 3
    mana_bonus_roll = random.randint(1, 20)
    char_mana += mana_bonus_roll + char_wis

else:
    char_class = "Peasant"
    char_str += 1
    char_dex += 1
    char_int += 1
    char_wis += 1
    char_con += 1
    char_mana += char_wis

HP_roll1 = random.randint(1, 10)
HP_roll2 = random.randint(1, 10)

char_health += HP_roll1 + HP_roll2 + char_con


print(
    f"{char_class} {char_name} enters the dungeon with {char_health} HP! In front of you expands a large entryway. There is a door infront of you and to your left."
)

move_choice = 99

while game_running == True:

    if current_room == "entryway":

        print("You stand at the bottom of the stairs you used to enter the dungeon.")
        print("1. Move Forward")
        print("2. Move Left")
        print("3. Search the room")

        move_choice = int(
            input("Type the number associated with the action you want to preform: ")
        )

        if move_choice == 1:
            current_room = "entryway door"

        elif move_choice == 2:
            current_room = "iron gate"

        elif move_choice == 3:
            roll_loot = random.randint(1, 100)
            gold += roll_loot
            print(
                f"You look around the room and find a leather pouch. When you pick it up you hear the jingle of coins. Upon opening you find {roll_loot} gold. You now have {gold} gold."
            )

    elif current_room == "entryway door":

        print(
            "You move to the door infront of you. It is a large oaken door with a brass knob. Beyond the door you hear the sound of a fire and low murmurs you can't quite make out."
        )
        print("1. Open the door")
        print("2. Walk back into the room")

        move_choice = int(
            input("Type the number associated with the action you want to preform: ")
        )

        if move_choice == 1:
            current_room = "campsite room"

        elif move_choice == 2:
            current_room = "entryway"

    elif current_room == "iron gate":

        print(
            "You move to the left. Blocking your way is a small wrought iron gate. The latch is open. You could push it open easily."
        )
        print("1. Open the gate")
        print("2. Walk back into the room")

        move_choice = int(
            input("Type the number associated with the action you want to preform: ")
        )

        if move_choice == 1:
            current_room == "sewer entrance"

        elif move_choice == 2:
            current_room = "entryway"

    elif current_room == "sewer entrance":

    elif current_room == "slimy room":


print("You died!")

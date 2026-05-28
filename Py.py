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

# Enemies:
enemy_type = "Slime"
enemy_name = "Green Slime"
enemy_health = 10
enemy_damage = 0
enemy_exp = random.randint(5, 10)
#thinking to add a loot system that is more than gold. Go ahead and set variable to that. For now probably just gold.
enemy_loot = random.randint(1, 10)

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

        print("You enter through the iron gate. The path slopes downward. you begin to hear dripping water and the smell of stagnat water and something acrid. As you hit the bottom of the slope a sewer system sprawls out before you. You can see tunnels leading off to the left, the right, and infront of you.")
        print("1. Move to the left")
        print("2. Move to the right")
        print("3. Continue forward.")
        print("4. Go back")
        print("5. Search the area")

        move_choice = int(
            input("Type the number associated with the action you want to preform: ")
        )

        if move_choice == 1:
            current_room = "slimy room"

        elif move_choice == 2:
            current_room =

        elif move_choice == 3:
            current_room =

        elif move_choice == 4:
            current_room =
            
        elif move_choice == 5:
            print("A green blob rolls infront of you. The blob suddenly shudders and jumps at you!")

            while enemy_health > 0 and char_health > 0:


                print("1. Attack")
                print("2. Defend")
                print("3. Run")

                char_choice = int(input("Type the number associated with the action you want to preform: "))

                if char_choice == 1:
                        damage = random.randint(1, 3) + char_str
                        enemy_health -= damage
                        
                        if enemy_health > 0:
                            print(f"You dealt {damage} to the Green Slime.")
                        
                        else:
                            print("You killed the slime!")
                            char_exp += enemy_exp
                            gold += enemy_loot
                            print(f"You gained {enemy_exp}EXP and {enemy_loot}gold.")
                
                elif char_choice == 2:
                    print("You take a defensive stance.")
                    print("The Slime attacks you!")
                    enemy_damage = random.randint(1, 3)
                    char_health -= enemy_damage - char_con
                        
                    if char_health > 0:
                        print(f"You take {enemy_damage} damage. You were able to block {char_con} due to your defensive stance")

                    else:
                        print(f"You take {enemy_damage} damage. You have died.")

    elif current_room == "slimy room":










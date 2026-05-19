import random

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

elif class_choice == "2":
    char_class = "Mage"

elif class_choice == "3":
    char_class = "Rogue"

elif class_choice == "4":
    char_class = "Archer"

elif class_choice == "5":
    char_class = "Cleric"

else:
    char_class = "Peasant"

roll1 = random.randint(1, 20)
roll2 = random.randint(1, 20)

health = roll1 + roll2 - 7

gold = 0

print(f"{char_class} {char_name} enters the dungeon with {health} HP! In front of you expands a large entryway. There is a door infront of you and to your left." )

print("What do you do?")
print("1. Move Forward")
print("2. Move Left")
print("3. Loot the room")

move_choice = input("Type the number associated with the action you want to preform")

if move_choice == "1":
    print("You move to the door infront of you. It is a large oaken door with a brass knob. Beyond the door you hear the sound of a fire and low murmurs you can't quite make out.")

elif move_choice == "2":
   print("You move to the left. Blocking your way is a small wrought iron gate. The latch is open. You could push it open easily.")

elif move_choice == "3":
    roll_loot = random.randint(1, 100)
    gold += roll_loot
    print(f"You look around the room and find a leather pouch. When you pick it up you hear the jingle of coins. Upon opening you find {roll_loot} gold. You now have {gold} gold.")

else:
    move_choice == ""

print(move_choice)
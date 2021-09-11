
ASCII_TREASURE_ART = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."'` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''


def choose_colours() -> None:
    """Asks the player to pick a door colour."""
    print("\n\nYou arrive at the island unharmed. There is a house with 3 doors of different colours.")
    print(
        "\nDoor Colours:\033[91m Red\033[0m,\033[93m Yellow\033[0m,\033[94m Blue\033[0m")

    colours = ["red", "yellow", "blue"]

    while True:
        colour_choice = input("\nChoose a colour: ").lower()
        if colour_choice in colours[:1]:
            print("\nIt's a room full of fire. Game Over.\n")
            break
        elif colour_choice in colours[:2]:
            print("\nYou found the treasure! You Win!\n")
            break
        elif colour_choice in colours[-1]:
            print("\nYou enter a room of beasts. Game Over.\n")
            break
        else:
            print("\nRed, Yellow, and Blue Only!")


def ask_wait_or_swim() -> None:
    """Asks the player to choose to wait or swim."""
    print("\n\nYou've come to a lake. There is an island in the middle of the lake.")
    print(
        "\nType\033[1m 'wait'\033[0m to wait for a boat. Type\033[1m 'swim'\033[0m to swim across.")

    while True:
        wait_or_swim = input("\nWait or Swim: ").lower()
        if wait_or_swim == "swim":
            print("\nYou get attacked by an angry trout. Game Over.\n")
            break
        elif wait_or_swim == "wait":
            choose_colours()
            break
        else:
            print("\nWait or Swim Only!")


def ask_left_right() -> None:
    """Asks the player to choose left or right."""
    while True:
        print("\n\nYou are at a cross road, and you can only go left or right. Where do you want to go?")
        left_or_right = input("\nLeft / Right: ").lower()
        if left_or_right == "right":
            print("\nYou fell into a hole. Game Over.\n")
            break
        elif left_or_right == "left":
            ask_wait_or_swim()
            break
        else:
            print("\nLeft or Right Only!")


def play_game():
    """Starts the game."""
    print(ASCII_TREASURE_ART)
    print("\nWelcome to Treasure Island.")
    print("\nYour mission is to find the treasure.")

    ask_left_right()


if __name__ == "__main__":
    play_game()

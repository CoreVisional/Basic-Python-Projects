
import random

name = input("\n\nEnter your username: ")

print("\n\nWelcome to Guess The Number, " + name)

while True:
    try:
        # User can set the number they want to guess up to
        # They may find it difficult to win the game if they set their upper bound to a larger number
        upper_bound = int(input("\n\nEnter a number for an upper bound: "))
        break
    except ValueError:
        print("\nInvalid value. \nInput must be an integer number.")

random_num = random.randint(1, upper_bound)

# Player has not yet made a guess, so guess_num is set to None by default
guess_num = None

# Number of times for the user to get the correct number
guess_count = 0

# Number of times that user can guess the number
guess_limit = 3

print("\n\tYou will only have", guess_limit, "tries to guess the number.\n")

# To simplify if/else in determining the correct answers from the user input
# User can retry or keep playing the game when answering the prompt with any of the values in choice_yes
# Entering any of the values in choice_no will exit the program
choice_yes = ["Yes", "yes", "Y", "y"]
choice_no = ["No", "no", "N", "n"]

while guess_count < guess_limit:
    guess_num = int(input("\n\nEnter a number between 1 and " + str(upper_bound) + ": "))
    guess_count += 1
    if guess_num == random_num:
        print("\n\n\U0001F44F Congratulation, you guessed the number!\U0001F44F")
        if guess_count == 1 and guess_num == random_num:
            print("\nIt took you", guess_count, "try to guess the number.\n")
        elif guess_count == guess_limit and guess_num == random_num:
            print("\nNice One! You guessed the number on your last try.")
        else:    
            print("\nIt took you", guess_count, "tries to guess the number.\n")

        keep_playing = True
        
        while keep_playing:
            play_again = input("\n\nWould you like to play again? (Y/N): ")
            if play_again in choice_yes:
                keep_playing = False
                upper_bound = int(input("\n\nEnter a number for an upper bound: "))
                guess_count = 0
            elif play_again in choice_no:
                exit()
            else:
                print("\n\nInvalid input. Make sure you enter a valid response.")

    elif guess_num > random_num:
        print("Your guessing number is too high. Try guessing lower.")
    elif guess_num < random_num:
        print("Your guessing number is too low. Try guessing higher.")

    if guess_count >= guess_limit:
        print("\n\nSorry, you lost the game. You ran out of guesses. Better luck next time!")

        retry_game = True

        while retry_game:
            retry = input("\n\nDo you want to retry? (Y/N): ")
            if retry in choice_yes:
                guess_count = 0
                retry_game = False
            elif retry in choice_no:
                exit()
            else:
                print("\nPlease enter a valid input.")

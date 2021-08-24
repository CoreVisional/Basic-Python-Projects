
import random


def welcome_user():
    
    while True:
        name = input("\n\nEnter your username: ")

        if name != "":
            print("\n\nWelcome to Guess The Number, " + name)
            return name
        else:
            print("\nUsername Required!")


def validate_input(user_input):

    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("\n\nValue must be an integer. \n\nTry again.")

            
def get_upper_bound():

    while True:
        guess_number_maximum = validate_input("\n\nEnter a number for an upper bound: ")

        if guess_number_maximum < 1:
            print("\nYour upper bound must be greater than one.")
        else:
            return guess_number_maximum


def ask_user_yes_no(yes_no_question):

    choice_yes = ['yes', 'y']
    choice_no = ['no', 'n']

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in choice_yes:
            return True
        elif user_choice in choice_no:
            return False
        else:
            print("\n\nInvalid Input. Try again.")


GUESS_LIMIT = 3
 

def play_game(upper_bound, player_name):

    guess_count = 0

    random_number = random.randint(1, upper_bound)

    while True:
        user_number = validate_input("\n\nGuess the number between 1 and " + str(upper_bound) + ": ")
        guess_count += 1
    
        if user_number == random_number:
            print(f"\n\n\U0001F44F Congratulation, {player_name}, you guessed the number!\U0001F44F")
            count_guess_attempt(guess_count)
            return True
        elif user_number > random_number:
            print("Your guessing number is too high. Try guessing lower.")
        else:
            print("Your guessing number is too low. Try guessing higher.")
        
        if guess_count >= GUESS_LIMIT:
            print(f"\n\nSorry, {player_name}, you lost the game. You ran out of guesses. Better luck next time!")
            return False


def count_guess_attempt(guess_attempt):

    if guess_attempt == 1:
        print(f"\nIt took you {guess_attempt} try to guess the number.\n")
    elif guess_attempt == GUESS_LIMIT:
        print("\nNice One! You guessed the number on your last try.")
    else:    
        print(f"\nIt took you {guess_attempt} tries to guess the number.\n")


def should_play_again():

    user_name = welcome_user()

    may_change_upper_limit = True

    while True:
        if may_change_upper_limit:
            upper_limit = get_upper_bound()

        may_change_upper_limit = play_game(upper_limit, user_name)

        if not ask_user_yes_no("\n\nWould you like to play again? (Y/N): "):
            print("\n\nExiting game...\n\n")
            exit()


should_play_again()

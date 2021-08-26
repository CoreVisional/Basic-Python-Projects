
import random


def welcome_user():
    """Ask the user to enter their username as part of welcoming
    the user to the game.

    This is repeated until the user has provided a username to the program.
    Prints a greeting message along with the player's username.

    """
    while True:
        name = input("\n\nEnter your username: ")

        if name != "":
            print("\n\nWelcome to Guess The Number, " + name)
            return name
        else:
            print("\nUsername Required!")


def validate_input(user_input):
    """Check the user input for a ValueError.

    Prints a message when a ValueError occured.

    """
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("\n\nValue must be an integer. \n\nTry again.")


def get_upper_bound():
    """Ask the player to set the number that they want to guess up to.

    They may find it difficult to win the game if they set their
    upper bound to a larger number.

    If they enter anything that is not an integer value,
    then a warning message will appear.

    The game will ask the user to set a number for their upper bound again.

    This will be repeated until the user has entered a valid input.

    """
    while True:
        guess_number_maximum = validate_input(
            "\n\nEnter a number for an upper bound: ")

        if guess_number_maximum < 1:
            print("\nYour upper bound must be greater than one.")
        else:
            return guess_number_maximum


def ask_user_yes_no(yes_no_question):
    """Simplify if/else in determining the correct answers from the user input.

    Returns True if the user answer the prompt with
    any of the values in choice_yes.

    Returns False if the user enters any of the values in choice_no.

    """
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


# Indicate the number of times that the user can guess the number.
GUESS_LIMIT = 3


def play_game(upper_bound, player_name):
    """
    Keep count of the number of times it takes the
    user to get the correct number.

    Increments it by 1 for each attempt by the user.

    Sets the starting range of number to 1 with the ending range set
    by the user from get_upper_bound function.

    The guessing range of number is between 1 and up to the
    number that the user has set.

    Checks the user's guessed number and prints out a message
    to indicate that the guessed number is either too high
    or too low than the random number.

    Returns True if the user won the game.
    Returns False if the user lost the game.

    Prints out a winning message once the user have
    guessed the number or out of guesses.

    """
    guess_count = 0

    random_number = random.randint(1, upper_bound)

    while True:
        user_number = validate_input(
            "\n\nGuess the number between 1 and " + str(upper_bound) + ": ")

        guess_count += 1

        if user_number == random_number:
            print(f"\n\n\U0001F44F Congratulation, {player_name}, "
                  "you guessed the number!\U0001F44F")

            count_guess_attempt(guess_count)

            return True

        elif user_number > random_number:
            print("Your guessing number is too high. Try guessing lower.")
        else:
            print("Your guessing number is too low. Try guessing higher.")

        if guess_count >= GUESS_LIMIT:
            print(f"\n\nSorry, {player_name}, you lost the game. "
                  "You ran out of guesses. Better luck next time!")
            return False


def count_guess_attempt(guess_attempt):
    """Count the number of times it takes the user to guess the number.

    User can only guess the number 3 times.

    Prints a message containing the number of times it
    took the user to guessed the number.

    """
    if guess_attempt == 1:
        print(f"\nIt took you {guess_attempt} try to guess the number.\n")
    elif guess_attempt == GUESS_LIMIT:
        print("\nNice One! You guessed the number on your last try.")
    else:
        print(f"\nIt took you {guess_attempt} tries to guess the number.\n")


def should_play_again():
    """Call greet_user function to greet the user
    when the program first executes.

    Starts round of Guess The Number.

    Asks the user if they want to play again.

    Restarts the program if play_game returns True
    and user wants to play again.

    Lets the user guess the number again if play_game
    returns False and user wants a try again.

    Exits the program if the user does not want to continue with the program.

    """
    user_name = welcome_user()

    may_change_upper_limit = True

    while True:
        if may_change_upper_limit:
            upper_limit = get_upper_bound()

        may_change_upper_limit = play_game(upper_limit, user_name)

        if not ask_user_yes_no("\n\nWould you like to play again? (Y/N): "):
            print("\n\nExiting game...\n\n")
            break


should_play_again()

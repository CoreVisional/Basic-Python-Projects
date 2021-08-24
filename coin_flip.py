
import random


# Indicate all possible coin sides
COIN_SIDES = ["heads", "tails"]


def greet_user():
    """Ask the user to enter their username as
    part of welcoming them into the game.

    This is repeated until the user keyed in their username.

    Prints a greeting message along with the player's username.

    Returns a string containing the player's username.

    """
    while True:
        name = input("\n\nEnter your username: ")

        if name != "":
            print("\n\nWelcome to Flip The Coin, " + name)
            return name

        print("\nUsername Required!")


def ask_user_yes_no(yes_no_question):
    """Simplify if/else in determining the correct answers from the user input.

    Returns True if the user answer the prompt with
    any of the values in choice_yes.

    Returns False if the user enters any of the values in choice_no.

    """
    choice_yes = ["yes", 'y']
    choice_no = ["no", 'n']

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in choice_yes:
            return True
        elif user_choice in choice_no:
            return False

        print("\n\nInvalid Input. Try again.")


def flip_coin():
    """Returns a randomized coin side."""
    return random.choice(COIN_SIDES)


def get_player_guess():
    """Prompt the player to input "Heads" or "Tails".

    This process execution is repeated until a valid input is received.

    Returns a string containing the player's input.

    """
    while True:
        player_guess = input("\nHeads or Tails?: ").lower()

        if player_guess in COIN_SIDES:
            return player_guess

        print("\nHeads or Tails only!")


def start_game(username):
    """Play 3 rounds of Flip The Coin.

    Counts the number of times the player wins or loses.
    Increments the counter by 1 for each win and loss.

    Prints out a message indicating which round the player
    is currently in and the number of rounds left to play.

    Increments the round by 1 after the end of each round.

    Prints "Round Won" if round_result is True, or
    "Round Lost" if round_result is False.

    Prints the number of wins and losses after the game ends, then prints a
    message to the player for winning or losing all the rounds.

    """
    game_round = 3

    wins, losses = (0, 0)

    for count_round in range(game_round):
        print(f"\n\nStarting round {count_round + 1} of {game_round}")
        round_result = run_round()

        if round_result:
            print(f"\n\n** Round Won **".upper())
            wins += 1
        else:
            print("\n\n** Round Lost **".upper())
            losses += 1

    print_game_result(wins, losses, game_round, username)


def run_round():
    """Run a single round of the game and returns a True / False result.

    Prints out both results containing the side of the coin that the player
    has flipped and the coin side that the player has guessed.

    """
    player_guess = get_player_guess()

    actual_flip = flip_coin()

    round_outcome = player_guess == actual_flip

    print(f"\n\nYou flipped: {player_guess}")
    print(f"\nYou guessed: {actual_flip}")

    return round_outcome


def print_game_result(round_won, round_lost, total_round, player):
    """Print out a scoreboard showing the number of rounds
    that the player has won and lost.

    Prints a message to the player if they won or lost all the rounds.

    """
    print(f"\n\nRound Won: {round_won} \tRound Lost: {round_lost}")

    if round_won == total_round:
        print(f"\n\nCongratulation, {player}, you won all the rounds!")
    elif round_lost == total_round:
        print(f"\n\nSorry, {player}, you lost all the rounds.")
        print("\n\nBetter luck next time!")


def should_play_again():
    """Call greet_user function to greet the user when the
    program first executes.

    Starts 3 rounds of Flip The Coin.

    Asks the user if they want to play again.

    Restarts round if the player wants to play again.

    Exits the program if the user does not want to play again.

    """
    player_name = greet_user()

    while True:
        start_game(player_name)

        if not ask_user_yes_no("\n\nWould you like to play again? (Y/N): "):
            print("\n\n-----Program Exited-----\n\n")
            break


should_play_again()

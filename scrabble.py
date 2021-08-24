
from string import ascii_letters


def get_word():
    """
    Asks the user to input a word.
    Returns a string containing the user's input. 
    """

    user_word = input("\n\nEnter a word: ")

    return user_word


def ask_user_yes_no(yes_no_question):
    """
    To simplify if/else in determining the correct answers from the user input.
    Returns True if the user answer the prompt with any of the values in choice_yes.
    Returns False if the user enters any of the values in choice_no
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


def generate_letters():
    """
    Loops through all the alphabet letters.
    Splits the letters and add it into the empty list.
    Returns a list of splitted alphabet letters.
    """

    letters = []

    for char in ascii_letters:
        letters += char.split()

    return letters


def generate_points():
    """
    A list of integers as a point for each letter in the alphabet.
    Multiplies the list by 2 to match the length of generate_letters function.
    Returns the extended list of integers.
    """

    points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10] * 2

    return points


def map_letters_points():
    """
    Calls generate_letters function and assign the returned value to letter_list
    Calls generate_points function and assign the returned value to point_list

    Maps each letter to point with letter being the key and point as the value.

    Handles blank tiles by assigning 0 to letter_to_points if the user did not input anything.

    Returns a dictionary that has the elements of letter_list as keys and the elements of point_list as values.
    """
    
    letter_list = generate_letters()
    point_list = generate_points()

    letter_to_points = {letter: point for letter, point in zip(letter_list, point_list)}

    letter_to_points[" "] = 0

    return letter_to_points


def score_word(word):
    """
    Calls map_letters_points function and assign the returned value to letter_points

    Sets point_total equals to 0

    Iterates through the letters in word and adds the point value of each letter to point_total from
    letter_points dictionary.

    Adds 0 to point_total if the letter is not found in letter_points.

    Returns an integer of the total points that the user has scored with the give word. 
    """

    letter_points = map_letters_points()
    
    total_point = 0

    for key in word:
        total_point += letter_points.get(key, 0)

    return total_point


def play_word():
    """
    Gets a word input from the user.
    Sums the point of each letter from the given word.

    Pluralizes the word "point" if the scored_points is either 0 or more than 1.

    Asks the user if they want play again.
    Asks the user to input word if the user wants to play again.
    Exits the program if the user does not want to continue with the program.
    """

    while True:

        player_word = get_word()

        scored_points = score_word(player_word)

        if scored_points == 1:
            print(f"\nYour word scores {score_word(player_word)} point!\n")
        else:
            print(f"\nYour word scores {score_word(player_word)} points!\n")

        if not ask_user_yes_no("\nWould you like to play again? (Y/N): "):
            print("\n\nExiting program...\n\n")
            break


play_word()

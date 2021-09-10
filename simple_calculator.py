
import operator

from functools import reduce

import doctest


# Display a list of math operators as options for user to select.
MATH_OPERATIONS = """\n\nList of math operations:

1. Addition (+)

2. Subtraction (-)

3. Multiplication (*)

4. Division (/)

5. Exponentiation (**)

"""


# A dictionary dispatch that contain options of operations
# to perform the calculation.
OPERATIONS = {
    1: operator.add,
    2: operator.sub,
    3: operator.mul,
    4: operator.truediv,
    5: operator.pow,
}


def ask_user_yes_no(yes_no_question) -> bool:
    """Simplifies if/else to determine the correct answers from the user input.

    Args:
        yes_no_question: A string that asks user a yes or no question.

    Returns:
        True if the user's answer is in CHOICE_YES,
        and False otherwise.

        Prints a message to the user if their input are not similar
        to the ones in CHOICE_YES and CHOICE_NO.

    """
    CHOICE_YES = ("yes", 'y')
    CHOICE_NO = ("no", 'n')

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in CHOICE_YES:
            return True
        elif user_choice in CHOICE_NO:
            return False
        else:
            print("\nInvalid Input. Try again.")


def count_number_input():
    """Count the amount of numbers that the user wants to calculate.

    Prints out a message if ValueError occurs.

    """
    while True:
        try:
            count_input = int(
                input("\nHow many number would you like to calculate?: "))
        except ValueError:
            print("\nINVALID INPUT - Field must not be blank or "
                  "contained non-integer or non-numerical values.")
        else:
            return count_input


def get_number_list():
    """Ask the user to input that they wish to calculate.
    
    Displays an error message if the prompt contains a null
    or non-numerical values.

    """
    input_amount = count_number_input()

    while True:
        try:
            numbers_list = [float(input("\nNumbers: "))
                            for _ in range(input_amount)]
        except ValueError:
            print("\nInvalid input, try again.")
            print("\nPrompts must not contain a null or non-numerical values.")
        else:
            return numbers_list


def select_choice():
    """Print out a list of math operations.

    Asks the user to select an option to use in the calculation.

    Checks user's selection for ValueError and skip if none is found.

    Prints out a message if the user has selected an option
    beyond the specified range of options.

    """
    print(MATH_OPERATIONS)

    while True:
        try:
            user_choice = int(
                input("Select an option | 1 | 2 | 3 | 4 | 5 |: "))
        except ValueError:
            print("\nInvalid Input.\n")
            continue

        if user_choice <= 0 or user_choice > 5:
            print("\nOption selected must be from 1 to 5 only!\n")
        else:
            return user_choice


def calculate(numbers, choice):
    """Apply operations across all numbers and return the result.

    >>> calculate([2.0, 2.0], 1)
    4.0

    >>> calculate([5.0, 3.0], 2)
    2.0

    >>> calculate([5.0, 5.0], 3)
    25.0

    >>> calculate([9.0, 3.0], 4)
    3.0

    >>> calculate([5, 0], 4)
    <BLANKLINE>
    Math ERROR - Division by 0

    >>> calculate([4.0, 4.0], 5)
    256.0

    """
    try:
        return reduce(OPERATIONS[choice], numbers)
    except ZeroDivisionError:
        print("\nMath ERROR - Division by 0")


def format_value(option: int) -> str:
    """Return the result unchanged if user selects the 4th option (division).

    Leaves the result of a division as a float number using
    the '' (None) format specifier.

    Formats the result on the rest of the operations using
    the 'n' format specifier.

    """
    return 'n' if option != 4 else ''


def start_program():
    """Start the program and print out the result.

    Performs a calculation on those numbers.

    Calls format_number function to format the result before printing it out.

    """
    user_number = get_number_list()

    user_choice = select_choice()

    calculation_result = calculate(user_number, user_choice)

    result_format = format_value(user_choice)

    print(f"\nResult: {calculation_result:{result_format}}")


def should_calculate_again():
    """Ask the user if they want to calculate again.

    Restarts the program if ask_user_yes_no returns True.

    Exits the program telling the user that the program has exited
    if ask_user_yes_no returns False.

    """
    while True:

        start_program()

        if not ask_user_yes_no("\n\nWould you like to perform "
                               "another calculation? (Y/N): "):
            print("\n\n-----Program Exited-----\n")
            break


doctest.testmod()

should_calculate_again()

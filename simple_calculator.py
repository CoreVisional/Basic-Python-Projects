
# List of math operators that the user can choose to perform their calculation.
MATH_OPERATIONS = """\n\nList of math operations:

1. Addition (+)

2. Subtraction (-)

3. Multiplication (*)

4. Division (/)

5. Exponentiation (**)

"""


def get_number_input():
    """Ask the user to input first and second number for calculation.

    This is repeated until the user has given numerical values in both prompts.

    Returns the first and second number.

    """
    while True:
        try:
            first_num = float(input("\nInput 1st Number: "))
            second_num = float(input("\nInput 2nd Number: "))
        except ValueError:
            print("\n\nINVALID INPUT - Field must not be blank or contained non-numerical values.\n")
        else:
            return check_int_float(first_num), check_int_float(second_num)


def check_int_float(number: float) -> float:
    """Check if the numbers given by the user is an int or a float."""

    if number.is_integer(): number = int(number)

    return number


def select_choice():
    """Ask the user to select an operator to use in the calculation.

    Prints out a list of math operations.
    
    Check user's selection for ValueError and skip if none is found.

    Prints out a message if the user has selected an option beyond the specified range of options.

    """
    print(MATH_OPERATIONS)

    while True:
        try:
            user_choice = int(input("Select an option | 1 | 2 | 3 | 4 | 5 |: "))
        except ValueError:
            print("\nInvalid Input.\n")
            continue
        
        if user_choice > 5:
            print("\nOption selected must be from 1 to 5 only!\n")
        else:
            return user_choice


# A function that sums two numbers
def add(x, y):

    return x + y


# A function that substracts two numbers
def subtract(x, y):

    return x - y


# A function that multiplies two numbers
def multiply(x, y):

    return x * y


def divide(x, y):
    """Divide two numbers and print out an 
    error message if division by 0 is found.
    """
    try:
        return x / y
    except ZeroDivisionError:
        print("\nMath ERROR - Division by 0")


# A function that raises a number to the power of another number
def exponentiate(x, y):

    return x ** y


def calculate(num_1, num_2):
    """Determine operations and display the result.

    Prints out the division equation if the returned value is not None.

    Calculation:

        >>> add(5, 1)
        6

        >>> subtract(6, 3)
        3

        >>> multiply(2, 2)
        4

        >>> divide(9, 6)
        1.5

        >>> divide(5, 0)
        <BLANKLINE>
        Math ERROR - Division by 0

        >>> exponentiate(2, 3)
        8

    """
    choice = select_choice()

    if choice == 1:
        print(f"\n{num_1} + {num_2} = {add(num_1, num_2)}")
    elif choice == 2:
        print(f"\n{num_1} - {num_2} = {subtract(num_1, num_2)}")
    elif choice == 3:
        print(f"\n{num_1} * {num_2} = {multiply(num_1, num_2)}")
    elif choice == 4:
        div_result = divide(num_1, num_2)
        if div_result:
            print(f"\n{num_1} / {num_2} = {divide(num_1, num_2)}")
    elif choice == 5:
        print(f"\n{num_1} ** {num_2} = {exponentiate(num_1, num_2)}")


def run_program():
    """Start the program by asking the user to input their numbers first
    and then perform a calculation on those numbers.
    """
    user_num_1, user_num_2 = get_number_input()

    calculate(user_num_1, user_num_2)


run_program()

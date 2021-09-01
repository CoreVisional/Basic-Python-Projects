
from typing import Union
from ast import literal_eval
import doctest


# Displays a list of options to the user that will
# calculate the measures of central tendency.
MEASUREMENTS = """\n\nSelect A Calculation:

1. Mean

2. Median

3. Mode

"""


def ask_user_yes_no(yes_no_question: str) -> bool:
    """Simplifies if/else to determine the correct answers from the user input.

    Args:
        yes_no_question: A string that asks user a yes or no question.

    Returns:
        True if the user's answer is in choice_yes,
        and False otherwise.

        Prints a message to the user if their input are not similar
        to the ones in choice_yes and choice_no.

    """
    choice_yes = ('yes', 'y')
    choice_no = ('no', 'n')

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in choice_yes:
            return True
        elif user_choice in choice_no:
            return False
        else:
            print("\n\nInvalid Input. Try again.")


def get_number_dataset() -> list:
    """Asks the user to input the dataset that is needed to
    calculate mean, median, and mode.

    Returns:
        A list of integer or float numbers, depending on the data
        type present in the dataset.

    Prints out a message if the user tries to give non-numerical
    values or providing less than 2 values.

    """
    while True:
        user_number_input = input("\nEnter Number Dataset: ").replace(
            ",", " ").split()
        try:
            number_dataset = [literal_eval(num) for num in user_number_input]
        except ValueError:
            print(f"\nNumbers Only For Mean and Median!")
            print(f"\nYour Input: {''.join(user_number_input).strip('')}")
            continue

        if len(number_dataset) < 2:
            print("\nPlease enter at least 2 values.")
        else:
            return number_dataset


def get_mode_dataset() -> list[str]:
    """Asks the user to input the values into the dataset
    in order to get the frequency of those values.

    Returns:
        A list of strings containing the values in a data set.

    Prints out a message if the dataset contains less than 2 values.

    """
    user_mode_input = input("\nEnter Mode Dataset: ").replace(",", " ").split()

    if len(user_mode_input) < 2:
        print("\nPlease enter at least 2 values.")
    else:
        return user_mode_input


def select_choice() -> int:
    """Asks the user to select an option that is used to calculate
    the mean, median, or mode.

    Returns:
        An integer of the user's selection.

    Prints out a list of math operations.

    Prints out a message if the user inputs a value other than integer or
    selects an option that is beyond the specified range of options.

    """
    print(MEASUREMENTS)

    while True:
        user_choice = input("Select an option | 1 | 2 | 3 |: ")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print(f"\nInvalid Input: {user_choice!r}\n")
            continue

        if user_choice > 3:
            print("\nOption selected must be from 1 to 5 only!\n")
        else:
            return user_choice


def calculate_mean(numbers_list: list) -> float:
    """Calculates mean.

    Args:
        numbers_list: A list of integer or float numbers.

    Returns:
        A float number due to division.

    Examples:

        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0

        >>> calculate_mean([2.4, 6.5, 3.1, 9.2, 13.5])
        6.94

        >>> calculate_mean([535, 120, 76, 32, 45])
        161.6

    """
    return sum(numbers_list) / len(numbers_list)


def calculate_median(numbers_list: list) -> Union[int, float]:
    """Calculates median.

    Args:
        numbers_list: A list of integer or float numbers.

    Returns:
        An integer or a float number. The result of the calculation
        is determined by the given dataset.

    Examples:

        >>> calculate_median([105, 321, 95, 64, 31])
        95

        >>> calculate_median([1.0, 2.0, 3, 4.0, 5])
        3

        >>> calculate_median([3.2, 12.5, 20, 21.2, 32, 51])
        20.6

    """
    num_length = len(numbers_list)

    numbers_list.sort()

    if not num_length % 2:
        calc_median_1 = numbers_list[num_length//2]
        calc_median_2 = numbers_list[num_length//2 - 1]
        median = (calc_median_1 + calc_median_2)/2
    else:
        median = numbers_list[num_length//2]

    return median


def find_mode(items_list: list) -> list[str]:
    """Finds the frequency of a particular value.

    Args:
        items_list: A list strings.

    Returns:

        An int or a float number or a string
        if trivial cases occurs.

        A message telling the user that no mode was found
        if the user gave a list of elements
        that occur only once.

        A list containing a string of element/s.

    Examples:

        >>> find_mode(['830', '476', '5664', 'Smash Mouth'])
        'No Mode Found!'

        >>> find_mode(['Shrek', 'Shrek', 'is', 'life'])
        'Shrek'

        >>> find_mode(['3', '3', '3'])
        '3'

        >>> find_mode(['nike', 'nike', 'adidas', '88', '25', '88'])
        ['nike', '88']

    """
    counter = {element: items_list.count(element)
               for element in set(items_list)}

    if len(set(items_list)) == 1:
        return set(items_list).pop()
    elif len(counts := set(counter.values())) == 1:
        return "No Mode Found!"

    mode = [key for key, count in counter.items() if count == max(counts)]

    return mode if len(mode) > 1 else mode.pop()


def print_result(choice: int) -> None:
    """Determines the options selected and display the result.

    Args:
        choice: An integer to determine which type of calculation
                based on the user's selection.

    Formats the result of mean and mode calculation
    using locale aware separator.

    """
    if choice == 1 or choice == 2:
        mean_median_dataset = get_number_dataset()
    elif choice == 3:
        mode_dataset = get_mode_dataset()

    if choice == 1:
        print(f"\nMean: {calculate_mean(mean_median_dataset):n}")
    elif choice == 2:
        print(f"\nMedian: {calculate_median(mean_median_dataset)}")
    elif choice == 3:
        print(f"\nMode: {find_mode(mode_dataset)}")


def should_calculate_again():
    """Asks the user if they want to calculate again.

    Restarts program if True, else prints a message
    telling the user that the program has exited.

    """
    if ask_user_yes_no("\n\nWould you like to perform "
                       "another calculation? (Y/N): "):
        return start_calculation()
    else:
        print("\n\n-----Program Exited-----\n")


def start_calculation() -> None:
    """A function that initializes the calling of the
    other functions to start the program.

    """
    user_option = select_choice()

    print_result(user_option)

    should_calculate_again()


def main():

    if __name__ == "__main__":
        doctest.testmod()
        start_calculation()


main()

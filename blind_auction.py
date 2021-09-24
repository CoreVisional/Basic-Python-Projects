
from os import system

from typing import Union


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


def get_bidder_name() -> str:
    """Asks the bidder to type in their name.

    Returns:
        A string containing the bidder's name.

    This is repeated until the bidder has provided a 
    name to the program.

    """
    while True:
        name = input("\n\nEnter your name: ")

        if not name:
            print("\nName Required!")
        else:
            break

    return name


def get_bidding_price() -> float:
    """Asks the bidder to enter their bidding price.

    Returns:
        A float number representing the bidder's price.

    This is repeated until the bidder has entered
    a bidding price into the program.

    """
    while True:
        price = input("\n\nEnter your bidding price: $")

        try:
            price = float(price)
        except ValueError:
            print(f"\nInvalid Input: {price!r}")
            continue
        else:
            return price


def get_highest_bid(bidding_record: dict) -> Union[tuple[str, float]]:
    """Finds the highest bidder and bidding amount.

    Args:
        bidding_record: A dictionary containing all the names of the
                        bidders and their bidding amounts.

    Returns:
        A tuple of string and a float number containing the name of the
        highest bidder and their bidding amount.

    """
    highest_bidder = max(bidding_record, key=bidding_record.get)

    bid_amounts = bidding_record.values()
    highest_bid = max(bid_amounts)

    return highest_bidder, highest_bid


def print_auction_winner(bidding_record: dict) -> None:
    """Prints out the auction winner and the bid amount.

    Args:
        bidding_record: A dictionary that contains the winner's name
                        and the winner's bidding amount.

    """
    auction_winner, bid_amount = get_highest_bid(bidding_record)

    print(f"\n\nThe winner of this auction is \033[1m{auction_winner}\033[0m with "
          f"a bid of \033[1m${bid_amount:n}\033[0m.\n")


def check_other_bidders() -> bool:
    """Asks the user if there are other bidders who
    would like to bid against the user.

    Returns:
        True if there are other bidders, False otherwise.

    """
    return ask_user_yes_no("\n\nAre there any other bidders? (Y/N): ")


def main() -> None:
    """Starts the program.

    Loops the program if there are other bidders, otherwise, prints the
    winner of the secret auction.

    """
    _ = system('cls')

    bids = {}

    while True:
        bidder_name = get_bidder_name()
        bid_price = get_bidding_price()

        bids[bidder_name] = bid_price

        if not check_other_bidders():
            break

    print_auction_winner(bids)


if __name__ == "__main__":
    main()

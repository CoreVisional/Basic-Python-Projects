
"""A CLI-based Bidding Game."""

from os import system


GAVEL_LOGO = r"""
                         ___________
                         \         /
                          )_______(
                          |'''''''|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )'''''''(
                         /_________\\
                       .-------------.
                      /_______________\\

"""


def ask_user_yes_no(yes_no_question) -> bool:
    """Simplifies if/else to determine the correct answers from the user input.

    Args:
        yes_no_question: A string that asks user a yes or no question.

    Returns:
        True if the user's answer is in choice_yes,
        and False otherwise.

        Prints a message to the user if their input are not similar
        to the ones in choice_yes and choice_no.

    """
    choice_yes = ("yes", 'y')
    choice_no = ("no", 'n')

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in choice_yes:
            return True

        if user_choice in choice_no:
            return False

        print("\nInvalid Input. Try again.")


def get_bidder_name() -> str:
    """Ask the bidder to type in their name.

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


def get_highest_bid(bidding_record: dict) -> tuple[str, float]:
    """Find the highest bidder and bidding amount.

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
    """Print out the auction winner and the bid amount.

    Args:
        bidding_record: A dictionary that contains the winner's name
                        and the winner's bidding amount.

    """
    auction_winner, bid_amount = get_highest_bid(bidding_record)

    print(f"\n\nThe winner of this auction is \033[1m{auction_winner}\033[0m with "
          f"a bid of \033[1m${bid_amount:n}\033[0m.\n")


def check_other_bidders() -> bool:
    """Ask the user if there are other bidders.

    Returns:
        True if there are other bidders, False otherwise.

    """
    return ask_user_yes_no("\n\nAre there any other bidders? (Y/N): ")


def main() -> None:
    """Start the program.

    Loops the program if there are other bidders, otherwise, prints the
    winner of the secret auction.

    """
    _ = system("clear")

    print(GAVEL_LOGO)

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


"""

*** PROJECT DESCRIPTION ***


Alex runs the biggest shipping company in the tri-county area, Alex’s Shippers.
He wants to make sure that every single one of his customers has the best,
and most affordable experience shipping their packages.

This program will take the weight of a package and determine the cheapest way
to ship that package using Alex’s Shippers.


Options for a customer to ship their package:

Ground Shipping           -   This shipping option has a small flat charge plus
                              a rate based on the weight of your package.

Ground Shipping Premium   -   This shipping option does not charge for weight,
                              but has a higher flat charge.

Drone Shipping            -   This shipping option has no flat charge, but the rate
                              is based on weight is triple the
                              rate of ground shipping.


---------------------------------------------------------------------------------------------------------------------------


Prices of all three shipping options.


Standard Ground Shipping:

Weight of Package	                        Price per Pound	            Flat Charge

2 lb or less	                                 $1.50	                   $20.00
Over 2 lb but less than or equal to 6 lb	     $3.00	                   $20.00
Over 6 lb but less than or equal to 10 lb	     $4.00	                   $20.00
Over 10 lb	                                   $4.75	                   $20.00


---------------------------------------------------------------------------------------------------------------------------


Premium Ground Shipping:

Flat Charge = $125


---------------------------------------------------------------------------------------------------------------------------


Drone Shipping:

Weight of Package	                        Price per Pound	            Flat Charge

2 lb or less	                                 $1.50	                   $0.00
Over 2 lb but less than or equal to 6 lb	     $3.00	                   $0.00
Over 6 lb but less than or equal to 10 lb	     $4.00	                   $0.00
Over 10 lb	                                   $4.75	                   $0.00

---------------------------------------------------------------------------------------------------------------------------
"""


def greet_customer():
    """Ask the customer to enter their name as part
    of welcoming them Alex's Shippers.

    This is repeated until the customer keyed in their name.

    Prints a greeting message along with the customer's name.

    Prints the company's mission statement.

    """
    while True:
        name = input("\n\nEnter your name: ")

        if name != "":
            print(f"\n\nWelcome to Alex's Shippers, {name}.")
            print("\nWe take pride in providing our customers get the best, "
                  "and most affordable experience shipping their packages.")
            return name

        print("\nName Required!")


def validate_user_input(prompt_text):
    """Check the user input for a ValueError.

    Prints a message when a ValueError occured.

    """
    while True:
        try:
            return int(float(input(prompt_text)))
        except ValueError:
            print("\n\nValue must be a number. \n\nTry again.")


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


def get_package_weight():
    """Ask the customer to enter their package's weight.

    A warning message will be displayed to the customer if the
    customer did not enter anything into the prompt.

    Returns the weight of the customer's item.

    """
    while True:

        package_weight = validate_user_input(
            "\n\nEnter your package's weight: ")

        if package_weight == "":
            print("\nPackage Weight Required!")
        return package_weight


# Flat charge of using Ground Shipping
FLAT_CHARGE = 20

# Flat charge of using Ground Shipping Premium
PREMIUM_GROUND_SHIP = 125


def calculate_ground_shipping_cost(weight):
    """Calculate the shipping cost of using Ground Shipping."""
    if weight <= 2:
        return (weight*1.5) + FLAT_CHARGE
    elif weight > 2 and weight <= 6:
        return (weight*3) + FLAT_CHARGE
    elif weight > 6 and weight <= 10:
        return (weight*4) + FLAT_CHARGE
    else:
        return (weight*4.75) + FLAT_CHARGE


def calculate_drone_shipping_cost(weight):
    """Calculate the shipping cost of using Drone Shipping."""
    if weight <= 2:
        return weight * 4.5
    elif weight > 2 and weight <= 6:
        return weight * 9
    elif weight > 6 and weight <= 10:
        return weight * 12
    else:
        return weight * 14.25


def print_cheapest_shipping_option(total_package_weight, consumer_name):
    """Find the cheapest shipping option for the customer.

    Prints out a message to inform the customer that the program has found
    the best and affordable shipping method for them.

    Prints out the weight of the package.

    Prints out a message that tells the customer which
    shipping method is the cheapest.

    """
    ground_ship = calculate_ground_shipping_cost(total_package_weight)

    drone_ship = calculate_drone_shipping_cost(total_package_weight)

    print(f"\n\nGood news, {consumer_name}, we have found the perfect "
          "shipping method for you based on your package's weight.")
    print(f"\n\nPackage's Weight: {total_package_weight} lbs")

    if (ground_ship < PREMIUM_GROUND_SHIP) and (ground_ship < drone_ship):
        print("\n\nCheapest Shipping Method: Ground Shipping (Standard)")
    elif (PREMIUM_GROUND_SHIP < ground_ship and
          PREMIUM_GROUND_SHIP < drone_ship):
        print("\n\nCheapest Shipping Method: Ground Shipping (Premium)")
    else:
        print("\n\nCheapest Shipping Method: Drone Shipping")


def main():
    """Ask the user if they have more packages to calculate.

    Prompts the customer to enter their package's weight again if the customer
    has another package to ship, and wants to check which shipping method
    is the cheapest based on the package's weight.

    Exits the program if the customer does not have any more packages to ship.

    """
    customer_name = greet_customer()

    may_change_package_weight = True

    while True:
        if may_change_package_weight:
            customer_package = get_package_weight()

        print_cheapest_shipping_option(customer_package, customer_name)

        if not ask_user_yes_no("\n\nDo you have another "
                               "package to weight? (Y/N): "):
            print("\n\nExiting Program...\n\n")
            break


main()

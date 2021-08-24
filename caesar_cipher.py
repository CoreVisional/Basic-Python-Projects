
from string import ascii_letters, ascii_lowercase, ascii_uppercase


def get_mode():
    """Return a string containing the user's input.

    Asks the user if they want to encrypt or decrypt their message.

    This is repeated until a valid input is received.

    """
    while True:
        mode = input("\n\nEncrypt or Decrypt: ").lower()
        if mode in "encrypt e decrypt d".split():
            return mode
        else:
            print("\nInvalid input. Only 'encrypt', 'e', 'decrypt', or 'd'.")


def get_message():
    """Return a string containing the user's input.

    Calls get_mode to check if the user wants to encrypt or decrypt the message.

    Asks the user to enter the message for encryption or decryption.

    This is repeated until the user enters at least a character into the input prompt.

    """
    get_mode()

    while True:
        user_message = input("\nType your message: ")

        if user_message != "":
            return user_message
        
        print("\nInput must not be null.")
        

def get_key():
    """Return an integer containing the user's input.

    Asks the user to enter a key used for shifting the letters.

    This is repeated until the user enters a valid key.

    """
    key = 0

    while True:
        try:
            key = int(input("\nEnter a key number: "))
        except ValueError:
            print("\nInput must only be an integer.")
        else:
            return key


def ask_user_yes_no(yes_no_question):
    """Simplify if/else in determining the correct answers from the user input.

    Returns True if the user answer the prompt with any of the values in choice_yes.

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
        
        print("\n\nInvalid Input. Try again.")


def alphabet_position(shift):
    """Return the new shifted lowercase and uppercase alphabets.

    Shifts the lowercase and uppercase characters given a new key.

    """
    shifted_lowercase = ascii_lowercase[shift:] + ascii_lowercase[:shift]

    shifted_uppercase = ascii_uppercase[shift:] + ascii_uppercase[:shift]

    return shifted_lowercase, shifted_uppercase


def translate_message(message: str, offset):
    """Return a string of the encrypted message with 
    each character mapped to the given translation table.

    Rearranges the ordinal numbers of the alphabets 
    with the given offset including uppercase letters.

    """
    lowercase_alpha, uppercase_alpha = alphabet_position(offset)

    char_index = message.maketrans(ascii_letters, lowercase_alpha + uppercase_alpha)

    print(f"\n\nTranslated Message: {message.translate(char_index)}")


# def perform_brute_force(message):
#     """Perform a brute-force attack if the user 
#     does not know the offset to decrypt the message.

#     Prints every possible decryption key from 1 to 26 along with the decrypted message.

#     """
#     for char in range(1, 26):
#         print(f"Key: {char}")
#         print(f"\t{translate_message(message, char)}")


def should_translate_again():
    """Ask whether or not the user wants to encrypt ot decrypt again.

    Restarts the program if the user wants to perform further encryption or decryption.

    Exits the program if the user does not want to continue with the program.

    """
    while True:
        user_text, key_rotation = get_message(), get_key()
        
        translate_message(user_text, key_rotation)

        if not ask_user_yes_no("\n\nWould you like to encrypt or decrypt another message? (Y/N): "):
            print("\n\n-----Program Exited-----\n")
            break


should_translate_again()

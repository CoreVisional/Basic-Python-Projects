
from string import ascii_letters, ascii_lowercase, ascii_uppercase


CAESAR_CIPHER_ASCII_ART = """

           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

"""


def get_mode():
    """Return a string containing the user's input.

    Asks the user if they want to encrypt or decrypt their message.

    This is repeated until a valid input is received.

    """
    while True:
        mode = input("\nEncrypt or Decrypt: ").lower()
        if mode in "encrypt e decrypt d".split():
            return mode
        else:
            print("\nInvalid input. Only 'encrypt', 'e', 'decrypt', or 'd'.")


def get_message():
    """Return a string containing the user's input.

    Calls get_mode to check if the user wants
    to encrypt or decrypt the message.

    Asks the user to enter the message for encryption or decryption.

    This is repeated until the user enters at least a
    character into the input prompt.

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


def alphabet_position(shift):
    """Return the new shifted lowercase and uppercase alphabets.

    Shifts the lowercase and uppercase characters given a new key.

    """
    shifted_lowercase = ascii_lowercase[shift:] + ascii_lowercase[:shift]

    shifted_uppercase = ascii_uppercase[shift:] + ascii_uppercase[:shift]

    return shifted_lowercase, shifted_uppercase


def translate_message(message: str, offset):
    """Return a string of the encrypted message with each
    character mapped to the given translation table.

    Rearranges the ordinal numbers of the alphabets with
    the given offset including uppercase letters.

    """
    lowercase_alpha, uppercase_alpha = alphabet_position(offset)

    char_index = message.maketrans(
        ascii_letters, lowercase_alpha + uppercase_alpha)

    print(f"\n\nTranslated Message: {message.translate(char_index)}")


# def perform_brute_force(message):
#     """Perform a brute-force attack if the user does
#     not know the offset to decrypt the message.

#     Prints every possible decryption key from 1 to 26
#     along with the decrypted message.

#     """
#     for char in range(1, 26):
#         print(f"Key: {char}")
#         print(f"\t{translate_message(message, char)}")


def should_translate_again():
    """Asks the user if they want to encode or decode another text.

    Returns True if yes, False otherwise.

    """
    return ask_user_yes_no("\n\nWould you like to encrypt or "
                           "decrypt another message? (Y/N): ")


def start_program():
    """Starts the program.
    
    Restarts the program if the user wants to encode or
    decode another message.

    Prints out a message telling the user that the program has ended
    if they do not wish to continue with the program.
    
    """
    print(CAESAR_CIPHER_ASCII_ART)

    while True:
        user_text, key_rotation = get_message(), get_key()

        translate_message(user_text, key_rotation)

        if not should_translate_again:
            break

    print("\n\n-----Program Exited-----\n")


if __name__ == "__main__":
    start_program()


"""Encodes or decodes a message using Vignere Cipher method."""

from string import ascii_letters


def get_mode(text, key):
    """Ask the user whether they want to encrypt or decrypt their message.

    Return statement calls encode_message function or decode_message
    function depends on the mode that the user chose.

    and translate the message based on the chosen mode.

    """
    while True:
        mode = input("\n\nDo you wish to encrypt or "
                     "decrypt the message: ").lower()

        if mode in "encrypt e".split():
            return encode_message(text, key)

        if mode in "decrypt d".split():
            return decode_message(text, key)

        print("\n\nInvalid input. Only 'encrypt', 'e', 'decrypt', or 'd'.")


def get_message():
    """Ask the user to enter the message for encryption or decryption.

    This is repeated until the user enters at least a
    character into the input prompt.

    Returns a string containing the user's input.

    """
    while True:
        message = input("\n\nEnter your message: ")

        if (not message.isdigit()) and (message != ""):
            return message

        print("\n\nInput must not be null or contain any numeric value.")


def get_keyword():
    """Ask the user to enter a keyword that is used to shift the value of
    each letter in the alphabets and generate a key phrase
    that has the same length as the message.

    This is repeated until the user enters a valid key.

    Returns a string containing the user's input.

    """

    while True:
        letter_key = input("\n\nEnter a keyword: ")

        if (not letter_key.isdigit()) and (letter_key != ""):
            return letter_key

        print("\n\nKeyword must be a string.")


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
    choice_yes = ("yes", 'y')
    choice_no = ("no", 'n')

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in choice_yes:
            return True

        if user_choice in choice_no:
            return False

        print("\nInvalid Input. Try again.")


def encode_message(plaintext, key):
    """Wrapper function to encode message for vigenere_translate function."""
    return vigenere_translate(plaintext, key, "encrypt e".split())


def decode_message(ciphertext, key):
    """Wrapper function to decode message for vigenere_translate function."""
    return vigenere_translate(ciphertext, key, "decrypt d".split())


def check_text_case(symbol: str, result: list, key_position: int) -> list:
    """Check whether the letter in the message is an uppercase or
    a lowercase in order to get the translated message
    to match the casing of the original message.

    Appends the uppercase letter in ascii_letters[key_position] to result
    if the letter found in symbol is an uppercase letter.

    Appends the lowercase letter in ascii_letters[key_position] to result
    if the letter found in symbol is an lowercase letter.

    Appends the encrypted (or decrypted) character to result
    using key_position as the index to match the position
    of the letter in ascii_letters.

    """
    if symbol.isupper():
        result.append(ascii_letters[key_position].upper())
    elif symbol.islower():
        result.append(ascii_letters[key_position].lower())


def check_index_length(index, key):
    """Check if the index that is used to match the length of
    the given keyword is equal to the length of the keyword.

    Resets index to 0 if index is equal to the length
    of the keyword and returns an integer of 0.

    Returns index unchanged if index is not equal to the length of the keyword.

    """
    if index == len(key):
        index = 0
        return index
    return index


def print_translated_message(original_message, result, mode):
    """
    Prints the original message entered by the user.
    Prints a string containing the translated message.

    """
    print(f"\n\nOriginal Message: {original_message}")

    if mode == "encrypt e".split():
        print(f"\nEncrypted Message: {''.join(result)}")
    elif mode == "decrypt d".split():
        print(f"\nDecrypted Message: {''.join(result)}")


def vigenere_translate(message, key, mode):
    """Build the encrypted (or decrypted) string one character at
    a time and store  these characters in translated_message.

    The key_index variable keeps track of which subkey to use since a different
    key is used  depending on the position of the letter in the message.

    Sets key_index to 0 since the letter used to encrypt or decrypt the
    first letter of the message will be the one at key[0]
    where key variable is the keyword given by the user.

    The key_index (subkey) will always be what key[key_index] evaluates to;
    for instance: key_index is 1, keyword is "dog", key[key_index]
    or dog[1] evaluates to the letter 'o'.

    Sets the characters in message to the variable char
    on each iteration of the for loop.

    Finds the index of char in ascii_letters and
    assigns the result to char_position.

    The letter in char is found in ascii_letters
    if char_position is not set to -1.

    Checks if the mode chose by the user is encryption or decryption.
    += is used for encryption and -= is used for decryption.

    Mods the integer stored in char_position if the new value of char_position
    is less than 0 or if the new value of char_position is
    the length of ascii_letters or greater.

    Increments key_index by 1 after char has been translated in order
    to use the next subkey on the  next iteration of the for loop.

    This way, when the next iteration uses key[key_index] to get
    the subkey, it will be the index to the next subkey.

    Appends the character untranslated if char was not found in
    ascii_letters e.g. char is a number or puncutuation
    marks such as '10', '?', or ':'.

    After building the string from each character and appending it to
    translated_message, calls print_translated_message and join
    method on the blank string (the result of appending untranslated character)
    to join together all the strings in translated_message.

    """
    translated_message = []

    key_index = 0

    for char in message:
        char_position = ascii_letters.find(char)

        if char_position != -1:
            if mode == "encrypt e".split():
                char_position += ascii_letters.find(key[key_index])
            elif mode == "decrypt d".split():
                char_position -= ascii_letters.find(key[key_index])

            char_position %= len(ascii_letters)

            check_text_case(char, translated_message, char_position)

            key_index += 1

            key_index = check_index_length(key_index, key)

        else:
            translated_message.append(char)

    print_translated_message(message, translated_message, mode)


def should_translate_again():
    """Ask the user to enter a message and give a secret keyword in order to
    encrypt the message.

    Calls get_mode to check whether the user wants to encrypt or decrypt their
    messages and translates the message according to the chosen mode.

    Asks the user if they want to encrypt or decrypt more messages.

    Restarts the program if the user wants to perform
    further encryption or decryption.

    Exits the program if the user does not want to continue with the program.

    """
    while True:
        user_message, keyword = get_message(), get_keyword()

        get_mode(user_message, keyword)

        if not ask_user_yes_no("\n\nWould you like to encrypt or "
                               "decrypt another message? (Y/N): "):
            print("\n\nExiting program...\n\n")
            break


should_translate_again()

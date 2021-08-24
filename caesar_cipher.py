
from string import ascii_lowercase as ALPHABETS


def get_cipher_text(new_shift, character):
    """
    Returns new character given a new shift key.
    Returns the original symbol to the decrypted result if a letter in the message is not found in ALPHABETS
    """

    if character in ALPHABETS:
        return ALPHABETS[new_shift]
    return character


def decode_ciphered_text(message, offset):
    """
    Initializes an empty string as the decrypted result from building up each letter.
    Loops through every letter in the message.
    Finds the first occurence of the letter and shifts the character with the given POSITIVE offset.
    Reduces any number greater than 26 to a number from 0 to 25 using the modulo operator.
    Adds each decrypted letter into decrypted result using new_char_position as an index to the string ALPHABETS
    """
    
    decrypted_result = ""
    
    for char in message:
        new_char_position = (ALPHABETS.find(char) + offset) % len(ALPHABETS)
        decrypted_result += get_cipher_text(new_char_position, char)

    return decrypted_result


def encode_plain_text(message, offset):
    """
    Initializes an empty string as the decrypted result from building up each letter.
    Loops through every letter in the message.
    Finds the first occurence of the letter and shifts the character with the given NEGATIVE offset.
    Reduces any number greater than 26 to a number from 0 to 25 using the modulo operator.
    Adds each decrypted letter into decrypted result using new_char_position as an index to the string ALPHABETS
    """
    
    encrypted_message = ""
    
    for char in message:
        new_char_value = (ALPHABETS.find(char) - offset) % len(ALPHABETS)
        encrypted_message += get_cipher_text(new_char_value, char)

    return encrypted_message


print(decode_ciphered_text("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))

print(encode_plain_text("hey there! this is an example of a caesar cipher. were you able to decode it?", 10))

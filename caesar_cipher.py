
# This program currently can only check for lowercase strings.


def encrypt_message(plain_text):
    """
    Checks whether or not the string is an uppercase or lowercase from A to Z using the isalpha() string method.

    Adds 26 (there are a total of 26 letters in the English alphabet) to ord_num value if it has a 
    smaller value than the ordinal value for "a" and then concatenates the encrypted value to enrypted_message.

    Concatenates the original letter to decrypted_message if the letter was not a lowercase.

    Returns a string of the encrypted message in lowercase.
    """

    offset = -10

    enrypted_message = ""

    for char in plain_text:
        if char.isalpha():
            ord_num = ord(char) + offset

            if ord_num < ord('a'):
                ord_num += 26 

            enrypted_message += chr(ord_num)
        else:
            enrypted_message += char
    
    return enrypted_message


def decrypt_message(plain_text):
    """
    Checks whether or not the string is an uppercase or lowercase from A to Z using the isalpha() string method.

    Subtracts 26 (there are a total of 26 letters in the English alphabet) from ord_num value if it has a 
    larger value than the ordinal value for "z" and then concatenates the decrypted value to decrypted_message.

    Concatenates the original letter to decrypted_message if the letter was not a lowercase.

    Returns a string of the decrypted message in lowercase.
    """

    offset = 10

    decrypted_message = ""

    for char in plain_text:
        if char.isalpha():
            ord_num = ord(char) + offset

            if ord_num > ord('z'):
                ord_num -= 26 

            decrypted_message += chr(ord_num)
        else:
            decrypted_message += char
    
    return decrypted_message

print(encrypt_message("hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"))

print(decrypt_message("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"))
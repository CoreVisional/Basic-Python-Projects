
# This program currently can only check for lowercase strings.


from string import ascii_lowercase as alphabets


def decrypt_cipher_text(message, offset):
    
    decrypted_message = ""
    
    for char in message:
        if char in alphabets:
            new_char_position = (alphabets.find(char) + offset) % len(alphabets)
            decrypted_message += alphabets[new_char_position]
        else:
            decrypted_message += char
    return decrypted_message


def encrypt_plain_text(message, offset):
    
    encryted_message = ""
    
    for char in message:
        if char in alphabets:
            new_char_position = (alphabets.find(char) + offset) % len(alphabets)
            encryted_message += alphabets[new_char_position]
        else:
            encryted_message += char
    return encryted_message


print(decrypt_cipher_text("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
print(encrypt_plain_text("performing multiple caesar ciphers to code your messages is even more secure!", -14))
# caesar.py
""" Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.
"""
import string 
def caesar(key, plaintext):
    charmap = {letter: idx for (idx, letter) in enumerate(string.ascii_letters, 1)}
    chars = string.ascii_lowercase
    plaintext = plaintext.lower()
    ciphertext = ''
    for letter in plaintext:
        if letter in chars:
            print('found')
            letter_index = chars.find(letter)
            letter_index = (letter_index + key) % len(chars)
            print(letter_index)
            ciphertext += chars[letter_index] 
        else:
            ciphertext += letter
        print(ciphertext)



def map_caesar(key, plaintext):
    """
        This solution implements .translate() and .maketrans() from the str class.  
        This maps the characters through a translation table
    """
    letters = string.ascii_lowercase
    mask = letters[key:] + letters[:key]
    transtab = str.maketrans(letters, mask)
    return plaintext.translate(transtab)


def shift_n(letter, table):
    try:
        index = string.ascii_lowercase.index(letter)
        return table[index]
    except ValueError:
        return letter

def caesar_alt(message, amount):
    amount = amount % 26
    table = string.ascii_lowercase[amount:] + string.ascii_lowercase[:amount]
    enc_list = [shift_n(letter, table) for letter in message]
    return "".join(enc_list)
"""
Interview Question #2

"A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking whether
 a given string is palindrome or not! 
"""

def is_palindrome(word):
    rev_word = word[::-1]
    if rev_word == word:
        return True
    return False

def is_palindrome_alt(word):
    return word == ''.join(word[::-1])

if __name__ == "__main__":
    word = 'radar'
    print(is_palindrome(word))
    print(is_palindrome_alt(word))
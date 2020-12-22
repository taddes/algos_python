"""
Interview Question - Anagram

Construct an algorithm to check whether two words (or phrases) are anagrams or not!
An anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.
"""

def is_anagram(word_a, word_b):
    # Character Map/Hash Table
    letter_count_a = {}
    letter_count_b = {}
    for letter in word_a:
        letter_count_a[letter.lower()] = letter_count_a.get(letter.lower(), 0) + 1
    for letter in word_b:
        letter_count_b[letter.lower()] = letter_count_b.get(letter.lower(), 0) + 1
    print(letter_count_a, letter_count_b)
    print(letter_count_a == letter_count_b)
    return letter_count_a == letter_count_b

def is_anagram_2(word_a, word_b):
    if len(word_a) != len(word_b):
        print(False)
        return False
    # Sort alphabetically (has O (N log N) runtime, n being the number of characters)
    word_a = sorted(word_a)
    word_b = sorted(word_b)

    # Linear search O(n) but overall is O(n log n) - linearithmic due to above sorting
    # Therefore O (N log N) + O (N) == O (N log N)
    for i in range(0 ,len(word_a)):
        if word_a[i] != word_b[i]:
            print(False)
            return False
    print(True)
    return True


if __name__ == "__main__":
    
    is_anagram('restful', 'fluster')
    is_anagram_2('restful', 'fluster')
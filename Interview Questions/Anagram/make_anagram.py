"""
Given two strings in lowercase, the task is to make them into anagrams by removing
characters from either string.

Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c, and d from str1.
"""
from collections import Counter

def remove_chars(str1, str2):

    dict_1 = Counter(str1)
    dict_2 = Counter(str2)

    keys_1 = dict_1.keys()
    keys_2 = dict_2.keys()

    # Must add 1, as will return 0 indexed length
    count_1 = len(keys_1) + 1
    count_2 = len(keys_2) + 1
    print(str(count_1))
    print(str(count_2))

    # Convert list of keys into set to find common keys
    set_1 = set(keys_1)
    common_keys = len(set_1.intersection(keys_2))

    if common_keys == 0:
        print(str(count_1 + count_2))
        return count_1 + count_2
    else:
        print(str(max(count_1, count_2) - common_keys))
        return max(count_1, count_2) - common_keys

if __name__ == "__main__":
    remove_chars('abugida', 'abugidahar')
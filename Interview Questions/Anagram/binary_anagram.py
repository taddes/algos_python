"""
Python Dictionary | Check if binary representations of two numbers are anagrams.

Requires Counter class from collections module:
class collections.Counter([iterable-or-mapping])
returns a Dictionary-like collection containing keys and their counts
1. Convert strings into binary representation.
2. Append zeros to the start of any shorter binary digits to ensure equal length.
3. Convert both binary outputs to strings of 0s and 1s with the Counter() function
to determine the count of each.
"""
from collections import Counter 

def bin_anagram(val1, val2):
    # Recall Bin repr will contain 0b as prefix. Slice this away
    bin1 = bin(val1)[2:]
    bin2 = bin(val2)[2:]
    print((bin1))
    print((bin2))

    zeros = abs(len(bin1) - len(bin2))
    print(zeros)
    if len(bin1) > len(bin2):
        bin2 = zeros * '0' + bin2
    else:
        bin1 = zeros * '0' + bin1
    
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)

    if dict1 == dict2:
        print(True)
        return True
    else:
        print(False)
        return False

if __name__ == "__main__":
    bin_anagram(4, 7)
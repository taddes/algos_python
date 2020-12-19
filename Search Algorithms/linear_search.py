"""
Linear Search/Sequential Search 
===============================
A method for finding an item in an unsorted list.
Sequentially go through each item and compare if it is the one you are searching for.
Algorithm makes N comparisons in its worst case.
O(n) - linear runtime complexity - impractical, as O(log N) or O(1) can be achieved
using other algorithms 
"""


def linear_srch(collection, item):
    for index in range(len(collection)):
        if collection[index] == item:
            return index
    return -1



print(linear_srch([2, 44, 56, 34, 5734, 5, 66, 23], 23))

def recursive_linear_srch(collection, item, index=0):
    if index >= len(collection):
        return -1
    
    if collection[index] == item:
        return index
    
    return recursive_linear_srch(collection, item, index+1)

nums = [1, 4, 6, -4, 0, 100]
print(recursive_linear_srch(nums, 0))
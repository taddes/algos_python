"""
Binary Search - Logarithmic Search
==================================
Method for finding the position of an item in a sorted list.
long N comparisons in worst-case.
Discard half of the list with each pass, comparing value at midpoint to item you 
are searching for.
O (log N) runtime complexity (very favorable) - close to constant time 
"""

def bin_search(collection, item, left, right):
    if right < left:
        return -1
    
    # generate index of middle item (int division to round down)
    middle_index = (left + right) // 2
    if collection[middle_index] == item:
        return middle_index

    # Check if middle item is smaller or greater
    elif collection[middle_index] > item:
        print('Checking items on the left')
        return bin_search(collection, item, left, middle_index-1)

    elif collection[middle_index] < item:
        print('Checking items on the right')
        return bin_search(collection, item, middle_index+1, right)


print(bin_search([2,5,7,11], 11, 0, 3))
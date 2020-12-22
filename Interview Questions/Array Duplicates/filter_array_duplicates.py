"""
Interview Question - Array Duplicates

The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) 
running time where the integer values are smaller than the length of the array!

Approaches:
1. Brute force method of comparing each element to each other. Fine for a small
array, but has a O(N^2) runtime.
2. Hashmap: traverse the array and insert each item into the hastable with the value
as the key. Not an in-place algorithm however and requires additional memmory.
3. Absolute values: in-place, O(N) runtime
"""

def filter_duplicates(array):
    pass



array = [1, 7, 9, 8, 4, 7, 3, 4, 7]
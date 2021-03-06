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
    # Simplest of all, cast to a set and then back to a list
    print(list(set(array)))
    return list(set(array))

def filter_duplicates_2(array):
    # Brute Force method. 
    filtered = []
    for item in array:
        if item not in filtered:
            filtered.append(item)
    print(filtered)
    return filtered

def filter_duplicates_3(array):
    # List Comprehension method. 
    filtered = []
    [filtered.append(item) for item in array if item not in filtered]
    print(filtered)
    return filtered

def filter_duplicates_4(array):
    # List Comprehension with enumerate method. Looks for already occuring elements
    filtered = [i for n, i in enumerate(array) if i not in array[:n]]
    print(filtered)
    return filtered

def filter_duplicates_5(array):
    # Ordered Dict method
    from collections import OrderedDict
    filtered = list(OrderedDict.fromkeys(array))
    print(filtered)
    return filtered

def filter_duplicates_6(nums):
    # Absolute Value filtering
    filtered = []
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
            filtered.append(nums[abs(num)])
        else:
            print(f'Repetition found {abs(num)}')


if __name__ == "__main__":
    array = [1, 7, 9, 8, 4, 7, 5,  3, 4, 7, 4, 3, 9, 12, 5]
    filter_duplicates(array)
    filter_duplicates_2(array)
    filter_duplicates_3(array)
    filter_duplicates_4(array)
    filter_duplicates_5(array)
    filter_duplicates_6(array)
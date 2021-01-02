"""
Largest sum subarray problem

Create an algorithm to find the sum of contiguous subarray within a
one-dimensional array of numbers which has the largest sum.


1. If the array contains all negative numbers, the solution is the number in the 
array with the smallest magnitude.
2. If the array contains all positive numbers, the solution is the sum of all the items.
3. If the array contains negative and positive numbers, it is not immediately clear.

Consider Kadane's Algorithm to solve this problem O(N) - Dynamic Programming
Reuse sub-solutions from previous solutions.
B i+1 = max(nums[i+1], nums[i+1] + B i)

Requires tracking of a current max and a global max.

Current Max
==========
Tracks the actual subarr we are considering, ending with current i
current_max = max(nums[i], current_max+nums[i])

Global Max
==========
Largest subarray sum
global_max = current_max (if current_max > max_global)

Common Applications:
Computer Vision - brightest area in an image (deep learning).
Genomic Sequence Analysis - identify segments of proteins.
Data Mining - association rules and predicting behavior.
"""

def largest_subarr(nums):
    max_global = nums[0]
    max_current = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current+nums[i])

        if max_current > max_global:
            max_global = max_current

    return max_global

if __name__ == "__main__":
    nums = [1, -2, 3, 4, -5, 8]
    print(largest_subarr(nums))
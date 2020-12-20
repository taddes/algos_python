"""
Quickselect - Tony Hoare Algorithm
==================================
Selection Algorithm - able to find the k-th smallest or largest item in an unordered array
Has O(n) linear run time (best-case) | O(n^2) (worst-case) | Average O(n)
Pivot point affects the runtime complexity. If too small.
In-place approach - does not need additional memory or pre-sorting

k-th order statistics - min, max, average, etc.

Similar to Quicksort: Instead or recursing into both sides of the array, only one side is used when
dealing with quickselect. Partition followed by selection.
1) Choose a pivot at random (in the range [first_index, last_index]).
2) Partition the array based on the pivot value.
3) Intead of recursion into both sides, only one side (fewer recursive calls over quicksort).
"""
import random

class Quickselect:
    def __init__(self, nums):
        self.nums = nums
        self.first_index = 0
        self.last_index= len(nums) - 1

    def run(self, k):
        return self.select(self.first_index, self.last_index, k-1)

    # Partition Phase
    def partition(self, first_index, last_index):
        pivot_index = random.randint(first_index, last_index)
        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            # < or > here determines whether checking for min or max
            # < for less, > for max
            if self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1
            
            self.swap(first_index, last_index)
            # Index of the pivot
            return first_index

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
    # Selection phase
    def select(self, first_index, last_index, k):
        # Partition Phase
        pivot_index = self.partition(first_index, last_index)

        if pivot_index < k:
            # discard leftmost sub-array, keep items on right
            return self.select(pivot_index+1, last_index, k)
        elif pivot_index > k:
            # discard the right sub-array, keep items on left
            return self.select(first_index, pivot_index-1, k)
        # item found
        return self.nums[pivot_index]

x = [1, 2, -5, 100, -7, 3, 4 ]
select = Quickselect(x)

print(select.run(1))
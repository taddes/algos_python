import random

class QuickSelect:
    def __init__(self, nums):
        self.nums = []
        self.first_idx = 0
        self.last_idx = len(nums) - 1

    # Partition
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def partition(self, first_idx, last_idx):
        pivot_idx = random.randint(first_idx, last_idx)

        # swap
        self.swap(pivot_idx, last_idx)

        for i in range(first_idx, last_idx):
            if self.nums[i] < self.nums[last_idx]:
                self.swap(i, first_idx)
                self.first_idx += 1
                first_idx += 1
        self.swap(first_idx, last_idx)
        return first_idx





array = [5, -6, 89, 65, 2, 14 -6, 22]
myselect = QuickSelect(array)
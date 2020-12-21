"""
Reversing an array in-place overview
Interview Question #1

The problem is that we want to reverse a T[] array in O(N) linear time complexity
 and we want the algorithm to be in-place as well!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
"""
arr = [1,2,3,4,5]

rev_arr = arr[::-1]
print(rev_arr)

def reverse_array(nums):
    start_index = 0
    end_index = len(nums) - 1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1
    return nums

print(reverse_array(arr))
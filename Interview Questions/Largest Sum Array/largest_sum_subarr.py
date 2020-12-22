"""
Largest sum subarray problem

Create an algorithm to find the sum of contiguous subarray within a
 one-dimensional array of numbers which has the largest sum.


1. If the array contains all negative numbers, the solution is the number in the 
array with the smallest magnitude.
2. If the array contains all positive numbers, the solution is the sum of all the items.
3. If the array contains negative and positive numbers, it is not immediately clear.
Consider Kadane's Algorithm to solve this problem O(N)
"""
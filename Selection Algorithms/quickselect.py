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
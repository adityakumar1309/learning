"""
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.
Examples :

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
"""

def find_diff(arr):
    if not arr:
        return "Empty Array"

    if len(arr) == 1:
        return arr[0]

    right_max = arr[-1]
    max_diff = -1

    n = len(arr)
    for i in range(n - 2, -1, -1): 
        ele = arr[i]
        if ele > right_max:
            right_max = ele
        else:
            max_diff = max(max_diff, right_max-ele)

    return max_diff

li = [[2, 3, 10, 6, 4, 8, 1], [7, 9, 5, 6, 3, 2]]

for arr in li:
    print arr
    print find_diff(arr)

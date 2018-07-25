"""
Sliding Window Maximum (Maximum of all subarrays of size k)
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples :

Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90

"""

def find_max_in_subarray(arr, k):
    stack = []
    stack.append(0)

    for index, element in enumerate(arr):
        if index == 0:
            continue

        while stack and element >= arr[stack[0]]:
            stack.pop()

        stack.append(index)

        #if our stack grows than size then eliminate extra item
        if len(stack) > k:
            #if max element in stack is outside the sliding range then pop that too
            if stack[-1] < (index-k):
                stack.pop(k-1)
            else:
                poped_item = stack.pop()

        #skip printing till we have covered k elements and evaluated max from that k
        if index < k-1:
            continue

        print arr[stack[0]]

k = 3
for tup in [(3, [1, 2, 3, 1, 4, 5, 2, 3, 6]), (4, [8, 5, 10, 7, 9, 4, 15, 12, 90, 13])]:
    k, arr = tup
    print "In Array: %s, k: %s"%(arr, k)
    find_max_in_subarray(arr, k)

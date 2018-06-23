# Python program to find maximum amount of water that can
# be trapped within given set of bars.
 
def findWater(arr, n):
 
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = arr[0]
 
    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = arr[0]
 
    # Initialize result
    water = 0
 
    for i in range(1, n):
        if right < arr[i]:
            right = arr[i]
            right_index = i

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    left_index = 0
    for i in range(0, n):
        
        #re-calculate_left max height
        if left < arr[i]:
            left = arr[i]
            left_index = i

        if right < arr[i]:
            right = arr[i]
            right_index = i

        print "water = water + min(left,right) - arr[i]"
        print "water = %s + min(%s,%s) - %s"%(water, left, right, arr[i])
        water += min(left,right) - arr[i]
    
        if left_index > right_index:
            continue

    return water
 
 
# Driver program
 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#arr = [3, 0, 0, 2, 0, 4] 
n = len(arr)
print("Maximum water that can be accumulated is",findWater(arr, n))

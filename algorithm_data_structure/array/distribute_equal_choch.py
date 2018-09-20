# Python3 implementation to 
# find the maximum number
# of chocolates to be 
# distributed equally
# among k students
 
# function to find the
# maximum number of chocolates
# to be distributed equally
# among k students
def maxNumOfChocolates(arr, n, k):
     
    um, curr_rem, maxSum = {}, 0, 0
     
    # 'sm[]' to store cumulative sm,
    # where sm[i] = sm(arr[0]+..arr[i])
    sm = [0]*n
    sm[0] = arr[0]
     
    # building up 'sm[]'
    for i in range(1, n):
        sm[i] = sm[i - 1] + arr[i]
         
    # traversing 'sm[]'
    for i in range(n):
 
        # finding current remainder
        curr_rem = sm[i] % k
         
        if (not curr_rem and maxSum < sm[i]) : 
            maxSum = sm[i]
        elif (not curr_rem in um) :
            um[curr_rem] = i
        elif (maxSum < (sm[i] - sm[um[curr_rem]])):
              maxSum = sm[i] - sm[um[curr_rem]]
         
    return maxSum//k
     
# Driver program to test above
arr = [ 2, 7, 6, 1, 5, 4 ]
n, k = len(arr), 3
 
print("Maximum number of chocolates: " +
     str(maxNumOfChocolates(arr, n, k)))
 
# This code is contributed by Ansu Kumari


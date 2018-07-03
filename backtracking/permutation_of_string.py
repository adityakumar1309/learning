# Python program to print all permutations with
# duplicates allowed
 
def toString(List):
    return ''.join(List)

def swap(a, index_1, index_2):
    temp = a[index_1]
    a[index_1] = a[index_2]
    a[index_2] = temp

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            swap(a, l, i)
            permute(a, l+1, r)
            swap(a, l, i)

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

def no_of_ways(_sum, n, arr):
    if _sum < n:
        for i in xrange(1, n+1):
            arr.append(i)
            no_of_ways(_sum+i, n, arr)
            arr.remove(i)
    if _sum == n:
        print arr
        arr = []

n = 5
arr = []
no_of_ways(0, n, arr)



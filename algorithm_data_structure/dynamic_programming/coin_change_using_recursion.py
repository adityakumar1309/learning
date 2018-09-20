def no_of_ways(_sum, n, arr, denominations):
    if _sum < n:
        for i in denominations:
            arr.append(i)
            no_of_ways(_sum+i, n, arr, denominations)
            arr.remove(i)
    if _sum == n:
        print arr
        arr = []

n = 10
denominations = [2,3,4]
arr = []
no_of_ways(0, n, arr, denominations)



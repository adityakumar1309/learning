#logic : 
#if you have taken 1 steps then if hop = 1 , ways(n-1)
#if you have taken 2 steps then if hop = 2 , ways(n-2)
#now any soln will either start with combinations of hops with 1 step or 2 step ie starting hop sequence will start with either 1 or either 2
#so total ways(n) = ways(n-1) + ways(n-2)

#DP SOLN : you dont need to calculate ways(n-2) twice
def get_no_of_ways(n, valid_hop):
    ways = [0]*(n+1)
    ways[1] = 1
    ways[2] =  2
    #ways(n) = ways(n-1) + ways(n-2)
    for i in xrange(3, n+1):
        ways[i] = ways[i-1] + ways[i-2]
    return ways[n]

n = 5
valid_hop = [1,2]
print "No of Ways Possible to get to : %s --> %s"%(n, get_no_of_ways(n, valid_hop))

#logic : 
#if you have taken 1 steps then if hop = 1 , ways(n-1)
#if you have taken 2 steps then if hop = 2 , ways(n-2)
#now any soln will either start with combinations of hops with 1 step or 2 step ie starting hop sequence will start with either 1 or either 2
#so total ways(n) = ways(n-1) + ways(n-2)

#DP SOLN : you dont need to calculate ways(n-2) twice

"""
Generalization of the above problem
How to count number of ways if the person can climb up to m stairs for a given value m? For example if m is 4, the person can climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.

We can write the recurrence as following.

   ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... ways(n-m, m) 
"""

def get_no_of_ways(n, valid_hop):
    ways = [0]*(n+1)
    ways[1] = 1
    ways[2] =  2
    #ways(n) = ways(n-1) + ways(n-2)
    for i in xrange(3, n+1):
        for hop in valid_hop:
            if hop > i:
                break
        
            ways[i] = ways[i] + ways[i-hop]
    return ways[n]

n = 4
valid_hop = [1,3]
print "No of Ways Possible to get to : %s --> %s"%(n, get_no_of_ways(n, valid_hop))

# Python program to find 3 elements such
# that max(abs(A[i]-B[j]), abs(B[j]- C[k]),
# abs(C[k]-A[i])) is minimized.
import sys
def findCloset(A, B, C, p, q, r):
    diff = sys.maxsize

    res_i = 0
    res_j = 0
    res_k = 0
    # Travesre Array
    i = 0
    j = 0
    k = 0
    while(i < p and j < q and k < r):
        curr_diff = max(abs(A[i]-B[j]), abs(B[j]- C[k]), abs(C[k]-A[i]))

        if curr_diff < diff:
            res_i = i
            res_j = j
            res_k = k
            diff = curr_diff

        if diff == 0:
            break

        #try to get closer to diff , by moving to next element from the array which yeilded min
        minimum = min(A[i], B[j], C[k])
        if A[i] == minimum:
            i = i+1
        elif B[j] == minimum:
            j = j+1
        else:
            k = k+1
    print(A[res_i], " ", B[res_j], " ", C[res_k])

# Driver Program
A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]

p = len(A)
q = len(B)
r = len(C)

print "A: %s\nB: %s\nC: %s"%(A, B, C)
findCloset(A,B,C,p,q,r)

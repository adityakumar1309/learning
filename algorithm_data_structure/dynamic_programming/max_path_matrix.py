def maximum_path(mat):
    for i in range(1, N):
        res = -1
        for j in range(M):

            # When all paths are possible
            if (j > 0 and j < M - 1):
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j - 1], mat[i - 1][j + 1])

            # When diagonal right is not possible
            elif (j > 0):
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j - 1])

            # When diagonal left is not possible
            elif (j < M - 1):
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j + 1])

            # Store max path sum
            res = max(mat[i][j], res)
    return res

mat1 = [[4, 2, 3, 4],
       [2, 9, 1, 10],
       [15, 1, 3, 0],
       [16, 92, 41, 44]]
mat2 = ([[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ],
        [ 0, 10, 4, 0, 2, 0 ],
        [ 1, 0, 2, 20, 0, 4 ]])

for mat in [(mat1, 4, 4), (mat2, 4, 6)]:
    mat, N, M = mat
    print(maximum_path(mat))

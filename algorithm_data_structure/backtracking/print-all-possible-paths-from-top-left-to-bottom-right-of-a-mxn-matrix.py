"""
Print all possible paths from top left to bottom right of a mXn matrix
The problem is to print all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.

Examples :

Input : 1 2 3
        4 5 6
Output : 1 4 5 6
         1 2 5 6
         1 2 3 6

Input : 1 2 
        3 4
Output : 1 2 4
         1 3 4

"""
MAX_ROW = 2
MAX_COL = 3

def print_all_path(matrix, path, row, col):
    if row == MAX_ROW-1 and col == MAX_COL-1:
        print path
        return

    if row ==  MAX_ROW-1:
        for i in xrange(col, MAX_COL):
            path = path + "-" + str(matrix[row][i])

        print path
        return

    if col == MAX_COL-1:
        for i in xrange(row, MAX_ROW):
            path = path + "-" + str(matrix[i][col])
        print path
        return

    path = path + "-" + str(matrix[row][col])

    if row < MAX_ROW-1:
        print_all_path(matrix, path, row+1, col)
    if col < MAX_COL-1:
        print_all_path(matrix, path, row, col+1)

matrix = [[1, 2, 3], [4, 5, 6]] #2X3 matrix
path = ""
print_all_path(matrix, path, 0, 0)

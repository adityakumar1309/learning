"""
Minimum time required to rot all oranges
Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0: Empty cell

1: Cells have fresh oranges

2: Cells have rotten oranges 
So we have to determine what is the minimum time required so that all the oranges become rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.

Examples:

Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges can become rotten in 2 time frames.


Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {0, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges cannot be rotten.
"""

from collections import deque

def min_time_frame(arr):
    que = deque()
    no_of_one = 0

    for row_no in xrange(MAX_ROW):
        for col_no in xrange(MAX_COL):
            if arr[row_no][col_no] == 2:
                que.append((row_no, col_no))
            if arr[row_no][col_no] == 1:
                no_of_one = no_of_one + 1

    que.append(('#', '#'))
    time_frame = 0

    while que:
        position = que.popleft()
        if position[0] == '#':
            if not que:
                break

            que.append(position)
            time_frame = time_frame + 1
            continue

        row, col = position
        row_comb = [-1, -1, -1,  0, 0,  1, 1, 1]
        col_comb = [-1,  0,  1, -1, 1, -1, 0, 1]

        for k in range(8):
            x_index, y_index = row_comb[k], col_comb[k]
            if row+x_index < MAX_ROW and row+x_index >= 0 and col+y_index < MAX_COL and col+y_index >= 0 and arr[row+x_index][col+y_index] == 1:
                arr[row+x_index][col+y_index] = 2
                que.append((row+x_index, col+y_index))
                no_of_one = no_of_one - 1

    if no_of_one == 0:
        return time_frame
    return -1

MAX_ROW = 3
MAX_COL = 5
arr = [ [2, 1, 0, 2, 1],
        [1, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]]
print min_time_frame(arr)

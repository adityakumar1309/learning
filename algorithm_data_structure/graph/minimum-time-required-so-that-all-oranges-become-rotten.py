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

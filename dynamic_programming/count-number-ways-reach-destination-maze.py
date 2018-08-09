def count_no_ways(maze, nrow, ncol):
    #fill row 0 and col 0 with 1 as there is only way to reach that row or col
    for i in xrange(0, nrow):
        if maze[i][0] == 0:
            maze[i][0] = 1
        else:
            break

    #col has to start with col 1 otherwise our if else will break at first col istelf
    for i in xrange(1, ncol):
        if maze[0][i] == 0:
            maze[0][i] = 1
        else: 
            break

    for row_num in xrange(0, nrow):
        for col_num in xrange(0, ncol):
            if maze[row_num][col_num] == -1:
                continue

            #total ways at (i,j) is total ways total(i-1,j) + total(i,j-1)
            maze[row_num][col_num] = maze[row_num][col_num] + maze[row_num-1][col_num] if maze[row_num-1][col_num] > 0 else maze[row_num][col_num]
            maze[row_num][col_num] = maze[row_num][col_num] + maze[row_num][col_num-1] if maze[row_num][col_num-1] > 0 else maze[row_num][col_num]

    return maze[row_num-1][col_num-1]

nrow = 4
ncol = 4
maze = [[0,0,0,0],
        [0,-1,0,0],
        [-1,0,0,0],
        [0,0,0,0]]

print "No of ways in a maze: %s"%count_no_ways(maze, nrow, ncol)

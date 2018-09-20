from collections import deque

class Vertex:
    def __init__(self):
	self.cell_num = 0
	self.moves = 0

def min_moves(board, size):
    visited = {}
    queue = deque()
    vertex = Vertex()
    vertex.cell_num = 0
    vertex.moves = 0

    queue.append(vertex)

    visited[0] = True

    while queue:
        vertex = queue.popleft()
        cur_cell = vertex.cell_num
        moves = vertex.moves

        if cur_cell == size-1:
            break

        for dice_value in xrange(1, 7):
            next_possible_cell = cur_cell + dice_value

            if next_possible_cell >= size:
                break

            if visited.get(next_possible_cell):
                continue

            visited[next_possible_cell] = True
            current_vertex = Vertex()
            current_vertex.cell_num = board[next_possible_cell]
            current_vertex.moves = moves + 1
            queue.append(current_vertex)

    return vertex.moves

size = 36
board = [index for index in xrange(0, size)]

#ladder
board[2] = 15;
board[14] = 24;
board[20] = 31;

#Snakes
board[11] = 1;
board[29] = 3;
board[34] = 21;

print "Minimum Dice throws needed to reach to end: %s"%min_moves(board, size)

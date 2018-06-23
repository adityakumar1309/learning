# O(n) solution to find LCS of two given values n1 and n2
 
# A binary tree node
# Python program to find the diameter of binary tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def get_depth(node, depth, incr, opr, depth_hash):
    if node is None:
        return depth + incr

    if depth in depth_hash:
        depth_hash[depth].append(node.data)
    else:
        depth_hash[depth] = [node.data]
    return opr(get_depth(node.left, depth-1, incr, opr, depth_hash), get_depth(node.right, depth+1, incr, opr, depth_hash))

def print_vertical_level(root, cur_depth, level):
    if root is None:
        return

    if cur_depth == level:
        print root.data
    print_vertical_level(root.left, cur_depth-1, level)
    print_vertical_level(root.right, cur_depth+1, level)

# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

#we need to add 1 to left depth and -1 to right depth since when we call depth-1 for left in case of None we have added 1 extra
depth_hash = {0: [root.data]}
mind = get_depth(root, 0, 1, min, depth_hash)
maxd = get_depth(root, 0, -1, max, depth_hash)
print mind, maxd
print depth_hash

#O(n2) approach
for i in xrange(mind, maxd+1):
    print_vertical_level(root, 0, i)

#O(n) approach
for i in xrange(mind, maxd+1):
    data_list = depth_hash[i]
    print list(set(data_list))

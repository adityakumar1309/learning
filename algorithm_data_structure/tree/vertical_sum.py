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

def print_vertical_level(root, cur_depth, level_hash):
    if root is None:
        return

    if cur_depth in level_hash:
        level_hash[cur_depth] = level_hash[cur_depth] + root.data
    else:
        level_hash[cur_depth] = root.data

    print_vertical_level(root.left, cur_depth-1, level_hash)
    print_vertical_level(root.right, cur_depth+1, level_hash)

# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

level_hash = {}
print_vertical_level(root, 0, level_hash)

_min = min(level_hash.keys())
_max = max(level_hash.keys())

for level in xrange(_min, _max+1):
    print "%s "%level_hash[level],

#root.right.left.right = Node(8)
#root.right.right.right = Node(9)


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
 
 
"""
The function Compute the "height" of a tree. Height is the 
number f nodes along the longest path from the root node 
down to the farthest leaf node.
"""
def height(node):
     
    # Base Case : Tree is empty
    if node is None:
        return 0 ;
     
    # If tree is not empty then height = 1 + max of left 
    # height and right heights 
    return 1 + max(height(node.left) ,height(node.right))
 
# Function to get the diamtere of a binary tree
def diameter(root):
     
    # Base Case when tree is empty 
    if root is None:
        return root, 0;
 
    # Get the height of left and right sub-trees
    lheight = height(root.left)
    rheight = height(root.right)
 
    # Get the diameter of left and irgh sub-trees
    lnode, ldiameter = diameter(root.left)
    rnode, rdiameter = diameter(root.right)
 
    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1 
    #return max(lheight + rheight + 1, max(ldiameter, rdiameter))
    local_ht = lheight + rheight + 1
    if local_ht > max(ldiameter, rdiameter):
        return root, local_ht
    elif ldiameter > rdiameter:
        return lnode, ldiameter
    else:
        return rnode, rdiameter

def print_path(diam_node):
    if diam_node is None:
        return

    print_path(diam_node.left)
    print diam_node.data
    print_path(diam_node.right)

# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.left.right.left = Node(6);
root.left.right.right = Node(7);
root.left.left.right = Node(8);
root.left.left.right.left = Node(9);

diam_node, diam = diameter(root)
print diam
print "Diameter Node: %s"%(diam_node.data)

print_path(diam_node)



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def height(node):
    if node is None:
        return 0 ;
     
    return 1 + max(height(node.left) ,height(node.right))
 
def diameter(root):
    if root is None:
        return root, 0;
 
    lheight = height(root.left)
    rheight = height(root.right)
 
    lnode, ldiameter = diameter(root.left)
    rnode, rdiameter = diameter(root.right)
 
    #return root, max(lheight + rheight + 1, max(ldiameter, rdiameter))
    local_ht = lheight + rheight + 1
    if local_ht > max(ldiameter, rdiameter):
        return root, local_ht
    elif ldiameter > rdiameter:
        return lnode, ldiameter
    else:
        return rnode, rdiameter

def print_path(node, diam_node, left_node, right_node, path):
    if node is None:
        return False

    path.append(node.data)
    if ((node.data == left_node.data) or print_path(node.left, diam_node, left_node, right_node, path) or (node.data == right_node.data) or print_path(node.right, diam_node, left_node, right_node, path)):
        path.append(node.data)
    else:
        path.pop()

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
print "Diameter: %s, LCA Node: %s"%(diam, diam_node.data)

path = []

left_node = root.left.left.right.left
right_node = root.left.right.left

print_path(diam_node, diam_node, left_node, right_node, path)

print path

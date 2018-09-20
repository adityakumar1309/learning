#Be careful to check for border cases, like what if there is no right subtree or left subtree

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

def get_min_depth(node):
    if node is None:
        return 0

    #if node.left is None and node.right is None:
    #    return 1

    if node.left is None:
        return get_min_depth(node.right)+1
     
    # If right subtree is Null , recur for left subtree
    if node.right is None:
        return get_min_depth(node.left) +1

    return 1 + min(get_min_depth(node.left), get_min_depth(node.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print get_min_depth(root)

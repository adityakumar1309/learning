class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def print_path(root, path):
    path.append(root.data)

    if root.left is None and root.right is None:
        print path
        return

    if root.left:
        print_path(root.left, path)
        path.pop()
    if root.right:
        print_path(root.right, path)
        path.pop()

# create root
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)


''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   4       5 None 6'''

root.left.left  = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

path = []
print print_path(root, path)

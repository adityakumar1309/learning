# Python program for binary traversal of binary tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
    if root is None:
        return

    printLeaves(root.left)
    
    if root.left is None and root.right is None:
        print root.data
    
    printLeaves(root.right)

def printBoundaryLeft(root):
    if root is None:
        return

    if root.left:
        print root.data
        printBoundaryLeft(root.left) 
    
    elif root.right:
        print root.data
        printBoundaryRight(root.right)

def printBoundaryRight(root):
    if root is None:
        return

    if root.right:
        printBoundaryLeft(root.right)
        print root.data
    elif root.left:
        printBoundaryRight(root.left)
        print root.data
 
 
# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    if root is None:
        return

    print root.data
    printBoundaryLeft(root.left)
    printLeaves(root.left)
    printLeaves(root.right)
    printBoundaryRight(root.right)
    pass
 
 
# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left =  Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)

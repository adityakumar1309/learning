
"""
Question: Given a binary tree, find out if the tree can be folded or not.

A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. An empty tree is considered as foldable.

Consider the below trees:
(a) and (b) can be folded.
(c) and (d) cannot be folded.

(a)
       10
     /    \
    7      15
     \    /
      9  11

(b)
        10
       /  \
      7    15
     /      \
    9       11

(c)
        10
       /  \
      7   15
     /    /
    5   11

(d)

         10
       /   \
      7     15
    /  \    /
   9   10  12

"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def check_foldable(ltree, rtree):
    if ltree is None and rtree is None:
        return True

    if (ltree and not rtree) or (not ltree and rtree):
        return False

    return check_foldable(ltree.left, rtree.right) and check_foldable(ltree.right, rtree.left)


root = Node(10)
root.left = Node(8)
root.left.right = Node(5)
root.left.left = Node(3)

root.right = Node(2)
root.right.left = Node(2)
root.right.left = Node(22)
print "Foldable: %s"%(check_foldable(root.left, root.right))

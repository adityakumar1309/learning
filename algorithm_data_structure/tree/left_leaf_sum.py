class Node:
 
    # A constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def leftLeavesSumRec(root, isLeft, _sum):
    if root is None:
        return 0
     
    # Check whether this node is a leaf node and is left
    if root.left is None and root.right is None and isLeft == True:
        _sum += root.key
        return _sum     

    # Pass 1 for left and 0 for right
    return leftLeavesSumRec(root.left, 1, _sum) + leftLeavesSumRec(root.right, 0, _sum)
 
# Let us construct the Binary Tree shown in the
# above figure
root = Node(20);
root.left= Node(9);
root.right   = Node(49);
root.right.left = Node(23);
root.right.right= Node(52);
root.right.right.left  = Node(50);
root.left.left  = Node(5);
root.left.right = Node(12);
root.left.right.right  = Node(12);
 
print "Sum of left leaves is", leftLeavesSumRec(root, 0, 0) 

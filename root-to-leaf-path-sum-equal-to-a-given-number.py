class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def has_sum(node, csum, dsum):
    if node is None:
        if csum == dsum:
            return True
        else:
            return False

    csum = csum + node.data
    return has_sum(node.left, csum, dsum) or has_sum(node.right, csum, dsum)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)

for s in [21, 22, 23, 14, 10]:
    result_bool = has_sum(root, 0, s)
    if result_bool:
        print "There is a root-to-leaf path with sum %d" %(s)
    else:
        print "There is no root-to-leaf path with sum %d" %(s)

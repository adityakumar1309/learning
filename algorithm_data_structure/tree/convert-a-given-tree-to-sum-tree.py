#it is top down approach hence it is O(n2), if we go by bottom up approach then we may not need to calculate few things again and end up in 
#O(n)
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def print_tree(root):
    if root is None:
        return

    print_tree(root.left)
    print root.data
    print_tree(root.right)

def change_sum_tree(node):
    if node is None:
        return 0

    ltree_sum = change_sum_tree(node.left)
    rtree_sum = change_sum_tree(node.right)

    prev_node_data = node.data
    node.data = ltree_sum + rtree_sum
    return ltree_sum + rtree_sum + prev_node_data

root =  Node(10)
root.left =  Node(-2)
root.right =  Node(6)
root.left.left =  Node(8)
root.left.right =  Node(-4)
root.right.left =  Node(7)
root.right.right =  Node(5)

change_sum_tree(root)
print_tree(root)

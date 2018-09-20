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

def get_tree_sum(node, csum):
    if node is None:
        return csum 

    #this will also work
    lsum = get_tree_sum(node.left, csum)
    rsum = get_tree_sum(node.right, csum)
    return node.data + lsum + rsum

def change_sum_tree(node, csum):
    if node is None:
        return csum

    ltree_sum = get_tree_sum(node.left, 0)
    rtree_sum = get_tree_sum(node.right, 0)

    node.data = ltree_sum + rtree_sum
    change_sum_tree(node.left, 0)
    change_sum_tree(node.right, 0)

root =  Node(10)
root.left =  Node(-2)
root.right =  Node(6)
root.left.left =  Node(8)
root.left.right =  Node(-4)
root.right.left =  Node(7)
root.right.right =  Node(5)

change_sum_tree(root, 0)
print_tree(root)

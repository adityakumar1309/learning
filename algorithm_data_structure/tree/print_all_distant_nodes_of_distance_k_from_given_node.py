# A binary tree node
class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
def print_from_node_till_k(node, k):
    if node is None:
        return 

    if k == 0:
        print node.key

    print_from_node_till_k(node.left, k-1)
    print_from_node_till_k(node.right, k-1)

def from_root_till_node(root, node, k):
    if root is None:
        return -1

    if root.key == node.key:
        return k
    
    dist = from_root_till_node(root.left, node, k+1)
    if dist > -1:
        return dist

    dist = from_root_till_node(root.right, node, k+1)
    if dist > -1:
        return dist

def print_k_till_node(root, node, k):
    y = from_root_till_node(root, node, 0)
    if y >= k:
        #it means node is in same branch
        #above N till k we need to go 
        new_k = y - k - 1
        print_from_node_till_k(root.right, new_k)
    else:
        new_k = k - y - 1
        print_from_node_till_k(root.left, new_k)

def print_all_nodes_at_distance_k(root, node, k):
    if root is None:
        return

    print_from_node_till_k(node, k)
    print_k_till_node(root, node, k)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(10)
root.left.right.right = Node(11)
root.right.right.right = Node(8)
root.right.right.right.left = Node(111)
root.right.right.right.right = Node(9)

for k in [1,2,3]:
    R = root
    N = root.right
    print "Root->%s, Node->%s, k->%s"%(R.key, N.key, k)
    print_all_nodes_at_distance_k(R, N, k)

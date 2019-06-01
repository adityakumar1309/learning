class Node:       
    # Constructor to create a new Binary Tree 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def find_parent(root, node, res):
    if node is None:
        return None 

    if root is None:
        return None

    if (root.left and root.left.data == node.data) or (root.right and root.right.data == node.data):
        res[0] = root
        return root
        #import pdb;pdb.set_trace()
    
    else:
        l = find_parent(root.left, node, res)
        r = find_parent(root.right, node, res)
    return l or r 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.right = Node(15) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
  
node1 = root.left.right 
node2 = root.right.right  

node3 =  Node(12)

for node in [node1, node2, node3]:
    res = [None]
    found = find_parent(root, node, res)
    if res and res[0] is not None:
        print "for node1: %s, parent: %s, found::::: %s "%(node.data, res[0].data, found.data)
    else:
        print "for node1: %s no parent found"%(node.data)

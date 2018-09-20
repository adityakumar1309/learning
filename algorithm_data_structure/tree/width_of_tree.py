from collections import deque

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

def get_depth(root, node, depth):
    if root is None:
        return -1

    if node.key == root.key:
        return depth

    ld = get_depth(root.left, node, depth+1)
    if ld > -1:
        return ld
        
    rd = get_depth(root.right, node, depth+1)
    if rd > -1:
        return rd

def get_width(root):
    if root is None:
        return queue

    queue = deque()
    height_hash = {}
    queue.append(root)
    while(queue):
        node = queue.popleft()
        print "Calculating depth for :%s"%(node.key)
        level =  get_depth(root, node, 0)
        print "For: %s, level is : %s"%(node.key, level)
        if level in height_hash:
            height_hash[level].append(node.key)
        else:
            height_hash[level] = [node.key]
        #or if you are using normal list then do pop of queue.pop(0) //no need of explicitly poping left using deque
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        

    max_width = 0
    max_level = 0
    for level, value_list in height_hash.items():
        if len(value_list) > max_width:
            max_width = len(value_list)
            max_level = level

    print "Max width: %s, Max Level: %s"%(max_width, max_level)
    print "Elements of max width are: %s"%(height_hash[max_level]) 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7) 

get_width(root)
#print get_height(root)

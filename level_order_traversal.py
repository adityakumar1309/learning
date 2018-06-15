from collections import deque

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
def level_order_traversal(root):
    if root is None:
        return queue

    queue = deque()
    queue.append(root)
    while(queue):
        node = queue.popleft()
        #or if you are using normal list then do pop of queue.pop(0) //no need of explicitly poping left using deque
        print node.key
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7) 

level_order_traversal(root)

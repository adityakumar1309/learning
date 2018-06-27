from collections import deque

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
def level_order_traversal(root):
    depth = 0
    if root is None:
        return queue

    queue = deque()
    queue.append((root, depth+1))
    while(queue):
        node, depth = queue.popleft()
        #or if you are using normal list then do pop of queue.pop(0) //no need of explicitly poping left using deque
        if node.left is None and node.right is None:
            return depth
        if node.left:
            queue.append((node.left, depth+1))
        if node.right:
            queue.append((node.right, depth+1))
      
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print level_order_traversal(root)

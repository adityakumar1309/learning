from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonal_view(root):
    que = deque()
    if not root:
        return 

    node = root
    node1 = root
    que.append(root)

    while que:
        node = que.popleft()
        while node:
            print node.data
            if node.left:
                que.append(node.left)
            node = node.right
    
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonal_view(root)

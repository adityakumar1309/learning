from collections import deque

class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def leftView(root):
    if not root:
        return

    que = deque()
    que.append('#')
    que.append(root)
    
    while que:
        #print que
        ele = que.popleft()
        
        if ele == '#':
            que.append('#')
            ele = que.popleft()
            if ele !='#':
                print ele.data
        
        if ele !='#':
            if ele.left:
                que.append(ele.left)
            if ele.right:
                que.append(ele.right)

root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 
  
leftView(root) 

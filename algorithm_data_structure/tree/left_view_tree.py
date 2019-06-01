from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
def left_view(root):
    if not root:
        return

    que = deque()
    que.append(root)
    que.append('#')
    print root.data

    import pdb;pdb.set_trace()
    while que:
        poped_ele = que.popleft()
        if poped_ele == '#':
            if not que:
                return
            que.append('#')
            poped_ele = que.popleft()
            print poped_ele.data
        else:
            if poped_ele.left:
                que.append(poped_ele.left)
            if poped_ele.right:
                que.append(poped_ele.right)


root = Node(4) 
root.left = Node(5) 
root.right = Node(2) 
root.right.left = Node(3) 
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
#root.right.right.left = Node(8)
#root.right.right.right = Node(9)

left_view(root)

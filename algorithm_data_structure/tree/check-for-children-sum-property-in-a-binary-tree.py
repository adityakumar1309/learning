class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def isSumProperty(root):
    if not root:
        return 0

    root_data = root.data

    left = isSumProperty(root.left)
    right = isSumProperty(root.right)

    if root_data == (left+right) and isSumProperty(root.left) and isSumProperty(root.right):
        return True
    else:
        return False

root = newNode(10)  
root.left = newNode(8)  
root.right = newNode(2)  
root.left.left = newNode(3)  
root.left.right = newNode(5)  
root.right.right = newNode(2)  

if(isSumProperty(root)):  
    print("The given tree satisfies the",  
                "children sum property ")  
else: 
    print("The given tree does not satisfy", 
                   "the children sum property ")

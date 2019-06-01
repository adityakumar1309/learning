class Node: 
    # Constructor to initialize 
    # the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None


def print_list(node):
    while node:
        print node.data
        node = node.next

def 

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next = Node(5)

#node.next.next.next.next = node.next.next

print_list(node)

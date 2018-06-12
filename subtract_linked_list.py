class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None
 
root_1 = Node(1)
root_1.Next = Node(9);

root_2 = Node(4);
root_2.Next = Node(5);
root_2.Next.Next = Node(6);

print "456-019"

def padd_zero(node, diff):
    for i in xrange(0, diff):
        new_node = Node(0)
        new_node.Next = node
        node = new_node

    return node

def print_list(node):
    while node is not None:
        print node.data
        node = node.Next

def cal_len(node):
    _len = 0
    while node is not None:
        _len = _len + 1
        node = node.Next
    return _len

def sustract(root_1, root_2, new_node, borrow=False):
    #check which no is bigger 
    #if root_1 is not None and root_2 is not None:
    #    root_1.data > root_2.data
    #root_2 - root_1 we are doing
    if root_1 is not None:
        sustract(root_1.Next, root_2.Next, new_node, False)
        if borrow:
            root_2.data = root_2.data - 1
        if root_1.data > root_2.data:
            num = root_2.data+10-root_1.data
            borrow = True
        else:
            borrow = False
            num = root_2.data-root_1.data
        node = Node(num)
        node.Next = new_node
        new_node = node

    print "Diff list"
    print_list(new_node)
        

def reverse(node):
    if node.Next.Next is not None:
        reverse(node.Next)
    node = node.Next.Next
    return node

#416-39
def normalize(root_1, root_2):
    num_1_len = cal_len(root_1)
    num_2_len = cal_len(root_2)

    diff = abs(num_2_len-num_1_len)
    if num_1_len < num_2_len:
        #padd 0 in the beg of root_1
        root_1 = padd_zero(root_1, diff)
    elif num_1_len > num_2_len:
        root_2 = padd_zero(root_2, diff)
        #padd 0 in the beg of root_2

    #print_list(root_1)
    #print_list(root_2)

    return root_1, root_2

 
root_2 = reverse(root_2)
print_list(root_2)
root_1, root_2 = normalize(root_1, root_2)
#sustract(root_1, root_2, None)



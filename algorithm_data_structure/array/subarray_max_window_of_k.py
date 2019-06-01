#arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
#k = 3 
#Output :
#3 3 4 5 5 5 6

from collections import deque

def find_max_subbaray(li, k):
    dque = deque()

    for index, ele in enumerate(li):
        if index > k:
            break

        while dque and dque[-1] < ele:
            poped_ele = dque.popleft()

        dque.append(index)

    print li[dque[0]]
    _len = len(dque)

    for index, ele in enumerate(li):
        if index < k:
            continue

        if not dque:
            dque.append(index)
            _len = _len + 1
            print ele
            continue

        while dque and dque[-1] < ele:
            poped_ele = dque.popleft()
       
        print dque
        dque.append(index)
        print li[dque[0]]

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
find_max_subbaray(arr, k)

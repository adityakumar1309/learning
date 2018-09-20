def get_left_child_index(i): 
    return 2 * i + 1 

def  get_right_child_index(i):
    return 2 * i + 2 

def heap_sort(data):
    size = len(data)
  
    i = size / 2 - 1
    while i >=0:
        heapify(i, data, size)
        i = i - 1

    i = size - 1
    while i >=0:
        data[0], data[i] = data[i], data[0]
        size  = size-1
        heapify(0, data, size)
        i = i - 1

def heapify(i, data, size):
    largest_element_index = i

    left_child_index = get_left_child_index(i)
    if left_child_index < size and data[left_child_index] > data[largest_element_index]:
        largest_element_index = left_child_index

    right_child_index = get_right_child_index(i)
    if right_child_index < size and data[right_child_index] > data[largest_element_index]:
        largest_element_index = right_child_index

    if largest_element_index != i:
        data[i], data[largest_element_index] = data[largest_element_index], data[i]
        #Recursively heapify the affected sub-tree
        heapify(largest_element_index, data, size)

arr = [1,10,2,11,1,3,4,2]
heap_sort(arr)
print arr

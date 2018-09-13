hash_map = {}
stack = []

#insert 10
#insert 20
#insert 30
#insert 40

#search 30
#search 50
#get random
#delete 30
#get random

op_list = [('i', 10), ('i', 20), ('i', 30), ('i', 40), ('s', 30), ('s', 50), ('r', ''), ('d', 30), ('r', '')]

last_index = -1

for op in op_list:
    operation, val = op
    if operation == 'i':
        if val in hash_map:
            continue
        last_index = last_index + 1
        hash_map[val] = last_index
        stack.append(val)
        print "value: %s added at index: %s"%(val, last_index)

    elif operation == 's':
        print "Search: %s, status: %s"%(val, hash_map.get(val, 'not found'))

    elif operation == 'r':
        from random import randint
        rand_index = randint(0, last_index)
        print "Random: %s, Val: %s"%(rand_index, stack[rand_index])

    elif operation == 'd':
        #get index of element
        if val not in hash_map:
            continue
        index = hash_map[val]
        print hash_map
        stack[index], stack[last_index] = stack[last_index], stack[index]
        print "Delete: %s, from: %s"%(stack.pop(), index)
        hash_map[stack[index]] = index
        hash_map.pop(val)
        print hash_map
        last_index = last_index - 1

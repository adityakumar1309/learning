def comparator(a, b): 
	ab = str(a) + str(b) 
	ba = str(b) + str(a) 
	if (int(ba) > int(ab)):
	    return 1
	elif (int(ba) < int(ab)):
	    return -1
	elif int(ba) == int(ab):
	    return 0
	    
	#return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 
	
# driver code 
if __name__ == "__main__": 
	a = [54, 546, 548, 60, ] 
	sorted_array = sorted(a, cmp=comparator) 
	number = "".join([str(i) for i in sorted_array]) 
	print(number) 

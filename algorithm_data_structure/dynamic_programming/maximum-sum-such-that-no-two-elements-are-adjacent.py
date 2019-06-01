def find_max_sum(arr): 
    incl = 0
    excl = 0
     
    for ele in arr: 
	_temp = incl
        incl = max(excl + ele, incl) 
	excl = _temp         

    return max(excl, incl) 
  
arr = [5, 5, 10, 100, 10, 5] 
print find_max_sum(arr) 

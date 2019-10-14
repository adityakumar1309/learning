arr = [10, 20, 30, 40] 

excl = 0 
incl = 0 

for ele in arr:
    temp = incl
    #when i include(not include but consider the ele what is my incl sum)
    incl = max(excl+ele, incl)
    excl = temp

print(max(incl, excl))
~                           

import numpy as np
ls = eval(input("enter the integer values:- "))
arr = np.array(ls)

print(arr)
print("Size of the memory occupied by the array: %d bytes" % (arr.size * arr.itemsize))

print(ls)
print("Size of the memory occupied by the list: " , (ls.__sizeof__()) , "bytes")
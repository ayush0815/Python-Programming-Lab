import numpy as np
ls = eval(input("enter the elements"))
arr = np.array(ls)
print(arr)
flag = 0
for i in arr:
    if i<=100:
        flag = 0
    else:
        flag = 1
if flag == 0:
    print('None of the element of array is greater than 100')
else:
    print('Element(s) of the array is greater than 100')
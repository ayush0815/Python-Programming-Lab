import numpy as np
ls = eval(input("enter the elements"))
arr = np.array(ls)
print(arr)
num = int(input('enter a number you want to delete'))
for i in arr:
    if i>=num:
        del arr[i]
print(arr)
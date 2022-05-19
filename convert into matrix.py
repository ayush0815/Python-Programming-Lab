import numpy as np
ls = list(map(int,input().split()))
object = np.array(ls)
arr = object.reshape(3,3)
print(arr)
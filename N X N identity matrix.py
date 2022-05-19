import numpy as np
order = int(input("enter the order of the matrix:-"))
matrix = np.eye((order))
print(f'The identity matrix of {order}X{order} is:-')
print(matrix)
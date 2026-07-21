import numpy as np
# 1D array
arr=np.arange(1,21)
print('1D array:',arr)

#5X5 zero matrix
Z=np.zeros((5,5))
print('5X5 zero matrix:\n',Z)

#4X4 identity matrix
I=np.eye(4)
print('4X4 identity matrix:\n',I)

#even space between 10-50
even_arr=np.linspace(10,50,10)
print('evenly spaced array:\n',even_arr)

print('attributes of the array:')
print('shape:',arr.shape)
print('Dimension:',arr.ndim)
print('data type:',arr.dtype)
print('size:',arr.size)
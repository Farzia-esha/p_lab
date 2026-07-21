import numpy as np
arr=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print('\nFirstRow:',arr[0,:]) 
print('\nLastColumn:',arr[:,-1])
print('\nSubArray:',arr[0:2,0:2])

arr[1,1]=99 #modify

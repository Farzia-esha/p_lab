import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

print("Addition:\n",A+B)
print("Multiplication:\n", np.matmul(A,B))
print("Transpose of A:\n",A.T)
print("Determinant of A:\n", np.linalg.det(A))
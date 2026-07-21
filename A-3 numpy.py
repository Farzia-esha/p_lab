#Assignment 3: Numpy

#task 1: create arrays
import numpy as np

# a) 1D array (1 to 20)
arr1 = np.arange(1, 21)
print("1D Array:\n", arr1)

# b) 5x5 zero matrix
zero_matrix = np.zeros((5, 5))
print("\n5x5 Zero Matrix:\n", zero_matrix)

# c) 4x4 identity matrix
identity_matrix = np.eye(4)
print("\n4x4 Identity Matrix:\n", identity_matrix)

# d) Evenly spaced values between 10 and 50
even_array = np.linspace(10, 50, 10)
print("\nEvenly Spaced Array:\n", even_array)

#task2: Array Attributes
print("\n--- Array Attributes ---")
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Data Type:", arr1.dtype)
print("Size:", arr1.size)

 #task 3:indexing & slicing
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# a) First row
print("\nFirst Row:", arr2[0, :])

# b) Last column
print("Last Column:", arr2[:, -1])

# c) Subarray (first 2 rows & first 2 columns)
print("Subarray:\n", arr2[0:2, 0:2])

# d) Modify value
arr2[1, 1] = 99
print("Modified Array:\n", arr2)

#task 4: mathematical operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\n--- Mathematical Operations ---")
print("Addition:", np.add(a, b))
print("Subtraction:", np.subtract(a, b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))
print("Dot Product:", np.dot(a, b))

#task 5:Statistical calculations
data = np.array([10, 20, 30, 40, 50])

print("\n--- Statistics ---")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))

#task 6:multi D Array
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\n--- Matrix Operations ---")
print("Addition:\n", A + B)
print("Multiplication:\n", np.matmul(A, B))
print("Transpose of A:\n", A.T)
print("Determinant of A:", np.linalg.det(A))

#task 7:Reshaping Arrays
arr = np.arange(1, 13)

reshaped = arr.reshape(3, 4)
print("\nOriginal Array:\n", arr)
print("Reshaped Array (3x4):\n", reshaped)

#task 8: Real-life mini problem
marks = np.array([75, 80, 65, 90, 85])

print("\n--- Student Analysis ---")

# Average
print("Average Marks:", np.mean(marks))

# Highest
print("Highest Marks:", np.max(marks))

# Filter > 80
high_scores = marks[marks > 80]
print("Marks above 80:", high_scores)

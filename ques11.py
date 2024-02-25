import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("A: \n", A)
print("A transpose: \n", A.T)

print("A + B: \n", A + B)

print("A - B: \n", A - B)

print("A * B: \n", np.dot(A, B.T))

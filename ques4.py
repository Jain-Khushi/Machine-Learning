import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
array

array_2D = np.array([[1, 2, 3, 4, 5, 6],[2, 4, 6, 1, 9, 10]])
array_2D

array_1s = np.ones(10)
array_1s

array_0s = np.zeros(10)
array_0s

array_ran = np.random.randint(100, size=(5))
array_ran

x = np.arange(16).reshape((4,4))
diag = np.diag(np.diag(x))
print(diag)
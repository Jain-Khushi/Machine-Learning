import pandas as pd
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(3,4)
print(arr)
print("shape is   :")
print(np.shape(arr))

print("number of rows : ")
print(np.shape(arr)[0])


print("number of columns : ")
print(np.shape(arr)[1])

arr2=np.zeros(12).reshape(3,4)

print("the array is stored to arr.txt")
np.savetxt("arr.txt",arr,fmt='%.2e')
print("\n\n")


print("array is loaded from arr.txt")
arr2=np.loadtxt("arr2.txt",dtype=int)
print(arr2)

import pandas as pd
import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(3,4)
arr2=np.array([6,3,4,7,5,4,1,3,23,2,1,1]).reshape(3,4)
arr3=np.array([6,3,4,7,5,4,1,3,23,2,1,1]).reshape(4,3)
print("arr1")
print(arr1)
print("arr2")
print(arr2)
print("arr3")
print(arr3)




case=-1
while case!=0:

    print("MENU:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("0.exit")
    case = int(input("enter the choice   :"))
    if case==1:
        print("addition")
        print(arr1 + arr2)

    if case==2:
        print("subtraction")
        print(arr1 - arr2)

    if case==3:
        print("multiplication")
        print(arr1.dot(arr3))






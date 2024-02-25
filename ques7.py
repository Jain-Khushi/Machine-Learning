import pandas as pd
import numpy as np

arr1=np.array([-1,-2,3,-4,-5,6,7,-8,9,10,-11,-12]).reshape(3,4)
print("arr1")
print(arr1)

case=-1
while case!=0:
    print("MENU")
    print("1.abosulte values")
    print("2.negetive")
    print("3.max of a row / column")
    print("4.min of a row / column")
    print("5.add row / column")
    print("6.delete row column")
    print("0.exit")
    case=int(input("Enter the choice    :"))
    if case==1:
        print("absolute values ")
        print(np.abs(arr1))
    if case==2:
        print("taking negetive of matrix values   :")
        print(arr1 * -1)
    if case==3:
        ch=input("row or column(r/c)  : ")
        if ch=="r":
            r=int(input("enter the row number   : "))
            print(np.max(arr1[r]))
        if ch=="c":
            c=int(input("enter the column number number   : "))
            print(np.max(arr1[:,c]))
    if case==4:
        ch=input("row or column(r/c)  : ")
        if ch=="r":
            r=int(input("enter the row number   : "))
            print(np.min(arr1[r]))
        if ch=="c":
            c=int(input("enter the column number number   : "))
            print(np.min(arr1[:,c]))

    if case==5:
        ch = input("row or column(r/c)  : ")
        if ch=="r":
            inp=np.zeros(4)
            print("enter 4 elements")
            for i in range(4):
                inp[i]=int(input("enter element : "))
            res=np.insert(arr1,arr1.shape[0],[inp],axis=0)
            print(res)
        if ch=="c":
            inp = np.zeros(3)
            print("enter 3 elements")
            for i in range(3):
                inp[i] = int(input("enter element : "))
            res=np.column_stack((arr1,inp))
            print(res)
    if case==6:
        ch = input("row or column(r/c)  : ")
        if ch=="c":
            c=int(input("enter the column number to be deleted  : "))
            print(np.delete(arr1,c,1))
        if ch=="r":
            r=int(input("enter the row number to be deleted  : "))
            print(np.delete(arr1,r,0))
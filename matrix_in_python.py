'''
Creating Matrix in Python using matrix function
Date-1st Nov 2020
'''
from numpy import *
arr1=[]
arr2=[]
r1=int(input("Enter the number of rows for arr1:"))
c1=int(input("Enter the number of column for arr1:"))
r2=int(input("Enter the number of rows for arr2:"))
c2=int(input("Enter the number of column for arr2:"))
n=int(input("Enter number of elements of arr1:"))
s=int(input("Enter number of elements of arr2:"))
for i in range(n):
    arr1.append(int(input("Next")))
for j in range(s):
    arr2.append(int(input("Next")))  
arr1=array(arr1)#converting list into array
arr2=array(arr2) 
arr3=arr1.reshape(r1,c1)#specifies rows and column
arr4=arr2.reshape(r2,c2)     
m1=matrix(arr3)#converts into matrix
m2=matrix(arr4)
print(m1)
print(m2)
print(diagonal(m1))#diagonal elements
print(m1*m2)#matrix multiplication
print(m1.shape)#(row,column)




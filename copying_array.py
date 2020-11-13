'''
Important-To understand axes in numpy refer to https://www.sharpsightlabs.com/blog/numpy-axes-explained/
In case you dont want to use append of numpy.Refer below(less time complexity):
import numpy as np 
l = [] 
for i in range(4): 
  a =int(input("enter"))
  l.append(a) 
l = np.array(l)
print(l)
Date-31st Oct 2020
'''
from numpy import *
arr1=array([],int)
arr2=array([],int)
arr3=[]
arr4=[]
n=int(input("Enter the length of arr1: "))#length must be same 
s=int(input("Enter the length of arr2: "))
for i in range(n):
    arr3.append(int(input()))
for i in range(s):
    arr4.append(int(input()))
#arr-Input array
#values-To be appended to arr. It must be of the same shape as of arr (excluding axis of appending)    
arr1=append(arr1,[arr3])#append(arr,values,axis)
arr2=append(arr2,[arr4]) 
print(arr1)#[1 2]
print(arr2)#[3 4]  
print(arr1+arr2)#[4 6]
print(arr1+5) #[1+5,2+5]=[6,7]  
print(concatenate([arr1,arr2]))#[1 2 3 4] 

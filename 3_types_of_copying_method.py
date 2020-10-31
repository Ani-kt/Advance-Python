'''
3 methods for copying.
Difference between deep copy and shallow copy.
Deep copy doesnot change once copied even after changing values of main array.
Shallow copy changes.
Date-31st Oct 2020
'''
from numpy import *
#normal_copy
arr=array([1,2,3,4])
arr1=arr
print(arr1)#[1 2 3 4]
print(id(arr1),id(arr))#115491288 115491288
#shallow_copy
arr1=arr.view()
arr[0]=7
print(arr)#[7 2 3 4]
print(arr1)#[7 2 3 4]
print(id(arr1),id(arr))#120216016 120184168
#deep_copy
arr2=array([1,2,3,4])
arr3=arr2.copy()
arr2[0]=7
print(arr2)#[7 2 3 4]
print(arr3)#[1 2 3 4]
print(id(arr2),id(arr3))#63527536 4296736


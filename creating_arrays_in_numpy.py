'''
For multidimensional array,numpy module is used
In numpy,typecode mentioning is optional.
If typecode mentioned,its syntax is array([Initializers],typecode)
Date-31st oct 2020
'''
from numpy import *
#Here,according to typecode the initializers will get change 
arr=array([1,2,3,4,5.0]) #[1.2.3.4.5.]
print(arr)
#numpy.linspace(start,stop,num = no. of samples,endpoint = True,retstep = False,dtype = None(type of o/p array))
#If the endpoint is set to false, then the end value is not included in the sequence.By default it's True
arr1=linspace(0,2,5,retstep=False)#[0. 0.5 1. 1.5 2. ]
arr2=linspace(0,2,5,retstep=True)#(array([0. , 0.5, 1. , 1.5, 2. ]), 0.5)
print(arr1)
print(arr2)
arr3=zeros(3)
print(arr3)#[0. 0. 0.]
arr4=ones(3,int)
print(arr4)#[1 1 1]
#addition
arr5=array([1,2,3,4])
arr6=arr5+3
print(arr6)#[4 5 6 7]
arr7=array([2,5,6,3])
print(arr7+arr5)#[3 7 9 7]
print(sin(arr7))#[ 0.90929743 -0.95892427 -0.2794155   0.14112001]
                #cos,log,sum,sqrt,min,max,sort etc maths functions are under numpy
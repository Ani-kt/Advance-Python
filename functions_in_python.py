'''
Functions are helpful during projects.
Python dont have a concept of call by reference and call by value.
Imp-In python when we pass a value the adresses remains same until we change the value 
the address will get change.Refer below.(Only for immutables)
Refer below for mutables.(all addresses remains same even if value changes)
Date-1st Nov 2020
'''
def add_mul(a,b):
    c=a+b
    d=a*b
    return c,d
print(add_mul(4,3))#(7,12) 
#address remains same until value changes
def value(x):
    print(id(x))#261645632
    x=9
    print(id(x))#261645616
    return x
a=10
print(id(a))#261645632
print(value(10))#9 
#address remains same even if we change the all value  
def val(lst):
    print(id(lst))#6830720
    lst[0]=2
    lst[1]=6
    lst[2]=1
    print(id(lst))#6830720 
    return lst    
lst=[3,4,5]
print(id(lst))#6830720
print(val(lst))#[2, 6, 1]    
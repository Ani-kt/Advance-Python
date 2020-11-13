"""
Global function is used when we want to make the variable outside the function to behave as global variable
which is declared inside function.It can also change the value of global variable.
Global keyword is used when we want global variable which is present inside the function.(function body)
Date-2nd Nov 2020
"""
#normal way
b=10
def f():
    b=9
    print("IN ",b)
f()
print("OUT ",b) 
print()   
#global keyword
a=10
def func():
    global a
    a=9
    print("IN ",a)#9
    #a=8
func()
print("OUT ",a)#9
print()
#global function
c=7
def ff():
    c=9
    #when we are writing c here,it is accessing the c varibale which is outside the function that is 7.
    x=globals()['c']
    print("IN ",c)#9
    #we can also change the global variable inside the function.
    globals()['c']=12
ff()
print("OUT ",c) #12       
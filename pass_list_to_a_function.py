'''
Input-10 list of names
Output-number of names which have letters more than 5
Date-2 Nov 2020
'''
def count(lst):
    c=0
    for i in lst:
        if len(i)>5:
            c+=1
    return c        
lst=[]
for i in range(3):
    lst.append(input("Name: "))
count(lst)    
print(count(lst))
#........Fibbonaci series.........
def fib(n):
    l=[0,1]
    a,b=0,1
    for j in range(2,n):
        l.append(a+b)
        a=b
        b=a+b    
    return l   
n=int(input("Enter number of series: "))
s=fib(n)
print(s) 
print(*s)
print(*s,sep=", ")
#........Factorial of a number.......
def factorial(n):
    mul=1
    for i in range(1,n+1):
        mul*=i
    return mul    
n=int(input("Enter a number: "))
print(factorial(n))  
#......Factorial using recursion....
def fac(a):
    if a==1:
        return 1
    else:
        return a*fac(a-1) 
print(fac(5))                

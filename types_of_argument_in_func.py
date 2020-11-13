"""
4 types of argument-1.Position 2.Default 3.Keyword 4.Varibale length 5.Keyword variable length 
Date-1st Nov 2020
"""
#position
def sum(a,b):
    return a+b
print(sum(5,6))#11
#default
def info(name,age=16):
    print(name,age)#Yash 16
info("Yash") #or info("yash",age=20)
#Keyword 
def infor(name,age):
    age-=2
    print(name,age)
infor(age=5,name="R")#R 3
#variable length
def summ(a,*b):
    sum=a
    for i in b:
        sum+=i
    print(sum)    
summ(2,3,4,5,6,7)#27
#or
def addition(*b):
    print(b)#(2, 3, 4, 5),returns a tuple
    sum=0
    for i in b:
        sum+=i
    print(sum)
addition(2,3,4,5) #14 
#keyword variable length
def person(name,**data):
    print(name)#xxx
    print(data)#{'age': 15, 'home': 'Delhi', 'mob': 37898},returns a dictionary
    for i in data:
        print(i,data[i])
person("xxx",age=15,home="Delhi",mob=37898)#age 15
                                           #home Delhi
                                           #mob 37898                  
            

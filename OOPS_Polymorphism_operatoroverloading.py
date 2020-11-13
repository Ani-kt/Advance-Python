"""
Operator Overloading
Date-12th Nov 2020
"""
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        a1=self.m1+ other.m1
        a2=self.m2+ other.m2
        s3=Student(a1,a2)
        return s3
    def __gt__(self,other):
        print("hello")
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        print(r1)
        print(r2)
        if r1>r2:
            return True
        else:
            return False  
    def __str__(self):
        return self.m1,self.m2         

n1=int(input())  
n2=int(input())      
s1=Student(n1,n2)
s2=Student(23.5,4.5)
s3=s1+s2
print(s3.m1)
if s1>s2:
    print("greater")
else:
    print("smaller") 
a=9
print(a)
print(s1.__str__())       



"""
Python doesnot have concept of method overloading(a class having same method name with different arguments).
In python we cannot create two methods with the same name within a class.
Date-13th Nov 2020
"""
#Method overloading(in an indirect way as direct way not possible in python)
class A:
    def sum(self,*a):#variable length argument
        print(a)
        s=0
        for i in a:
            s+=i
        return s
s1=A()
print(s1.sum(2,3,4)) 
#Method overriding 
class B:
    def show(self):
        print("in B")
class C(B):
    def show(self):
        print("in C")
c=C()
c.show()                          

"""
Inheritance-Inheritance is a powerful feature in object oriented programming.
It refers to defining a new class with little or no modification to an existing class. 
The new class is called derived/child/sub class 
and the one from which it inherits is called the base/parent/super class.
Date-11th Nov 2020
"""
#single level inheritance
class A:
    def feature1(self):
        print("feature1")
class B(A):
    def feature2(self):
        print("feature2") 
a1=A()
a1.feature1()
b1=B()
b1.feature1()
b1.feature2()
#multi level inheritance
class A:
    def feature3(self):
        print("feature3")
class B(A):
    def feature4(self):
        print("feature4") 
class C(B):
    def feature5(self):
        print("feature5")
a3=A()
a3.feature3()
b4=B()
b4.feature3()
b4.feature4() 
c5=C()
c5.feature3()
c5.feature4()
c5.feature5() 
#multiple inheritance
class A:
    def feature6(self):
        print("feature3")
class B:
    def feature7(self):
        print("feature4") 
class C(A,B):
    def feature8(self):
        print("feature5") 
a4=A()
a4.feature6()
b5=B()
b5.feature7()
c6=C()
c6.feature6()
c6.feature7()
c6.feature8()                      

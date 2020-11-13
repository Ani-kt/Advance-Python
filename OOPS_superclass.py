"""
MRO(Method Resolution Order)-left to right always
Date-11th Nov 2020
"""
class A:
    def __init__(self):
        print("in init A")
    def feature1(self):
        print("feature 1")
class B():
    def __init__(self):
        print("in init B")
    def feature1(self):
        print("feature 2")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("in init C")            
c=C() 
c.feature1()# Because of MRO, left class get access first          

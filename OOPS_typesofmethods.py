"""
3 types of methods
1.class method-@classmethod
2.static method-@staticmethod
 We cannot assign or change anything here.
3.instance method
    1.Accessor method
    2.Mutators method
Date-11th Nov 2020
"""
class School:
    schoolname="KV"
    def __init__(self):
        self.m1=9
        self.m2=19
        self.m3=27
    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)//3
    def get_m1(self): #accessor method
        return self.m1
    def change_m1(self,value):#mutator method
        self.m1=value
        return self.m1 
    @classmethod
    def schl(cls):
        cls.schoolname="Dav"
        return cls.schoolname 
    @staticmethod
    def numberofstudent():
        return 55  

s1=School()
s2=School() 
print(s1.avg())
print(s1.get_m1()) 
print(s1.change_m1(3)) 
print(School.schl())
print(School.numberofstudent())







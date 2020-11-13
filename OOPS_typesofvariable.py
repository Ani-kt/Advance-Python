"""
2 types of variable:
1.Class/static variable-written before init method
2.Instance variable-written under init method
Date-10th Nov 2020
"""
class Car:
    wheels=4 #class variable
    def __init__(self):
        self.company="audi" #instance variable
        self.features="good" #instance variable
c1=Car()
c2=Car()
Car.wheels=5 #variable changes
print(c1.company,c1.features,c1.wheels)
print(c2.company,c2.features,c2.wheels)        
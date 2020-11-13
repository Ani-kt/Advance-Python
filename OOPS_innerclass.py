"""
We can create object of inner class inside the outside class.
Or can create object outside the class by using outer class name.
Date-11th Nov 2020
"""
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        #self.lap=self.Laptop()
    def show(self):
        print(self.name,self.roll)
        #self.lap.show

    class Laptop:
        def __init__(self,laptop,ram):
            self.laptop=laptop
            self.ram=ram
        def show(self):
            print(self.laptop,self.ram)            
s1=Student("navin",4)
s2=Student("ani",5)
s1.show()
lap1=Student.Laptop("hp",32)
lap2=Student.Laptop("dell",8)
lap1.show()
lap2.show()

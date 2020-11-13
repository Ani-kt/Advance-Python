"""
Polymorphism-Poly-Many Morphism-Forms
4 types-Ducktyping,Method overloading,Operator overloading,Method overridding
Date-12th Nov 2020
"""
class VC:
    def execute(self):
        print("Compiling")
        print("Running")
class Codeblocks:
    def execute(self):
        print("syntax detector")        
class Laptop:
    def info(self,ide):
        ide.execute()
ide=VC()        
lap1=Laptop()
lap1.info(ide)        
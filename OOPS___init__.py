"""
Class is a blue print(design) of an object(thing).
To define attributes(variables),we need __init__method.
To define behaviours,we need methods(function).
Date-10th Nov 2020
"""
class Computer:
    def __init__(self,a,b):
        self.a=3
        self.b=b
    def config(self):
        print("config is",self.a,self.b)
com1=Computer("lenovo","32")
com1.a=4
com2=Computer("dell","16") 
com1.config() #Computer.config(com1)   
com2.config() #Computer.config(com2) 
if com1.a==com2.a:
    print("same") 
else:
    print("different")            

'''
Arrays have elements which are of same type whereas list can have elements of different type.
Arrays in Python can expand or shrink as per our need.
'''
# * is used to import everything from array module.
from array import *
value=array("u",["a","b","c"])#arrayName = array(typecode, [Initializers])
print(value.typecode) #u(unicode character)
val=array(value.typecode,(j for j in value))#copying the above array(value)
for i in val:
    print(i,end="")#abc
print()       
val.reverse()#reversing val
print(val)#array('u', 'cba')    

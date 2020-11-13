"""
Lamda function is used when only one operation is/have to be done.
Filter function filters out the required output within the given iterables(list,float etc)
Map function does some operations.
Map and Filter always returns some iterables like list,float.
Reduce function gives a single value.Import functools module for reduce function
Date-2nd Nov 2020
"""
import functools
#functions are object in python,so we have to store the value in variable
f=lambda a,b:a+b#many arguments but only one expression
print(f(4,5))#function doesnot have name in lambda
#......filter.......
nums=[3,4,2,5,7,89]
#syntax-filter(function,iterables)
res=list(filter(lambda n:n%2==0,nums))
print(res)
#.......map.....
#syntax-map(function,iterables)
doubles=list(map(lambda n:n*2,res))
print(doubles)
#.........reduce........
sum=functools.reduce(lambda a,b:a+b,doubles)
print(sum)


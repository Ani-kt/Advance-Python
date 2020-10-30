'''
Array values from user input
Date-30th Oct 2020
Note- All Inputs are randomly taken. 
'''
import array as arr
values=arr.array('i', []) #empty array
n=int(input("Enter the length of array:")) #4(let)
for i in range(n):
    #append method adds an element to the end of the array
    values.append(int(input("Enter elements of array:"))) #1,6,7,8(let)
print(values) #array('i', [1,6,7,8])
s=int(input("Enter the element that needs to be deleted: ")) #6(let)
for j in range(len(values)): #deleting an element
    if s==values[j]:
        continue    #skips the current iteration,jumps to the next iteration
    print(values[j],end="") #178   
print() 
values.remove(s) #remove function doesnot return anything,it updates the array
print(values) #array('i', [1,7,8])
values.extend([2,3]) #add elements to the end of the array
print(values) #array('i', [1,7,8,2,3])
k=len(values)-1 #reversing the array 
while(k>=0):
    print(values[k],end="") #32871
    k-=1


        
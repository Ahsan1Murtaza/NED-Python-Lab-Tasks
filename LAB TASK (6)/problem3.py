# 3.   Write the relevant Python expression or statement, involving a list of numbers lst and using list operators and methods for these specifications: 
# (a)An expression that evaluates to the index of the middle element of lst 
# (b)An expression that evaluates to the middle element of lst 
# (c)A statement that sorts the list lst in descending order 
# (d)A statement that removes the first number of list lst and puts it at the end 
# Note: If a list has even length, then the middle element is defined to be the rightmost of the two elements in the middle of the list.
from math import *
lst=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    element=int(input("Enter elements : "))
    lst.append(element)
if len(lst)%2!=0:
    middle_element=floor(len(lst)/2)
    print(f"The index of middle element is {middle_element}") # it will show index of middle element
    print(f"The middle element is {lst[middle_element]}")
elif len(lst)%2==0:
    middle_element=int(len(lst)/2)
    # middle_element=floor(len(lst)/2)
    print(f"The index of middle element is {middle_element}") # it will show index of middle element
    print(f"The middle element is {lst[middle_element]}")
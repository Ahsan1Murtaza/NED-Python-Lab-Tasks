# 7. Write a program which will multiply two square matrices. 
from os import system
system("cls")
x=[]
y=[]
print("Enter values of first matrix")
for i in range(1,5): #for 1st matrix
    valuesA=int(input("Enter values from left to right : "))
    x.append(valuesA)
print("Enter values of second matrix")
for i in range(1,5): #for 2nd matrix
    valuesB=int(input("Enter values from left to right : "))
    y.append(valuesB)
print("The mutliplication of both the matrix is : ")
print(((x[0]*y[0])+(x[1]*y[2])),end=" ")
print(((x[0]*y[1])+(x[1]*y[3])))
print(((x[2]*y[0])+(x[3]*y[2])),end=" ")
print(((x[2]*y[1])+(x[3]*y[3])))
# 6. Write a program which will add two square matrices
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
print("The addition of both the matrix is : ")
for i in range(0,4):
    if i==2:
        print("\n")
    print((x[i]+y[i]),end="  ")




    

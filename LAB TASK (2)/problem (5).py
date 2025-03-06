# 5. Write a program that prompts the user to enter number in two variables and swap the contents of the variables  
a=int(input("(a).Enter number : "))
b=int(input("(b).Enter number : "))

a,b=b,a #swapping two variables
print("After swapping variables")
print("The number in (a) is now",a)
print("The number in (b) is now",b)
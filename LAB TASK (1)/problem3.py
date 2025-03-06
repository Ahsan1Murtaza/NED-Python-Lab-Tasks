#Write a program to calculate area of rectangle
from math import*
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
area=length*breadth
print("The exact area of rectangle is :",area," meter square")
#ADDITIONAL
print("Rounded area is: ",round(area)," meter square")
print("ROund up area is :",ceil(area)," meter square")
print("Round down area is :",floor(area)," meter square")
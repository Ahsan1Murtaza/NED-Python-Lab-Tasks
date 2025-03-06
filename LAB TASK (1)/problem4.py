#Write a program to calculate the volume of a sphere
from math import* 
r=float(input("Enter radius of sphere :"))
vol=((4/3)*pi*r*r*r)
print("Volume of sphere is :",vol,"meter cube")
#ADDITIONAL
print("Rounded volume is: ",round(vol)," meter volume")
print("ROund up volume is :",ceil(vol)," meter volume")
print("Round down volume is :",floor(vol)," meter volume")
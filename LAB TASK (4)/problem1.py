# 1. Write a program which solves the quadratic equation. The user will enter the value of a, b and c. 
# The program will then check the denominator that if denominator is zero or not. If its zero it can 
# reply the equation cannot solve as there is a zero division else, it will execute the program and will 
# # generate two solutions
a=4
b=3
c=6
discriminant=((b**2)-(4*a*c))**0.5
sol2=(-b-discriminant)/(2*a)
sol1=(-b+discriminant)/(2*a)
print("The root 1 is ",sol1,"and root 2 is ",sol2)
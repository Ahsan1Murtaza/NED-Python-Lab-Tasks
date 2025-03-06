# 2.   A ladder put up right against a wall will fall over unless put up at a certain angle less than 
# 90 degrees. Given variables length and angle storing the length of the ladder and the  angle 
# that  it  forms  with  the  ground  as  it  leans  against  the  wall,  write  a  Python  expression 
# involving length and angle that computes the height reached by the ladder. Evaluate the 
# expression for these values of length and angle: 
# (a)16 feet and 75 degrees 
# (b)20 feet and 0 degrees 
# (c)24 feet and 45 degrees 
# (d)24 feet and 80 degrees 
# Note: You will need to use the trig formula: 
# height = length * sin(angle) 
# The math module sin() function takes its input in radians. You will thus need to convert 
# the angle given in degrees to the angle given in radians using: 
# radians = π * degrees / 180 
from math import *
# (a)16 feet and 75 degrees
l1=16
deg1=75
rad1=pi * (deg1/180) 
h1=l1*sin(rad1)
print(f"The height of ladder at angle {deg1} and length {l1} is {h1}")
# (b)20 feet and 0 degrees 
l1=20
deg1=0
rad1=pi * (deg1/180) 
h1=l1*sin(rad1)
print(f"The height of ladder at angle {deg1} and length {l1} is {h1}")
# (c)24 feet and 45 degrees 
l1=24
deg1=45
rad1=pi * (deg1/180) 
h1=l1*sin(rad1)
print(f"The height of ladder at angle {deg1} and length {l1} is {h1}")
# (d)24 feet and 80 degrees 
l1=24
deg1=80
rad1=pi * (deg1/180) 
h1=l1*sin(rad1)
print(f"The height of ladder at angle {deg1} and length {l1} is {h1}")
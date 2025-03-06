# Program 9: You are planning to throw a small bird at a distance d, with time t, and height h to some structure. Write a code in which you will use the physical quantities such as initial velocity,final velocity, angle in radians, gravity, height, sling shot etc. 
import math 
# User inputs 
velocity = float(input('Give me a velocity to fire at (in m/s): ')) 
angle = float(input('Give me an angle to fire at: ')) 
distance = float(input('Give me how far away you are from the structure: ')) 
height = float(input('Give me the height of the structure (in meters): ')) 
slingshot = 5 #Height of slingshot in meters 
gravity = 9.8 #Earth gravity 
# Converting angles to radians 
angleRad = math.radians(angle) 
# Computing our x and y coordinate 
x = math.cos(angleRad) 
y = math.sin(angleRad) 
# Calculations 
time = distance/(velocity * x) 
vx = x 
vy = y + (-9.8 * time) 
finalVelocity = math.sqrt((vx ** 2) + (vy ** 2))
# Program 5: Write a program to perform identity operator. 
x = ["ahmed", "bashir"] 
y = ["ahmed", "bashir"] 
z = x 
print(x is z) 
print(x is y) #(false) b/c its equal but not same object
print(x == y)

#Additional
print(x is not y)
print(not(x is y)) # it will negate wrong answer and produce correct one
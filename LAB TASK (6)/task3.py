# Program 3: Write a Python function which takes no argument and generate and print a list of first and last 6 elements where the values are cube of numbers between 1 and 30 (both included).

# By list comprehension
list1=[x**3 for x in range(1,31) if not(6<x<25)]
print(list1)

list2=[]
for i in range(1,31):
    list2.append(i**3)
print(list2[:6])
print(list2[-6:])
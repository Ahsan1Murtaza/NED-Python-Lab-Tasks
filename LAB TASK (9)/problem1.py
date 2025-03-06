# 1.   Write a program which will add your best five students name in a set. You will use a loop to insert names in set.
best_students=set()
for i in range(5):
    name=input(f"Enter {i+1} best student name : ")
    best_students.add(name)
print(f"The best 5 students are {best_students}")
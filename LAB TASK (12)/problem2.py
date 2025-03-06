#  Q.2   Define a list, consisting of names of different students, who are applying for a scholarship, pop an item from that list and transfer all items in a new list and apply sample method of random module to  give scholarship to two students of new list.
from random import *
students=["Ali","Amir","John","Alex","Adil"]
print(students)
students.pop()
print(students)
new_students=list(students) # new student list after pop
two_scholarship_student=sample(new_students,2)
print(two_scholarship_student)
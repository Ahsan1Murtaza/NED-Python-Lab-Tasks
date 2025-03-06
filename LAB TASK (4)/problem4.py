# 4. Write a program which will collect your name, your father’s name, your roll number and your subjects (5 Subjects with name and numbers). At the end it will generate a result with your name,  your father’s name, your details subjects, marks you have obtained with total marks with grade and percentage
from os import system
system("cls")
name=input("ENTER YOUR NAME : ")
father_name=input("ENTER YOUR FATHER'S NAME : ")
roll=int(input("ENTER YOUR ROLL NUMBER : "))
i=1
subject=5
x=[]
y=[]
sum=0
while(subject>=1): 
    subject_name=input(f"{i} Enter subject name : ")
    marks=int(input("Enter marks : "))
    if marks<0 or marks>100:
        print("Invalid marks")
        continue
    else:
        sum+=marks
        x.append(subject_name)
        y.append(marks)
        i+=1
        subject-=1
system("cls")
print("Name:".center(50),name)
print("Father's Name:".center(50),father_name)
print("Roll Number:".center(50),roll,end="\n\n")
print("SUBJECT".center(50),"MARKS",end="\n")
for i in range(0,5):
    print(x[i].center(50),y[i])
percentage=(sum/500)*100
print("\n")
print("TOTAL MARKS".center(50),sum,"/500")
print("PERCENTAGE".center(50),percentage,"%")


if(percentage>=80 and percentage<=100):
    print("Your grade is A one")
elif(percentage>=70 and percentage<80):
    print("Your grade is A")
elif(percentage>=60 and percentage<70):
    print("Your grade is B")
elif(percentage>=50 and percentage<60):
    print("Your grade is C")
elif(percentage>=0 and percentage<50):
    print("Your grade is F")
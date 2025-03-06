#Problem 3: Write a program that asks the user to enter their name and their age. Print out a 
#message addressed to them that tells them the year that they will turn 100 years old.

name=input("Enter your name : ")
age=int(input("Enter your age : "))
birthday=input("Have you celebrated your birthday (yes/no) :")
if birthday=="yes":
  year1=2024+(100-age)
  print(name,"You will be 100 years old in ",year1)
elif birthday=="no":
  year2=2023+(100-age)
  print(name,"You will be 100 years old in ",year2)
else:
  print("INVALID ANSWER")
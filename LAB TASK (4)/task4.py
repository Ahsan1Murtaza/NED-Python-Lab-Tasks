# Program 4: Write a program which takes the lower limit and upper limit then find which of the number 
# are prime number. 
# Code: 
# Python program to display all the prime numbers within an interval 
l_limit = int(input("Enter lower limit range: ")) 
u_limit = int(input("Enter upper limit range: ")) 
print("Prime numbers between",l_limit,"and",u_limit,"are:") 
for number in range(l_limit,u_limit + 1): 
    if number > 1: 
       for i in range(2,number): 
          if (number % i) == 0: 
            break 
       else: 
            print(number)
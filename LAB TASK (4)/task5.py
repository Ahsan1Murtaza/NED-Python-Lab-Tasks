# Program 5: Write a program which takes the initial and final values from the user then print the sum of all the number. 
initial_value = int(input("Enter the initial value for the range :")) 
final_value = int(input("Enter the final value for the range :")) 
numbers = range(initial_value,final_value+1) 
sum = 0 
for value in numbers: 
   sum = sum+value 
print("The sum is", sum)
 
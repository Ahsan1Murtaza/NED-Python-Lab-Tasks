# Program 3: Write a program which takes the limit for while loop condition and sum the total amount. 
# Code:
limit=int(input("Enter limit for while loop and gets sum of it : "))
i=1
sum=0
while i<=limit:
    sum=sum+i
    i+=1
print(sum)
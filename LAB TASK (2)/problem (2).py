# 2. Write a program which accept principle, rate and time from user and print the simple interest. The formula to calculate simple interest is: 
# simple interest = principle x rate x time / 100  
principle_amount=int(input("Enter principle amount : "))
rate=int(input("Enter rate : "))
time=int(input("Enter time : "))
interest=(principle_amount*rate*time)/100
print("The interest on",principle_amount,"at rate",rate,"and time",time,"is",interest)
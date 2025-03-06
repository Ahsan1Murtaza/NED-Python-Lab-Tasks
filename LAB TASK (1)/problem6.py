# The formula to calculate compound interest annually is given by:  
# A = P(1 + R/100) t  
# Compound Interest = A – P  
# Where,  
# •     A is amount  
# •     P is the principal amount  
# •     R is the rate and  
# •     T is the time span 
# Calculate the compound interest by taking input from the user by using 
# above formula.

principal_amount=float(input("Enter principal amount : "))
rate=float(input("Enter rate : "))
time=float(input("Enter time span in years : "))
amount=principal_amount*((1+(rate/100))**time)
compund_interest=amount-principal_amount
print("The Compound interest will be : ",compund_interest)

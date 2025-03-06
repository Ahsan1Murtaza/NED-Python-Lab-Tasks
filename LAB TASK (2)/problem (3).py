# 3. Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule: 
print(''' Minimum Rs. 2000 for up to 100 calls. 
Plus Rs. 0.60 per call for next 50 calls. 
Plus Rs. 0.50 per call for next 50 calls. 
 Plus Rs. 0.40 per call for any call beyond 200 ''')
call=int(input("Enter number of calls : "))
if(call<=100 and call>0):
    price=2000
    print("Total bill is",price,"Rs.")
elif(call>100 and call<=150):
    price=2000+(call-100)*0.60
    print("Total bill is",price,"Rs.")
elif(call>150 and call<=200):
    price=(2000+(0.60*50))+(call-150)*0.50
    print("Total bill is",price,"Rs.")
elif(call>200):
    price=(2000+(0.60*50)+(0.50*50))+(call-200)*0.40
    print("Total bill is",price,"Rs.")

# 3. Write a program which will check either the giving string is Palindrome or not. Palindrome is a 
# string when we reverse the string it will generate the original string. Example CIVIC, MOM, 010, 
# 1001, etc. So if you enter the word which is Palindrome it will say yes your string is Palindrome 
# otherwise it will generate sorry message. 

#first way
my_string=input("Enter any phrase ")
y=my_string.casefold()
x="".join(reversed(y))
if x==y:
    print("your phrase is a palindrome")
else:
    print("Sorry")


# print("\n")
# # another way
# reversed_string=my_string[::-1]
# print("The reversed of given is ")
# print(reversed_string)
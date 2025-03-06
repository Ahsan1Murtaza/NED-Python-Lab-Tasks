# 2. Write a function to design a personal phone directory of your parents and friends. You must add 12 members. Then make a function to delete a member from a telephone directory. Print total number of members in your personal phone directory.
number={}
# Funtion to add numbers of family and friends
def phone_number(name,phone_number):
    number[name]=phone_number

# Function to delete member
def delete_member(key):
    if key in number:
        del number[key]
    else:
        print("No such members found")


for i in range(12): # to take 12 inputs
    name=input("Enter name : ")
    phone=input("Enter phone number : ")
    phone_number(name,phone)

print("All numbers in my personal phone directory are")
for key,value in number.items():
    print(f"{key} : {value}")


# Deleting members
delete_member("Ali")
# 5. Design a list of guests with family members on your sister wedding. Each family members must be counted. Your parents have made a list of guests and you have made another list. At the end compare both the list and find the common guests which both of you have invited and count them once. The program will return the number of guest with members and total number of guest. Use functions to perform the required actions
count=0
parents_guest_list = [("Amir", 3), ("Ali", 2),( "Faizan", 4), ("Aslam", 2), ("Pappo", 1)]


my_guest_list = [("Faizan", 4),( "Akram", 2), ("Amir", 3), ("Imran", 4), ("Ayyub", 2)]

member_names=[]
# it will give number of members which are common
def number_of_members():
    global count
    for i in member_names:
        for j in range(len(my_guest_list)):
            if i in my_guest_list[j][0]:
                count+=my_guest_list[j][1]

# it will give the member names which are common
def member():
    for i in range(len(parents_guest_list)):
        for j in range(len(my_guest_list)):
            if parents_guest_list[i][0]==my_guest_list[j][0]:
                member_names.append(parents_guest_list[i][0])
    number_of_members()

member()

total=0

# it will cout the members from both the list which are not common
def total_members():
    global total
    for i in my_guest_list:
        if i[0] not in member_names:
            total+=i[1]
    for i in parents_guest_list:
        if i[0] not in member_names:
            total+=i[1]

total_members()


print(f"The names of members in both the list are {member_names}")
print(f"The total number of members in both the list and counting the duplicates one time are {total+count}") # members not common + members common to get all members one time only
print(f"The number of members which are common in both the list are {count}")
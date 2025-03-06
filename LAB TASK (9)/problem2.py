# 2.   Write a program which will remove 2 friends who left NED

friends = {"Ali", "Amir", "Ahmed", "Sarim", "Ahsan"}
print("Friends before leaving:", friends)
for i in range(2):
    name = input(f"Enter the name of friend {i + 1} who left: ")
    friends.discard(name)  # Remove the name if it exists in the set
print("Friends after leaving:", friends)
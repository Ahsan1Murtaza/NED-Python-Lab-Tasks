# 5. Generate a table from initial value to final, depending upon the user starting and ending range in  matrix form such as: 
# 1 2 3 4 5 
# 2 4 6 8 10 
# 3 6 9 12 15 
# 4 8 12 16 20 
# 5 10 15 20 25 
initial=int(input("Enter initial range : "))
final=int(input("Enter final range : "))
for i in range(initial,final+1):
    for j in range(initial,final+1):
         print(i*j,end=" ")
    print()
        
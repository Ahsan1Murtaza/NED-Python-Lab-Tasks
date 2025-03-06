# 4. Write a program in Python that holds an empty tuple and fill that tuple after taking user     input for names of provinces of Pakistan n fill an empty tuple and print.
tup=()
lis=list(tup)
print("PAKISTAN PROVINCES")
for i in range(4):
    province=input(f"Enter name of {i+1} province : ")
    lis.append(province)

tup=tuple(lis)
print(tup)
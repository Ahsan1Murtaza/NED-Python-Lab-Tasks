# 3.   Write a program which will add your best dishes and then pop one by one until the set is empty.
best_dishes=set()
n=int(input("Enter number of best dishes : "))
for i in range(n):
    dish=input("Enter dish name : ")
    best_dishes.add(dish)
print(f"Before popping : {best_dishes}")
for i in range(len(best_dishes)):
    best_dishes.pop()
print(f"After popping : {best_dishes}")
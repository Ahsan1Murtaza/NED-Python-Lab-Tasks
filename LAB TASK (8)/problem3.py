# 3.   Write function even() that takes a positive integer n as input and prints on the screen all numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
# >>> even(17)
# 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,

empty=[]
def even(number):
    for i in range(2,number+1):
        if i%2==0 or i%3==0:
            empty.append(i)
    for i in empty:
        print(f"{i}, ",end="")
even(17)


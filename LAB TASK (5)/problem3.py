#   Q.3      Write down a python program having one function for calculating factorial of a no. 
#               And call that function within a While loop to generate factorial of numbers from 0 to 10
def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n * facto(n-1)
i=0
while i<=10:
    print(f"{i}! = {facto(i)}")
    i+=1

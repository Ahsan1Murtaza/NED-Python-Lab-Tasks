# Program 5: Write a function f which takes one argument x, it will square the value of x and add 1 in it 
# then return the answer to user.
def f(x):
    return (x**2)+1
number=int(input("Enter number : "))
print(f"The square of {number} and 1 added in {number} is {f(number)}")
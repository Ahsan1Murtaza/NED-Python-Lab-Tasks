# 2. Calculate the arithmetic sequence of n numbers. The program will generate the nth term of the 
# sequence, whereas the user will enter the first term and the common difference. The program will 
# then ask either to continue or not, if the user will enter yes it will ask the next nth term to calculate. 
# Example: you have entered the first term as 3 and common difference 6 you are interesting in 35th 
# term. So it will calculate and generate the answer as 207. Now it will again ask for you to continue 
# if you agree it will ask next term like 45th or 96th term to calculate. 
while(True):
        a=int(input("Enter first term : "))
        d=int(input("Enter common difference : "))
        opt=input("Do you want to continue or not ? (yes or no)")
        if opt=="yes":
            n=int(input("Enter term number : "))
            tn=a+(n-1)*d
        elif opt=="no":
            print("Program is closed")
            break
        print("The",n,"th term is",tn)

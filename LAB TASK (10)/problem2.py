# 2. Implement function distribution() that takes as input the name of a file (as a string). This one-line file will contain letter grades separated by blanks. our function should print the distribution of grades

def distribution(filename):
    with open(filename,"r") as file:
        for line in file:
            x=line.split()

    for i in x:
        print(f"students got {i}")

distribution("example2.txt")
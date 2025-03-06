# 3. Implement function duplicate() that takes as input the name (a string) of a file in the .current directory and returns True if the file contains duplicate words and False otherwise


def duplicate(filename):
    s=set()
    with open(filename,"r") as file:
        words=file.read().strip().split()
        for word in words:
            if word in s:
                return True
            s.add(word)

    return False

result=duplicate("example3.txt")
print(result)
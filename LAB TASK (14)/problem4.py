#  Q.4 Design a python program to demonstrate IOError by using Try-Except Block
try:
    with open("not exist.txt","r") as f:
        data=f.read()
        print(data)
except IOError as e:
    print("No file found")
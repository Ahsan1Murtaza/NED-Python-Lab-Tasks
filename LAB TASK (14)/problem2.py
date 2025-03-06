# 1. EOF error jab hum input len or koi input na de matlab ctrl+z enter karde
try:
    text=input("Enter something")
    print(f"You have entered {text}")
except EOFError:
    print("No input was given")

# 2. EOFError with file reading
try:
    with open("file.txt","r") as f:
        data = f.read(100)  # Read more than available in file
        if not(data):
            raise EOFError("Unexpected end of file") # this will search for except block
except EOFError:
    print(EOFError)
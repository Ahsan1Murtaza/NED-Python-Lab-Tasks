# Program 11: Write a program which calculates the vowels from the given string.
phrase=input("Enter any phrase : ")
vowel=0
for i in phrase:
    if i==" ":
        continue
    elif i in "aeiou":
        vowel+=1
    else:
        continue
print("Total vowels in",phrase,"is",vowel)

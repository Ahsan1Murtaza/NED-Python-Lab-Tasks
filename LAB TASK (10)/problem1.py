# 1. Write a function stats() that takes one input argument: the name of a text file. The ;function should print, on the screen, the number of lines, words, and characters in the file .your function should open the file only once
def stats(filename):
    line_count=0
    word_count=0
    char_count=0
    vowel=0
    with open(filename,"r") as file:
        for line in file:
            line_count+=1
            word_count+=len(line.split())
            char_count+=len(line)
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")

stats("example1.txt")
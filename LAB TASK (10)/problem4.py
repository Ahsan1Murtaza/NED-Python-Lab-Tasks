# 4. The function abc() takes the name of a file (a string) as input. The function should open the file, read it, and then write it into file abc.txt with this modification: Every #  .'occurrence of a four-letter word in the file should be replaced with string 'xxxx #  abc('example.txt') >>> #  Note that this function produces no output, but it does create file abc.txt in the #  current folder
def abc(filename):
    with open(filename,"r") as file:
        data=file.read()
        words_list=data.split()
        for word in words_list:
            if len(word)==4:
                data=data.replace(word,"xxxx")
            with open("example4.txt","w") as f:
                f.write(data)

abc("sample.txt")
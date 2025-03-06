# 3. Write a function hexASCII() that prints the correspondence between the lowercase characters in the alphabet and the hexadecimal representation of their ASCII code. Note: [A format string and the format string method can be used to represent a number value in hex notation.]

def hexASCII():
    for  char in "abcdefghijklmnopqrstuvwxyz":
        ascii_value=ord(char)

        hex_value=hex(ascii_value)[2:] # SINCE HEX function gives 0x before string to represent hex decimal digits therefore string slicing
    
        # hex_value = format(ascii_value, 'x') # ANOTHER WAY

        print(f"{char} : {hex_value}",end="  ")

hexASCII()
# 5.   Translate each part into a Python statement using appropriate string methods:

# (a) Assign to variable message the string 'The secret of this message is that it is secret.' (b) Assign to variable length the length of string message, using operator len().
# (c) Assign to variable count the number of times the substring 'secret' appears in string message, using string method count().
# (d) Assign to variable censored a copy of string message with every occurrence of substring
# 'secret' replaced by 'xxxxxx', using string method replace(). 

message='The secret of this message is that it is secret.'
length=len(message)
count=message.count("secret")
censored=message.replace("secret","xxxxxx")

print(f"The message is {message}")
print(f"The length of message is {length}")
print(f"The number of times secret comes : {count}")
print(f"secret is replaced and now message is {censored}")
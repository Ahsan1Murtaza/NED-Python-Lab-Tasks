# 4.   Assume variables first, last, street, number, city, state, zipcode have already been assigned. Write a print statement that creates a mailing label:

# John Doe 
# 123 Main Street
# AnyCity, AS 09876 
# >>> first = 'John'
# >>> last = 'Doe'
# >>> street = 'Main Street'
# >>> number = 123
# >>> city = 'AnyCity'
# >>> state = 'AS'
# >>> zipcode = '09876'

first="John"
last="Doe"
street="Main Street"
number=123
city="AnyCity"
state="AS"
zipcode="09876"

print("{}\n{} {}\n{}, {} {}".format(first,number,street,city,state,zipcode))
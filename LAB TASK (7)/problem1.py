# 1.	Use  inbuilt min and max functions to perform the task of getting the minimum and maximum value of  in a list of tuples for a particular element position in a tuple.
# Sample  = [(2, 3), (4, 7), (8, 11), (3, 6)]

Sample  = [(2, 3), (4, 7), (8, 11), (3, 6)]

# FOR FIRST ELEMENTS 
first_elements=[t[0] for t in Sample]
print(f"The minimum value in first elements of tuple is {min(first_elements)}")
print(f"The maximum value in first elements of tuple is {max(first_elements)}")

# FOR SECOND ELEMENTS
second_elements=[t[1] for t in Sample]
print(f"The minimum value in second elements of tuple is {min(second_elements)}")
print(f"The maximum value in second elements of tuple is {max(second_elements)}")

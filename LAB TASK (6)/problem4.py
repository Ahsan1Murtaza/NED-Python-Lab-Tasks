# 4.   Start by assigning to variables monthsL and monthsT a list and a tuple, respectively, 
# both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order. Then attempt the 
# following with both containers: 
# (a)Insert string 'Apr' between 'Mar' and 'May'. 
# (b)Append string 'Jun'. 
# # (c)Pop the container.
# (d)Remove the second item in the container. 
# (e)Reverse the order of items in the container
monthsL=["Jan","Feb","Mar","May"]
monthsT=("Jan","Feb","Mar","May")

monthsL.insert(3,"Apr")
print(monthsL)
monthsL.append("Jun")
print(monthsL)
monthsL.pop()
print(monthsL)
del monthsL[1] # we can also use pop(1)
print(monthsL)
monthsL.reverse()
print(monthsL)
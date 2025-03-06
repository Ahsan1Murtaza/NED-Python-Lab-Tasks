# 5. Start by assigning to variables monthsL and monthsT a list and a tuple, respectively, both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order. Then attempt the following with both containers:
# (a)Insert string 'Apr' between 'Mar' and 'May'.
# (b)Append string 'Jun'.
# (c)Pop the container.
# (d)Remove the second item in the container. 
# (e)Reverse the order of items in the container.
# Note: when attempting these on tuple monthsT you should expect errors. 

monthsL=["Jan","Feb","Mar","May"]
monthsT=("Jan","Feb","Mar","May")

monthsL.insert(3,"Apr")
monthsL.append("Jun")
monthsL.pop()
monthsL.remove("Feb")
monthsL.reverse()
print(monthsL)


"ERROR WILL COME HERE"
# monthsT.insert(3,"Apr")
# monthsT.append("Jun")
# monthsT.pop()
# monthsT.remove("Feb")
# monthsT.reverse()
# print(monthsT)


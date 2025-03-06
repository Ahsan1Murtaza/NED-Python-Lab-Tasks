# Program 2: Using the following interactive session as an aid, explain in your own words what 
# the list methods extend(), copy(), and clear() do. 
lst = [2, 3, 4] 
lst.extend([5, 6]) 
print(lst) 
# [2, 3, 4, 5, 6]
lst2 = lst.copy() 
print(lst2 )
# [2, 3, 4, 5, 6] 
lst.clear() 
print(lst)
# []
print(lst2)
# [2,3,4,5,6]
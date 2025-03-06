# 1. Take a sample list [2, 1, 3, 5, 4, 3, 8] 
# Apply del(), remove(), sort(), insert(), pop(), extend()…) 

list1=[2,1,3,5,4,3,8]
print(list1)
list1.remove(3) # remove element 3 of first occurence
print(list1)
list1.sort() # sort the list
print(list1)
list1.insert(0,3)  # (index,element)
print(list1)
list1.pop() # remove last element
print(list1)
del(list1) # will del list1

list1=[2,1,3,5,4,3,8]
list2=[5,4,3,6,4]
list2.extend(list1) # list 2 wil open ans then list1 will add in it
print(list2)
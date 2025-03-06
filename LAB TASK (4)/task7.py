# Program 7: Write a program which will check the data type of given data in a loop. 
# Code: 
datalist = [300, 12.65, 5+6j, True, 'Faisal', (5, -7), [8, 52],{"color":'blue', "color":'red'}] 
for item in datalist: 
  print ("Type of ",item, " is ", type(item))
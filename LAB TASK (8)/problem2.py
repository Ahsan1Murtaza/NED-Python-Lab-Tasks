# 2.   Assuming that variable forecast has been assigned string 'It will be a sunny day today' Write Python statements corresponding to these assignments:

# (a) To variable count, the number of occurrences of string 'day' in string forecast. (b) To variable weather, the index where substring 'sunny' starts.
# (c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.

forecast="It will be a sunny day today"

# a)
count=forecast.count("day")

# b)
weather=forecast.find("sunny")

# c)
change=forecast.replace("sunny","cloudy")

print("Count of 'day':", count)
print("Index of 'sunny':", weather)
print("Replaced string:", change)
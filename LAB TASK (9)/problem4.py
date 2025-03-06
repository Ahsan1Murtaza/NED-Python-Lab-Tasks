# 4.Write a program which will store number of items in a set after each purchasing the items will be pop from the set and compare its price at the end program will give you the total amount of items have been sold. Also find the max amount  and minimum amount of items sold.
items_price_list=[300,75,100,200,250,450]
total_price=0
sold_items_price=[]

while items_price_list:
    price=items_price_list.pop()
    total_price+=price # solded items price will be added in total
    sold_items_price.append(price) # solded item ko store kar lia ta k max or min bata sakhen

max_amount=max(sold_items_price)
min_amount=min(sold_items_price)

print("Total amount of items sold:", total_price)
print("Maximum amount of a single item sold:", max_amount)
print("Minimum amount of a single item sold:", min_amount)
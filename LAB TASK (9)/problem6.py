# 6.   A pet store keeps track of the purchases of customers over a four-hour period. The store manager classifies purchases as containing a dog product, a cat product, a fish product, or product  for a different kind of pet. She found.
# a.   83 purchased a dog product 
# b.   101 purchased a cat product 
# c.   22 purchased a fish product
# d.   31 purchased a dog and a cat product 
# e.   8 purchased a dog and a fish product
# f.    10 purchased a cat and a fish product
# g.   6 purchased a dog, a cat and a fish product
# h.   34 purchased a product for a pet other than a dog, cat or a fish.
# i.   How many purchases were for a dog product only?
# ii.  How many purchases were for cat product only? 
# iii. How many purchases for a dog or a fish product? 
# iv.  How many purchases were there in total?
# Given values
D = 83  # purchases with dog product
C = 101  # purchases with cat product
F = 22  # purchases with fish product
D_and_C = 31  # purchases with both dog and cat product
D_and_F = 8  # purchases with both dog and fish product
C_and_F = 10  # purchases with both cat and fish product
D_and_C_and_F = 6  # purchases with dog, cat, and fish product
O = 34  # purchases with other pet product


# i. How many purchases were for a dog product only?
D_only = D - D_and_C - D_and_F + D_and_C_and_F

# ii. How many purchases were for a cat product only?
C_only = C - D_and_C - C_and_F + D_and_C_and_F

# iii. How many purchases were for a dog or a fish product?
D_or_F = D + F - D_and_F

# iv. How many purchases were there in total?
total_purchases = D + C + F - D_and_C - D_and_F - C_and_F + D_and_C_and_F + O


print("i. Purchases for a dog product only:", D_only)
print("ii. Purchases for a cat product only:", C_only)
print("iii. Purchases for a dog or a fish product:", D_or_F)
print("iv. Total number of purchases:", total_purchases)

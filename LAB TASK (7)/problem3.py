# 3.   Write Python expressions corresponding to these statements:
# (a)The number of characters in the word "anachronistically" is 1 more than the number of characters in the word "counterintuitive."
# (b)The word "misinterpretation" appears earlier in the dictionary than the word "misrep- resentation."
# (c)The letter "e" does not appear in the word "ﬂoccinaucinihilipiliﬁcation."
# (d)The number of characters in the word "counterrevolution" is equal to the sum of the number of characters in words "counter" and "resolution."

"a"
print(len("anachronistically")==len("counterintuitive")+1)

"b"
print("misinterpretation" < "misrepresentation")

"c"
print("e" not in "ﬂoccinaucinihilipiliﬁcation")

"d"
len("counterrevolution")==len("counter")+len("resolution")
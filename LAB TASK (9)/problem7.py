# 7.    Solve the following problem of real world.
# A camp of international students has 110 students, as shown in the diagram. The diagram will elaborate that all the students speak some kind of a language. We need to find out how many that speak none of them out of 110 students.
# Find how many students speak
# a.    English and Spanish but not French?
# b.    Neither English, Spanish, nor French?
# c.    French, but neither English nor Spanish?
# d.    Only one of the three languages?
# e.    Exactly two of the three languages?
 
# As a programmer your task is to verify that above Venn diagram is correctly filled.

# Given values (adjust based on the Venn diagram)
total_students = 110
only_english = 30  
only_spanish = 40  
only_french = 20  
english_spanish = 10  # Students speaking both English and Spanish, but not French
english_french = 5    # Students speaking both English and French, but not Spanish
spanish_french = 8    # Students speaking both Spanish and French, but not English
all_three = 3         # Students speaking English, Spanish, and French

# a. English and Spanish but not French
english_and_spanish_not_french = english_spanish

# b. Neither English, Spanish, nor French
neither_language = total_students - (only_english + only_spanish + only_french + english_spanish + english_french + spanish_french + all_three)

# c. French, but neither English nor Spanish
french_not_english_spanish = only_french + english_french + spanish_french - all_three

# d. Only one of the three languages
only_one_language = only_english + only_spanish + only_french

# e. Exactly two of the three languages
exactly_two_languages = english_spanish + english_french + spanish_french - 3 * all_three

# Output the results
print("a. English and Spanish but not French:", english_and_spanish_not_french)
print("b. Neither English, Spanish, nor French:", neither_language)
print("c. French, but neither English nor Spanish:", french_not_english_spanish)
print("d. Only one of the three languages:", only_one_language)
print("e. Exactly two of the three languages:", exactly_two_languages)

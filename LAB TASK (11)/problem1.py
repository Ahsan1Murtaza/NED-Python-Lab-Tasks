# 1. Design a dictionary of your family. Once you get the printout update family dictionary with your grandparents (maternal and paternal) including uncles and aunts (maternal and paternal).

family={"Father":"Murtaza","Mother":"Asma","Brother":"Aneeq","Sister":"Mariam","Me":"Ahsan"}
print("My family Tree is")
for key,value in family.items():
    print(f"{key} : {value}")

family["Nana"]="Afzal"
family["Nani"]="Bilqees"
family["Dada"]="Ashraf"
family["Dadi"]="Shameem"

print(f"My family Tree with grand parents and uncles and aunts is")
for key,value in family.items():
    print(f"{key} : {value}")



# 4. Create double dictionaries one of which is your choice of dishes. Other one is dishes cooked in a week. Compare them and find how many dishes you will get of your choice to be cooked in next week. Print the name of those dishes as well.
choice_dishes={1:"Palak",2:"Shawarma",3:"Mandi",4:"Biryani",5:"Sabzi",6:"Gosht",7:"Handi"}
dishes_cooked={1:"Pulao",2:"Biryani",3:"Mandi",4:"Bhindi",5:"Aloo",6:"Tinda",7:"Chinese"}

food=[]
for i in choice_dishes.values():
    if i in dishes_cooked.values():
            food.append(i)

if food:
      print("Your favourite dishes to be cooked in  next week")
      for i in food:
            print(i)
else:
      print("No favourite dish wwill be cooked of yours")
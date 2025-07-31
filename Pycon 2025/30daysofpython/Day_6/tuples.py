empty_tuple=()

#create tuple of brothers and sisters
brothers= ('Naruto', 'Sasuke', 'Boruto')
sisters= ('Hinata', 'Sakura', 'Ino', 'Stella')

#sum the tuples of brother and sister
siblings= brothers + sisters
print("All siblings : ", siblings)

#Number of siblings
print( "There are ", len(siblings), " siblings\n")

#adding father and mother
family_members = siblings + ('Minato','')
print("Family members: ", family_members, "\n")

##Level 2
#Unpacking
siblings = family_members[:-2]
parents= family_members[-2:]
print("Siblings:", siblings, "\n")
print("Parents: ", parents, "\n")

#tuples of fruits , vegetables and animal
fruits= ('Mango', 'Apple', 'Water Melon', 'Orange')
vegetables= ('Tomato', 'Cabbage', 'carrot')
animal= ('Lion', 'Eagle', 'Dog', 'Cat', 'Python')
print("Fruits: ", fruits, "\nVegetables: ", vegetables, "\nAnimals: ", animal, "\n")

#joining the the tuples
food_stuff_tp= fruits + vegetables + animal
print("Food Stuff: ", food_stuff_tp, "\n")

#changing the tuple to a list
food_stuff_lt= list(food_stuff_tp)
print("List: ", food_stuff_lt, "\n")

#slicing the middle item
mid_it= int(len(food_stuff_tp)/2)
print(food_stuff_tp[mid_it],"\n")

#Slicing the first three items and the last thre items
print("The first three items: ", food_stuff_lt[0:3], "\n")
print("The last three items: ", food_stuff_lt[-3:], "\n")

#deleting the tuple
del food_stuff_tp

#checking if an item exist
nordic_countries= ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia is a nordic country?: ", 'Estonia' in nordic_countries)
print("Iceland is a nordic country?: ", 'Iceland' in nordic_countries)


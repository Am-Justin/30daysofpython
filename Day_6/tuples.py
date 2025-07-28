# Exercises: Level 1

tpl = ()
sisters = ("lea", "deynah", "daniella")
brothers = ("jonh", "peter")
siblings = sisters + brothers
print(len(siblings))

siblings =list(siblings)
siblings.append("mum")
siblings.append("father")
siblings = tuple(siblings)
print(siblings)

# Exercice level 2

# 1. Unpack siblings and parents from family_members
siblings = list(siblings)
sisters, brothers, parents = siblings[0:3], siblings[3:5], siblings[5:]
sisters = tuple(sisters)
brothers = tuple(brothers)
parents = tuple(parents)
print(sisters)
print(brothers)

print(parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and
# assign it to a variable called food_stuff_tp.
fruits = ("mango", "orange", "apple")
vegetables = ("potato", "Beetroot", "tomato")
products = ("milk", "meat")

food_stuff_tp = fruits + vegetables + products
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt
# list.
length = len(food_stuff_lt)
if length % 2 == 0:
    mid1 = length // 2 - 1
    mid2 = length // 2
    food_stuff_lt.pop(mid2)
    food_stuff_lt.pop(mid1)
else:
    middle_index = length // 2
    food_stuff_lt.pop(middle_index)

print(food_stuff_lt)

# 5. Slice out the first three items and the last three items from food_staff_lt list
del food_stuff_lt[:3]

print(food_stuff_lt)
# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
#  Check if 'Estonia' is a nordic country
#  Check if 'Iceland' is a nordic country

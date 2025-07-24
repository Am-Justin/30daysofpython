# 1. Check the data type of all your variables using type() built-in function
# Exemple des de chaque different type de données
a = 12; 
b = 1.2; 
c = [1,2,3]; 
d = {"test":"ok", "day":"first"}
e = True
f = ("one", "two", "three")
g = {1,2,3}
h = 1 + 4j
i = "hello world"

liste = [a, b, c, d, e, f, g, h, i]
for i, var in enumerate(liste):
    print(f"le type de {var} est {type(liste[i])}")


# 2. Using the len() built-in function, find the length of your first name
first_name = "DOE"
last_name = "JOHN PETER"
first_name_len = len(first_name)
last_name_len = len(last_name)


# 3. Compare the length of your first name and your last name
print(f"le mot le plus long entre le nom et le prenom a { max(first_name_len, last_name_len)}")

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4


# 5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(f"le total est : {total}")

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(f"la difference est : {diff}")

# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(f"le produit est {product}")

# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(f"la division est : {division}")

# 9. Use modulus division to find num_two divided by num_one and assign the value to a
# variable remainder
remainder = num_one % num_two
print(f"le reste est : {remainder}")

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(f"l'expo est : {exp}")

# 11. Find floor division of num_one by num_two and assign the value to a variable
# floor_division
floor_division = num_one // num_two
print(f"le quotient est : {floor_division}")
# 12. The radius of a circle is 30 meters.
# i. Calculate the area of a circle and assign the value to a variable name
# of area_of_circle
raduis = 30
area_of_circle = 3.14* raduis**raduis
print("l'aire du cercle est :", area_of_circle)
# ii. Calculate the circumference of a circle and assign the value to a variable name
# of circum_of_circle
circum_of_circle = 2*3.14*raduis
print("la circonference du cercle est :", circum_of_circle)
# iii. Take radius as user input and calculate the area.
raduis = int(input("Quel est le rayon du cercle ? "))
print(f"l'aire du cercle est {3.14* raduis**raduis} et la circonference est {2*3.14*raduis}")


# 13. Use the built-in input function to get first name, last name, country and age from a user
# and store the value to their corresponding variable names
first_name = input("Quel est votre nom de famille ?")
last_name = input("Quel est votre prenom ?")
country = input("Vous venez de quel pays ?")
age = input("Vous avez quel âge ?")

print(f"je m'appelle {first_name} {last_name}, je viens du {country} et j'ai {age}ans")


# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved
# words or keywords
""" 
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not 

"""

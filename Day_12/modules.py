# 💻 Exercises: Day 12
# Exercises: Level 1
import string
import random
def random_user_id():
    random_chr = string.ascii_letters + string.digits
    random_id = "".join(random.choices(random_chr, k=6))
    return random_id
print(random_user_id())


def user_id_gen_by_user():
    length = int(input("La longueur du code a généré : "))
    number = int(input("le nombre code a généré : "))
    random_chr = string.ascii_letters + string.digits
    id_gen = []
    for _ in range(number):
        id_gen.append("".join(random.choices(random_chr, k=length))) 

    return "\n".join(id_gen)
# print(user_id_gen_by_user())

def rgb_color_gen():
    first = random.randint(0,255)
    second = random.randint(0,255)
    third = random.randint(0,255)
    return f"rgb({first},{second},{third})"
print(rgb_color_gen())

# Exercises: Level 2

def list_of_hexa_colors(nbre):
    liste = []
    for _ in range(nbre):
        random_chr = string.digits + "abcdef"
        random_color = "".join(random.choices(random_chr,k=6))
        liste.append(f"#{random_color}")
    return liste
print("list of hexa colors ",list_of_hexa_colors(4))

def list_of_rgb_colors(nbre):
    liste = []
    for _ in range(nbre):
        first = random.randint(0,255)
        second = random.randint(0,255)
        third = random.randint(0,255)

        liste.append(f"rgb({first},{second},{third})")

    return liste

print("list of rgb colors ",list_of_rgb_colors(5))

def generate_colors(type, nbre):
    liste = []
    if type == "hexa":
        return list_of_hexa_colors(nbre)
        
    
    if type == "rgb":
       return list_of_rgb_colors(nbre)

print("list of rgb or hexa colors ",generate_colors("hexa", 2))


# Exercises: Level 3

def shuffle_list(liste):
    liste2 = []
    length = len(liste)
    random_list = random.sample(range(0, length), length)

    for elt in random_list:
        liste2.append(liste[int(elt)])
    return liste2

print("shuffle_list ",shuffle_list([1,2,3,4,5]))

def all_unique():
    liste = []
    a = True
    while len(liste) < 7:
        b = random.randint(0,9)
        if b not in liste:
            liste.append(b)
    return liste

print("an array of seven random numbers in a rangeof 0-9 ",all_unique())

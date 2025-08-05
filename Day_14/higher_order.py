# 💻 Exercises: Day 14

import sys
import os

# Ajouter le chemin du dossier parent pour atteindre dossier_a
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark',
'Norway', 'Iceland']

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.

# map : applique une fonction à chaque élément.
# filter : garde les éléments selon une condition.
# reduce : réduit une liste à une seule valeur cumulée.

# 2.

# Higher order function : prend une fonction en argument ou retourne une fonction.
# Closure : fonction interne qui se souvient des variables de son scope externe.
# Decorator : fonction qui modifie le comportement d’une autre fonction.

# 3. 
def square(x): 
    return x * x
print(list(map(square, numbers)))


print(list(filter(lambda x: x % 2 == 0, numbers)))

from functools import reduce

print(reduce(lambda x, y: x + y, numbers))

# 4.
for country in countries:
    print(country)

# 5. 
for name in names:
    print(name)

# 6. 
for number in numbers:
    print(number)


# Exercises: Level 3
from Day_10.countries_data import countries_data

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-
# Python/blob/master/data/countries-data.py) file and follow the tasks below:
# o Sort countries by name, by capital, by population
sorted(countries_data, key=lambda x:x["name"])
sorted(countries_data, key=lambda x:x["capital"])
sorted(countries_data, key=lambda x:x["population"])

# o Sort out the ten most spoken languages by location.
freq_lang = {}
for country in countries_data:
    for lang in country["languages"]:
        if lang in freq_lang:
            freq_lang[lang] += 1
        else:
            freq_lang[lang] = 1
        print(lang)

print(sorted(freq_lang.items(), key=lambda x:x[1],reverse=True)[:10])

# o Sort out the ten most populated countries.
# print(sorted(countries_data, key=lambda x:x["population"],reverse=True)[:10])


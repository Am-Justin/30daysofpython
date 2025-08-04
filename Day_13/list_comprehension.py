# Exercices: Jour 13
# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if n <= 0]
print(filtered)

# 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened) 

# 3
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened = [[country.upper(), country[:3].upper(), city.upper()] 
             for group in countries 
             for (country, city) in group]

print(flattened)

# 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': country.upper(), 'city': city.upper()} 
             for group in countries 
             for (country, city) in group]

print(dict_list)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f"{first} {last}" 
              for group in names 
              for (first, last) in group]

print(full_names)

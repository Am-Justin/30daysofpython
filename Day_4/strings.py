# 1
a = 'Days' 
b = 'Of' 
c = 'Python'
print(f"{a} {b} {c}")

# 2
a = 'Coding', 
b = 'For', 
c = 'All'
print(f"{a} {b} {c}")

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company.split(" ")[0])

# 10
print(company.find("Codind"))

# 11
print(company.replace("Coding", "Python"))

# 12
print("Python for Everyone".replace("Everyone", "All"))

# 13
print(company.split(" "))

# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# 15
print(company[1])

# 16
print(company[-1])

# 17
print(company[10])

# 18
a=""
for chr in 'Python For Everyone':
    if chr.isupper():
        a+=chr
print(a)

# 19
a = ""
for chr in 'Coding For All':
    if chr.isupper():
        a+=chr
print(a)

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
print("Coding For All People".rfind('l'))

# 23
print("You cannot end a sentence with because because because is a conjunction".find("because"))

# 24
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

# 25
print("You cannot end a sentence with because because because is a conjunction".split("because because because"))

# 26
print("You cannot end a sentence with because because because is a conjunction".find("because"))

# 27
print("You cannot end a sentence with because because because is a conjunction".split("because because because"))

# 28
print("Coding For All".startswith("Coding"))

# 29
print("Coding For All".endswith("coding"))

# 30
print(" Coding For All ".strip())

# 31
print("30DaysOfPython".isidentifier())
print(" thirty_days_of_python".isidentifier())

# 32
print(" ".join(['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name    \tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36
print(f"8 + 6 = {8+6}")
print(f"8 - 6 = {8-6}")
print(f"8 * 6 = {8*6}")
print(f"8 / 6 = {8/6}")
print(f"8 % 6 = {8%6}")
print(f"8 // 6 = {8//6}")
print(f"8 ** 6 = {8**6}")



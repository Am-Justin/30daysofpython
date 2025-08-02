# 💻 Exercises: Day 11
# Exercises: Level 1

import math


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

def calcul_area(r):
    area = r*r*3.14
    return area

def add_all_nums(*num):
    if type(num) is not int:
        return None
    total += num
    return total


# Exercises: Level 2
def evens_and_odds(num):
    a,b = 0, 0
    for i in range(num + 1):
        if i % 2 == 0:
            a+=1
        else:
            b += 1
    print(f"The number of odds are {a}.")
    print(f"The number of even are {b}.")
print(evens_and_odds(100))


# 1. Call your function factorial, it takes a whole number as a parameter and it
# return a factorial of the number

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(6))

# 2. Call your function is_empty, it takes a parameter and it checks if it is empty or
# not
def is_empty(param):
    if len(str(param))==0:
        print("The parameter is empty")
    else:
        print("The parameter is not empty")

is_empty([1,4])


# 3
# calculate_mean
def calculate_mean(liste):
    total = 0
    for elt in liste:
        total += int(elt)
        moy = total / len(liste)
    return moy

print(calculate_mean([1,2,3,4,5]))

# calculate_median
def calculate_median(liste):
    if len(liste)%2==1:
        med = liste[len(liste)//2]
    else:
        med = (liste[len(liste)//2] + liste[(len(liste)//2)-1])/2
    
    return med

print(calculate_median([1,2,2,3]))

# calculate_mode
def calculate_mode(liste):
    freq = {}
    for elt in liste:
        if elt in freq:
            freq[elt]+=1
        else:
            freq[elt]=1
    a = sorted(freq.items(), key=lambda x:x[1], reverse=True)[:1]

    for elt, nbre in a:
        return f"le mode est {elt}, car il revient {nbre} fois"
    return a

print(calculate_mode([1, 2, 1, 1]))

# calculate_range
def calculate_range(liste):
    _range = max(liste) - min(liste)
    return _range

print(calculate_range([1, 2, 1, 1]))

# calculate_variance
def calculate_variance(liste):
    liste2 = []
    for elt in liste:
        liste2.append(elt - calculate_mean(liste))
    liste3 = []
    for elt in liste2:
        liste3.append(elt**2)
    
    total = 0
    for elt in liste3:
        total+=elt
    variance = total/(len(liste3)-1)

    return variance

print(calculate_variance([1,2,3,4,5]))

# calculate_std (standard deviation
def calculate_std(liste):
    std = math.sqrt(calculate_variance(liste))
    return std

print(calculate_std([1,2,3,4,5]))


# Exercises: Level 3

def is_prime(nbre):
    if nbre // 1 == 0 and nbre // nbre == 0:
        return True
    else:
        return False

print(f"Is prime ? {is_prime(2)}")

def all_unique(liste):
    a = []
    for elt in liste:
        a.append(elt)
        if elt in a:
            return False
        else: 
            return True
        

print(all_unique([1,3,5,4]))
# 2. Write a functions which checks if all items are unique in the list.

# Copyright © 2025 Skill Foundry
# 3. Write a function which checks if all the items of the list are of the same data
# type.
# 4. Write a function which check if provided variable is a valid python variable
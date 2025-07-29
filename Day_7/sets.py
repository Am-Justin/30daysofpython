# Exercises: Level 2

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1. Join A and B
print(A.union(B))

# 2. Find A intersection B
print(A.intersection(B))

# 3. Is A subset of B
print("Is A subset of B ?", B.issubset(B) )

# 4. Are A and B disjoint sets
print("Are A and B disjoint sets ?", A.isdisjoint(B))

# 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))

# 6. What is the symmetric difference between A and B
print("the symmetric difference between A and B", A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B
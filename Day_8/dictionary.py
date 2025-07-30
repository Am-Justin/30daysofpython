# Exercises: Day 8
dog = {}
dog["name"] = "rock"
dog["color"] = "black"
dog["breed"] = "boerbull"
dog["legs"] = 4
dog["age"] = 2

print(dog)

student = {
    'first_name':'Sarah',
    'last_name':'Lucky',
    'gender': 'female',
    'age':25,
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB',
    'Python'],
    'country':'Togo',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}

print(len(student))
print(type(student['skills']))
student['skills'].extend(['java', 'flutter'])

print(student.keys())
print(student.values())
print(student.items())

student.pop('address')
print(student)

del student

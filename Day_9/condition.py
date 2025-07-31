# Exercices: niveau 3
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 25,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB',
    'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
    }
}

# * Vérifiez si le dictionnaire de la personne a des compétences, si c'est le cas, imprimez les co
# mpétences intermédiaires dans la liste des compétences.
if person['skills']:
    print(person['skills'])

# * Vérifiez si le dictionnaire de la personne a une clé de compétences, si c'est le cas, vérifiez si
# la personne a des compétences «Python» et imprimez le résultat.
if person['skills']:
    if 'python' in person['skills']:
        print("La personne a des competences en Python")
    else:
        print("La personne n'a pas des competences en Python")


if person['skills']:
    if     all( competences in person['skills'] for competences in ['Node', 'Python', 'MongoDB', 'React', 'JavaScript']):
        print("Il est developpeur fullstack")
    elif     all( competences in person['skills'] for competences in ['Node', 'Python', 'MongoDB']):
        print("Il est developpeur backend")
    elif      all( competences in person['skills'] for competences in ['React', 'JavaScript']):
        print("Il est un développeur frontend")

    else:
        print("INCONNET TITME")


if person['is_marred'] == True:
    print(f"{person['last_name']} {person['first_name']} vit en {person['country']}. il est marié")
else:
    print(f"{person['last_name']} {person['first_name']} vit en {person['country']}. il est celibataire")

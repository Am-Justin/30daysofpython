# Exercices: niveau 3
personne = {'first_name': 'asabeneh', 'last_name': 'yetayeh', 'age': 25, 'country': 'Finland', 'is_marred': True, 'compétences': ['JavaScript', 'React','Node'], 'Zipcode': '02210'}

# * Vérifiez si le dictionnaire de la personne a des compétences, si c'est le cas, imprimez les co
# mpétences intermédiaires dans la liste des compétences.
if personne['compétences']:
    print(personne['compétences'])

# * Vérifiez si le dictionnaire de la personne a une clé de compétences, si c'est le cas, vérifiez si
# la personne a des compétences «Python» et imprimez le résultat.
if personne['compétences']:
    if 'python' in personne['compétences']:
        print("La personne a des competences en Python")
    else:
        print("La personne n'a pas des competences en Python")


if personne['compétences']:
    if     all( competences in personne['compétences'] for competences in ['Node', 'Python', 'MongoDB', 'React', 'JavaScript']):
        print("Il est developpeur fullstack")
    elif     all( competences in personne['compétences'] for competences in ['Node', 'Python', 'MongoDB']):
        print("Il est developpeur backend")
    elif      all( competences in personne['compétences'] for competences in ['React', 'JavaScript']):
        print("Il est un développeur frontend")

    else:
        print("INCONNET TITME")


if personne['is_marred'] == True:
    print(f"{personne['last_name']} {personne['first_name']} vit en {personne['country']}. il est marié")
else:
    print(f"{personne['last_name']} {personne['first_name']} vit en {personne['country']}. il est celibataire")

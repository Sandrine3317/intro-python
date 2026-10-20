# Faire un programme, qui recupère l'année de naissance d'un utilisateur et son prenom. 
# faites un print dynamique avec la phrase :
# "bonjour PRENOM, vous avez aujourdhui AGE"

#je récupère l'année de naissance (avec la fonction input)
#ensuite je transforme la réponse qui est du texte en nombre entier avec la fonction int
birthday = int(input("votre année de naissance ?"))

name = input("votre prénom?")

# variable qui contient l'année en cours
years = 2026

#calcul de l'ager de l'utilisateur, année actuelle moins sont les année de naissance
userAge = years - birthday

print(f"Bonjour {name}, vous avez {userAge} ans")

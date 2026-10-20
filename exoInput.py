# Faire un programme, qui recupère l'année de naissance d'un utilisateur et son prenom. 
# faites un print dynamique avec la phrase :
# "bonjour PRENOM, vous avez aujourdhui AGE"

prenom = input("Comment tu t'appelles?")
print(prenom)
annee= input("Donne moi ton année de naissance")
print(annee)
print(f"bonjour {prenom}, tu as aujourd'hui {2026-int(annee)}")
# exo 1 faire une phrase dynamique avec des données changeantes
# "je suis PRENOM, j'habite à VILLE et j'ai AGE ans"
# prenom, ville et age seront dans des variables
prenom = "Winnie"
ville = "Paris"
age = 25
print(f"Je suis {prenom}, j'habite à {ville} et j'ai {age} ans.")

# Exo 2
# Print une phrase le total est de TOTAL euros
# vous avez acheté une baguette et un croissant
# le montant de ces articles sont dans des variables
baguette = 1.20
croissant = 0.80
total = baguette + croissant
print(f"Le total est de {total} euros.")
print(f"Vous avez acheté une baguette à {baguette} euros et un croissant à {croissant} euros.")

# Exo3 
# Lors d'un jeu vous avez dix points
# Faire un print de vos points 
# Au premier tour vous perdez 1 pts
# au deuxieme tour vous en gagnez 5
# au dernier tour vous en perdez la moitié
# faire un print de votre nouveau total de points a chaque tours
points = 20
print(f"j'ai {points} points.")
points = points - 1
print(f"Au premier tour, je perds 1 point. J'ai maintenant {points} points.")
points = points + 5
print(f"Au deuxième tour, je gagne 5 points. J'ai maintenant {points} points.")
points = points / 2
print(f"Au dernier tour, je perds la moitié de mes points. J'ai maintenant {points} points.")
print(f"Mon nouveau total de points est de {points}")

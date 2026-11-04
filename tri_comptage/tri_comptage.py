tableau = [3, 5, 2, 2, 0, 1, 4, 4, 5]
maximum = max(tableau)
resultat = []

compteur = [0] * (maximum + 1)
for number in tableau:
    compteur[number] += 1

for i in range(len(compteur)):
    resultat += [i] * compteur[i]

print("Avant :", tableau)
print("Après :", resultat)

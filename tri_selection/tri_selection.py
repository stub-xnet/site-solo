tableau = [5, -3, 1, 8, 2, 1, 4, 9, -2]
resultat = tableau.copy()

for i in range(len(resultat)):
    indice_min = i
    for j in range(i + 1, len(resultat)):
        if resultat[j] < resultat[indice_min]:
            indice_min = j
    resultat[i], resultat[indice_min] = resultat[indice_min], resultat[i]

print("Avant :", tableau)
print("Après :", resultat)

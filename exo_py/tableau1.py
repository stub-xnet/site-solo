def tableau(ma_liste):
    if len(ma_liste) <= 1:
        return True
        
    for i in range(len(ma_liste) - 1):
        # Si l'élément suivant n'est pas strictement supérieur, ce n'est pas croissant
        if ma_liste[i+1] <= ma_liste[i]:
            return False
            
    return True

tab = [3, 2, 4, 9]
print(tableau(tab))

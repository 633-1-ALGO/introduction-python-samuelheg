# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Affichage du tableau mis à jour
def frequencelettres(tab):
    for lettre in tab[0]:
        compte = texte.count(lettre)
        tab[1][tab[0].index(lettre)] = compte
    return tab


print(frequencelettres(tab_lettres))

# Affichage lettre par lettre
def frequencelettres(tab):
    for lettre in tab[0]:
        compte = texte.count(lettre)
        tab[1][tab[0].index(lettre)] = compte
        print("le caractère ", lettre, "apparaît ", compte, " fois.")


frequencelettres(tab_lettres)

# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]
B2 = [2, 6, 8, 5, 4, 12, 98, 34, 1]


# Avec fonction --> source: https://www.science-emergence.com/Articles/Ordonner-une-liste-de-nombres-par-ordre-croissant-ou-d%C3%A9croissant-avec-python/
def triersort(liste):
    liste.sort()
    return liste


print(triersort(B))


# Manuellement
def trier(liste):
    cpt = 0
    prev = liste[0]
    for n in liste:
        if (n < prev):
            liste[liste.index(n)] = prev
            liste[liste.index(prev)] = n
            trier(liste)
        prev = n
    return liste


print(trier(B2))

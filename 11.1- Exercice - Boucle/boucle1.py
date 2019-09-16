# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]


def calculermoyenne(liste):
    somme = 0
    cpt = 0
    for n in liste:
        somme = somme + n
        cpt+=1
    moyenne = somme/cpt
    return moyenne


print(calculermoyenne(A))

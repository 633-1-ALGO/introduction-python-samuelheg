# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]


def searchmaxintab(table):
    m = 0
    for t in table:
        for n in t:
            if n > m:
                m = n
    return m

def searchtabwithmax(table,m):
    for t in table:
       if m in t:
           print("la valeur maximum est: ", m, " et elle se trouve à l'indice [",table.index(t),"][", t.index(m),"]")


searchtabwithmax(tab, searchmaxintab(tab))

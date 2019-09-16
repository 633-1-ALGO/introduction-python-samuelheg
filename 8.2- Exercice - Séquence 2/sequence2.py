# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75
tva = prix_ht*7.7/100
prix_at = prix_ht + tva
prix_tot = nb_articles * prix_at

print("le prix total sans tva est de : ", str(nb_articles*prix_ht))
print("le prix total avec tva est de : ", str(prix_tot))

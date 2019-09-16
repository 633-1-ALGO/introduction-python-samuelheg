# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
nb_exemple = texte.count("exemple")
print("exemple apparaît", nb_exemple, " fois.")

#BONUS source: https://www.journaldev.com/23647/python-reverse-string
def reverse_slicing(s):
    return s[::-1]

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

print(reverse_slicing(texte))
print(reverse_for_loop(texte))




def verif_invariant(ST, phi):
    R = set()  # Ensemble des états accessibles
    U = []  # Pile d'états
    b = True  # Booléen

    def visiter(s):
        nonlocal R, U, b
        U.append(s)  # on pose s sur la pile
        R.add(s)  # on marque s comme accessible
        while U:  # tant que la pile n'est pas vide
            s_prime = U[-1]  # s' est le premier élément de la pile
            if Post(s_prime).issubset(R):
                U.pop()  # on retire le premier élément de la pile
                b = b and phi(s_prime)  # on vérifie la validité de phi en s'
            else:
                s_double_prime = next(iter(Post(s_prime) - R))  # s'' est un nouvel état accessible
                U.append(s_double_prime)
                R.add(s_double_prime)

    while R or any(not phi(e) for e in R):
        s = choisir_etat_initial(ST, R)  # on choisit arbitrairement un état initial qui n'est pas dans R
        visiter(s)

    if b:
        return "OUI"
    else:
        return "NON", U

def choisir_etat_initial(ST, R):
    # Cette fonction doit choisir un état initial dans ST qui n'est pas déjà dans R
    # Ici, j'utilise une approche simpliste, mais cela peut dépendre de la structure exacte de ST.
    for etat in ST:
        if etat not in R:
            return etat

# Définition de la fonction Post pour notre ST
def Post(s):
    if s < 3:
        return {s + 1}
    else:
        return set()

# Proposition logique pour le cas "OUI"
def phi_oui(s):
    return s % 2 == 0

# Proposition logique pour le cas "NON"
def phi_non(s):
    return s < 3

# Système de transition
ST = {0, 1, 2, 3}

# Test pour le cas "OUI"
result_oui = verif_invariant(ST, phi_oui)
print("Résultat pour le cas 'OUI':", result_oui)  # Devrait afficher "OUI"

# Test pour le cas "NON"
result_non = verif_invariant(ST, phi_non)
print("Résultat pour le cas 'NON':", result_non)  # Devrait afficher "NON" suivi de l'état qui viole la proposition

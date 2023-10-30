class FiniteStateMachine:
    def __init__(self):
        # Liste des états accessibles
        self.R = set()
        # Pile des états
        self.U = []
        # Boolean pour vérifier la validité de la proposition logique
        self.b = True

    # Fonction pour obtenir les post-états d'un état donné
    def post(self, state):
        # Ici, il faudra définir comment on obtient les post-états.
        # Je mets un exemple simple en supposant une fonction fictive.
        # Cette fonction doit être définie en fonction de ton système de transition fini ST.
        return fictive_function_for_post_state(state)

    # Fonction pour vérifier une proposition logique sur un état donné
    def check_phi(self, state):
        # Encore une fois, il faut définir comment vérifier la proposition.
        # Je suppose une fonction fictive pour l'instant.
        return fictive_function_to_check_phi(state)

    def visiter(self, s):
        self.U.append(s)
        self.R.add(s)

        while self.U:
            s_prime = self.U[-1]  # Prendre le dernier élément de la pile

            if self.check_phi(s_prime):
                self.U.pop()
            else:
                s_double_prime = next((state for state in self.post(s_prime) if state not in self.R), None)
                if s_double_prime:
                    self.U.append(s_double_prime)
                    self.R.add(s_double_prime)
                else:
                    self.b = False
                    break

    def verification_dinvariant(self, ST, phi):
        # ST est le système de transition fini
        # phi est la proposition logique

        # Ici, on devrait avoir une manière de choisir un état initial dans ST qui n'est pas dans R.
        # Je suppose une fonction fictive pour cela.
        s = fictive_function_to_choose_initial_state(ST, self.R)

        while s and self.b:
            self.visiter(s)
            s = fictive_function_to_choose_initial_state(ST, self.R)

        return "OUI" if self.b else "NON"

# Exemple d'utilisation :
fsm = FiniteStateMachine()
result = fsm.verification_dinvariant(my_ST, my_phi)
print(result)

class TransitionSystem:
    def __init__(self, states, transitions, initial_state):
        self.states = states  # Les états possibles du système
        self.transitions = transitions # Les transitions possibles entre les états
        self.initial_state = initial_state # L'état initial du système

    def check_invariant(self, phi):
        R = set() # L'ensemble des états visités
        U = [] # Une pile pour gérer les états en cours de visite
        b = True # Un indicateur d'invariance initialisé à True

        def satisfies_phi(state):
            return phi(state)  # Une fonction qui évalue la proposition logique sur un état

        def visit(state): 
            nonlocal b #Déclarer b comme variable non locale pour le modifier dans cette fonction
            U.append(state) # Ajouter l'état actuel à la pile de visite
            R.add(state) # Marquer l'état comme visité
            while U:
                s_prime = U[-1] # Prendre le dernier état ajouté à la pile
                if all(s in R for s in self.transitions.get(s_prime, [])): # Vérifier si tous les états accessibles depuis s_prime sont déjà visités
                    U.pop() # S'ils le sont, retirer l'état actuel de la pile
                    if not satisfies_phi(s_prime):   # Vérifier si l'état ne satisfait pas la proposition logique
                       b = False 
                    
                    b = b and satisfies_phi(s_prime)
                else:
                    next_state = self.find_next_unvisited_transition(s_prime, R)
                    if next_state is not None:
                        U.append(next_state) # Ajouter le prochain état non visité à la pile
                        R.add(next_state) # Marquer le prochain état comme visité
                    else:
                        U.pop() # S'il n'y a plus d'états non visités accessibles, retirer l'état actuel

        visit(self.initial_state)# Commencer la visite à partir de l'état initial

        if b:
            return "OUI"  # Si l'invariance est maintenue, retourner "OUI"
    
        else:
            return "NON", U  # Sinon, retourner "NON" avec la pile d'états non conformes
        
# Fonction pour tester la satisfaction de chaque état par rapport à la proposition Ф
    def find_next_unvisited_transition(self, s, R):
        for next_state in self.transitions.get(s, []):
                  if next_state not in R:
                     return next_state
        return None
    
        

def tester_satisfaction_pour_tous_les_etats(ensemble_etats, Ф):
    resultat = {}
    for etat in ensemble_etats:
        resultat[etat] = Ф(etat)  # Évaluer la proposition logique sur chaque état
    return resultat

# Modèle de système de transition pour l'exclusion mutuelle avec un sémaphore binaire
states = {"NonCritique", "Attente", "Critique"}

# Transitions possibles entre les états
transitions = {
    "NonCritique": ["Attente"],
    "Attente": ["NonCritique", "Critique"],
    "Critique": ["NonCritique"]
}

# État initial
initial_state = "NonCritique"

# Proposition logique : Il ne peut y avoir qu'un seul processus à la fois dans l'état Critique
def Ф(etat):
    return (etat.count("Critique") <= 1)

# Créez une instance du système de transition
ST = TransitionSystem(states, transitions, initial_state)

# Testez l'invariant d'exclusion mutuelle
resultat = ST.check_invariant(Ф)
print(resultat)

# Testez la satisfaction de chaque état par rapport à la proposition Ф
etats_satisfaisants = tester_satisfaction_pour_tous_les_etats(states, Ф)
print(f"États satisfaisants pour l'exclusion mutuelle : {etats_satisfaisants}")
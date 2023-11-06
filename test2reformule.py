class TransitionSystem:
    def __init__(self, states, transitions, initial_state):
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state

    def satisfies_invariant(self, phi):
        visited = set()
        stack = [self.initial_state]

        while stack:
            current_state = stack.pop()
            if not phi(current_state) or any(next_state not in visited and next_state in stack
                                             for next_state in self.transitions.get(current_state, [])):
                return "NON", stack + [current_state]
            
            visited.add(current_state)
            for next_state in self.transitions.get(current_state, []):
                if next_state not in visited:
                    stack.append(next_state)
        
        return "OUI"

    def check_invariant(self, phi):
        return self.satisfies_invariant(phi)


def test_phi_satisfaction(states, phi):
    return {state: phi(state) for state in states}


def phi(state):
    return state.count("Critique") <= 1


# Données du système de transition
states = {"NonCritique", "Attente", "Critique"}
transitions = {
    "NonCritique": ["Attente"],
    "Attente": ["NonCritique", "Critique"],
    "Critique": ["NonCritique"]
}
initial_state = "NonCritique"

# Initialisation et test du système de transition
transition_system = TransitionSystem(states, transitions, initial_state)
invariant_result = transition_system.check_invariant(phi)
print(invariant_result)

# Test de la satisfaction de la proposition phi pour chaque état
satisfying_states = test_phi_satisfaction(states, phi)
print(f"États satisfaisants pour l'exclusion mutuelle : {satisfying_states}")

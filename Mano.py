class StateTransition:
    def __init__(self):
        # Set of accessible states
        self.R = set()
        # Stack of states
        self.U = []
        # Boolean value, initialized to True
        self.b = True

    def Post(self, s):
        # This function should return all possible transitions from state s
        # For now, let's assume an empty set; you'll need to fill in the logic.
        return set()

    def check_property(self, s):
        # This function checks if state s satisfies the property Φ
        # You'll need to define this based on your application.
        return False

    def visiter(self, s):
        self.U.append(s)
        self.R.add(s)
        
        while self.U and self.b:
            s_prime = self.U[-1]
            
            if s_prime in self.R:
                self.U.pop()
                self.b = self.b and self.check_property(s_prime)
            else:
                s_double_prime = None  # Choose a state from Post(s') that is not in R
                for state in self.Post(s_prime):
                    if state not in self.R:
                        s_double_prime = state
                        break

                if s_double_prime:
                    self.U.append(s_double_prime)
                    self.R.add(s_double_prime)
                else:
                    self.U.pop()

    def verification_invariant(self, ST, prop_logic):
        # Assuming ST is the finite transition system and prop_logic is the logical proposition Φ
        while not self.b and ST:  # Assuming ST is an iterable, modify as necessary
            s = None  # Choose an initial state that is not in R
            for state in ST:
                if state not in self.R:
                    s = state
                    break
            
            if s:
                self.visiter(s)

        if self.b:
            return "OUI"
        else:
            return "NON", self.U

# Usage:
# st = StateTransition()
# result = st.verification_invariant(ST, prop_logic)
# print(result)

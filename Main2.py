from Property import Or,Not,Property,Unary,And

class State:
    def __init__(self, name, label):
        self.name = name
        self.label = label
    
    def get_name(self):
        print(self.name)
        return self.name
    
    def get_label(self):
        print(self.label)
        return self.label

class TransitionList:
    def __init__(self):
        self.transitions = {}  # Utilise un dictionnaire pour stocker les transitions

    def add_transition(self, state_from, state_to):
        # Ajoute state_to à la liste des transitions pour state_from
        if state_from.get_name() not in self.transitions:
            self.transitions[state_from.get_name()] = []
        self.transitions[state_from.get_name()].append(state_to)

    def display_transitions(self):
        
        # Affiche les transitions
        for state_from, states_to in self.transitions.items():
            print(f"State {state_from}:")
            for state in states_to:
                print(f"  Transition to -> {state.get_name()} (Label: {state.get_label()})")

class TransitionSystem():
    def __init__(self, S, Action, Transition, I, Prop):
        self.S = S
        self.Action = Action
        self.Transition = Transition
        self.I = I
        self.Prop= Prop

def verif_invariant(ST):
    # Set of accessible states
    R = []
    # Stack of states
    U = []
    # Boolean value, initialized to True
    verif = True

    while verif and ST.I not in R:
        s = ST.I  # On choisit arbitrairement un état initial
        if s not in R:
            visiter(R,U,verif,s,ST)

    if verif:
        return "OUI"
    else:
        return "NON", print(U)
    
def visiter(R,U,verif,s,ST):
        U.append(s) # on ajoute s à la pile 
        R.append(s) # on marque s comme accessible
        print("dans visiter")
        while U != 0 and verif:
            s_prime = U[-1] # s' devient le premier element de la pile
            print("dans le while")
            if s_prime in R: # si s' est dans R alors
                print("if")
                U.pop() # on enlève le premier élément de la pile
                verif = verif and check_property(s_prime) # on teste si la condition phi est toujours valide dans s'
            else:
                print("else")
                s_double_prime = None  # on initialise
                for state in Post(s_prime): # Choose a state from Post(s') that is not in R
                    if state not in R:
                        s_double_prime = state
                        print("break")
                        break

                if s_double_prime:
                    print("if double prime")
                    U.append(s_double_prime)
                    R.append(s_double_prime)
                else:
                    print("else double_prime")
                    U.pop()

def check_property(self, s_prime):
        print("check_property")
        return True

def Post(self, s_prime):
    print("post")
    # Placeholder for post function logic
    # Needs to be implemented
    return []



def main():

    State1 = State(1,{"n1","n2"})
    State2 = State(2,{"p1","n2"})
    State3 = State(3,{"n1","p2"})
    State4 = State(4,{"p1","p2"})
    State5 = State(5,{"c1","n2"})
    State6 = State(6,{"n1","c2"})
    State7 = State(7,{"c1","p2"})
    State8 = State(8,{"p1","c2"})

    States = {State1,State2,State3,State4,State5,State6,State7,State8}

    Action =["epsilon"]

    # State1.get_name()
    # State1.get_label()

    transitionList = TransitionList()
    transition_list = TransitionList()


    # transistion State1
    transition_list.add_transition(State1,State2)

    transitionList.add_transition(State1,State2)
    transitionList.add_transition(State1,State3)

    # transistion State2
    transitionList.add_transition(State2,State4)
    transitionList.add_transition(State2,State5)
   
    # transistion State3
    transitionList.add_transition(State3,State4)
    transitionList.add_transition(State3,State6)

    # transistion State4
    transitionList.add_transition(State4,State7)
    transitionList.add_transition(State4,State8)

    # transistion State5
    transitionList.add_transition(State5,State7)
    transitionList.add_transition(State5,State1)

    # transistion State6
    transitionList.add_transition(State6,State8)
    transitionList.add_transition(State6,State1)

    # transistion State7
    transitionList.add_transition(State7,State3)

    # transistion State8
    transitionList.add_transition(State8,State2)

    print("Tableau des transitions")
    #transitionList.display_transitions()

    Prop ={"n1","n2","p1","p2","c1","c2"}
    I ={State1}


    Phi = Or(Not(Unary({"c1"})),Not(Unary({"c2"})))

    ST = TransitionSystem(8,Action,transitionList,I,Phi)

    #verif_invariant(ST)
    #transition_list.display_transitions()

main()
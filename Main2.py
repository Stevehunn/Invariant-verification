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

    # State1.get_name()
    # State1.get_label()

    transitionList = TransitionList()

    # transistion State1
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
    transitionList.display_transitions()

main()
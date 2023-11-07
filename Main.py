from Property import Or,Not,Property,Unary,And

class State:
    def __init__(self, name, label):
        self.name = name
        self.label = label
    
    def get_name(self):
        return self.name
    
    def get_label(self):
        return self.label

class Transition:
    def __init__(self, state, nextNode=None):
        self.state = state
        self.nextNode = nextNode

class TransitionList:
    def __init__(self):
        self.head = None

    def add_node(self, state):
        if not self.head:
            self.head = Transition(state)
        else:
            new_node = Transition(state, self.head)
            self.head = new_node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.nextNode


class StateTransition:
    def __init__(self, s, act, transition, initial_state, prop):
        # Sommet
        self.s = s
        # Action
        self.act = act
        # Transition
        self.transition = transition
        # Initial State
        self.init_state = initial_state
        # Prop
        self.prop = prop

    def verification_invariant(self):
        # Set of accessible states
        self.R = set()
        # Stack of states
        self.U = []
        # Boolean value, initialized to True
        self.b = True

        # Assuming ST is the finite transition system and prop_logic is the logical proposition Φ
        ST = self  # Assuming ST refers to the current instance of StateTransition
        while self.b and ST:
            s = ST.init_state  # On choisit arbitrairement un état initial
            if s not in self.R:
                self.visiter(s)

        if self.b:
            return "OUI"
        else:
            return "NON", self.U

    def visiter(self, s):
        self.U.append(s)
        self.R.add(s)
        print("dans visiter")
        while self.U and self.b:
            s_prime = self.U[-1]
            self.U.insert(0,s_prime)
            print("dans le while")
            if s_prime in self.R:
                self.U.pop()
                content_pile = self.U 
                print(content_pile)
                self.b = self.b and self.check_property(s_prime)
                print("if")
            else:
                print("else")
                s_double_prime = None  # Choose a state from Post(s') that is not in R
                # Assuming Post is a function that needs to be defined
                for state in self.Post(s_prime):
                    if state not in self.R:
                        s_double_prime = state
                        print("break")
                        break

                if s_double_prime:
                    self.U.append(s_double_prime)
                    self.R.add(s_double_prime)
                    print("if double prime")
                else:
                    print("else pop")
                    self.U.pop()

    def check_property(self, s_prime):
        print("check_property")
        if(self.prop != s_prime):
            return True
        else:return False

    def Post(self, s_prime, ST,s,R):
        print("post")
        post = ST.Transition[s.name]

        # Placeholder for post function logic
        # Needs to be implemented
        return []
    

def exemple1():
    State1 = State(1,{"n1","n2"})
    State2 = State(2,{"p1","n2"})
    State3 = State(3,{"n1","p2"})
    State4 = State(4,{"p1","p2"})
    State5 = State(5,{"c1","n2"})
    State6 = State(6,{"n1","c2"})
    State7 = State(7,{"c1","p2"})
    State8 = State(8,{"p1","c2"})

    States = {State1,State2,State3,State4,State5,State6,State7,State8}

    Act =["epsilon"]

    noeud1 =TransitionList()
    noeud1.add_node(State2)
    noeud1.add_node(State3)

    noeud2 =TransitionList()
    noeud2.add_node(State4)
    noeud2.add_node(State5)

    noeud3 =TransitionList()
    noeud3.add_node(State4)
    noeud3.add_node(State6)

    noeud4=TransitionList()
    noeud4.add_node(State7)
    noeud4.add_node(State8)

    noeud5=TransitionList()
    noeud5.add_node(State7)
    noeud5.add_node(State1)

    noeud6=TransitionList()
    noeud6.add_node(State8)
    noeud6.add_node(State1)


    noeud7=TransitionList()
    noeud7.add_node(State3)

    noeud8=TransitionList()
    noeud8.add_node(State2)


    Transitions=[noeud1,noeud2,noeud3,noeud4,noeud5,noeud6,noeud7,noeud8]

    Prop ={"n1","n2","p1","p2","c1","c2"}
    I ={State1}

    Phi = Or(Not(Unary({"c1"})),Not(Unary({"c2"})))

    calcul_inv = StateTransition(8,Act,Transitions,State1,Phi)
    StateTransition.verification_invariant(calcul_inv)




def main():
    # ... [Rest of your main function code] ...

    # You will need to define the Or, Not, and Unary functions or classes
    # Phi = Or(Not(Unary({"c1"})), Not(Unary({"c2"})))

    # ... [Rest of your main function code] ...

    # Assuming Phi is defined and State1 is an instance of State
    # calcul_inv = StateTransition(8, Act, Transitions, State1, Phi)
    # result = StateTransition.verification_invariant(calcul_inv)
    # print(result)
    exemple1()


main()  # Uncomment to run the main function
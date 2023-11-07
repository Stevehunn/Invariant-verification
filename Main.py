from typing import Callable
from Property import *

# Définition d'une classe Context qui contient une valeur entière 'y'
class Context:
    def __init__(self, y: int):
        self.y = y

     # Méthode pour créer et retourner une copie du contexte courant
    def copy(self):
        return Context(self.y)

# Définition d'une classe Condition qui prendra deux fonctions : une pour vérifier une condition et une pour appliquer une transition
class Condition:
    def __init__(self, function_condition: Callable, function_transition: Callable):
        self.inner_callable = function_condition
        self.transition_callable = function_transition

     # Méthode pour vérifier si la condition est remplie en utilisant le contexte passé
    def check(self, context: Context) -> bool:
        return self.inner_callable(context)

     # Méthode pour appliquer la fonction de transition au contexte et retourner le nouveau contexte
    def apply_transition(self, context: Context) -> Context:
        new_context = context.copy()
        self.transition_callable(new_context)
        return new_context

# Définition d'une classe State pour représenter un état dans une machine à états
class State:
    def __init__(self, t1: str, t2: str):
        self.next_states: set[(State, Condition)] = set()
        self.inner_state_info: tuple[str, str] = (t1, t2)
    
    # Retourne l'étiquette de l'état
    def get_label(self) -> tuple[str, str]:
        return self.inner_state_info

    # Méthode d'égalité pour vérifier si deux instances de State sont identiques
    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self.inner_state_info[0] == other.inner_state_info[0] and self.inner_state_info[1] == other.inner_state_info[1] and self.inner_state_info[2] == other.inner_state_info[2]
        return False
    
    # Méthode de hachage pour permettre d'utiliser les instances de State dans des ensembles et comme clés de dictionnaire
    def __hash__(self) -> int:
        return hash(self.inner_state_info[0]) ^ hash(self.inner_state_info[1])

    # Méthode pour générer l'état suivant et le contexte après l'application de la condition de transition
    def post(self, context: Context):
        for next_state, condition in self.next_states:
            if condition.check(context):
                yield next_state, condition.apply_transition(context)


    # Méthode de représentation pour imprimer les informations de l'état
    def __repr__(self) -> str:
        return repr(self.inner_state_info)

# Définition d'une classe Stack pour représenter une structure de données dernier entré, premier sorti (LIFO)
class Stack:
    def __init__(self):
        self.inner_stack = list()

    # Méthode pour ajouter un élément à la pile
    def push(self, elm):
        self.inner_stack.append(elm)

    # Méthode pour vérifier si la pile est vide
    def is_empty(self) -> bool:
        return len(self.inner_stack) == 0

    # Méthode pour retourner l'élément supérieur de la pile sans le retirer
    def top(self) -> State:
        return self.inner_stack[-1]

    # Méthode pour retirer et retourner l'élément supérieur de la pile
    def pop(self) -> State:
        return self.inner_stack.pop()
    
    # Méthode de représentation pour imprimer la pile
    def __repr__(self) -> str:
        return repr(self.inner_stack)

# Définition d'une fonction qui évalue une propriété contre un état
def phi(s: State, prop) -> bool:
    return prop.eval(s)

# Une fonction visiteur pour explorer les états
def visiter(s: State, stack_u: Stack, set_r: set[State], bool_b: bool, context: Context, prop):
    stack_u.push((s, context))
    set_r.add(s)
    new_context = context
    print(stack_u)
    while not stack_u.is_empty() or not bool_b:
        s_prime, new_context = stack_u.top()
        s_prime_2, new_context = next(s_prime.post(context))
        if s_prime_2 in set_r:
            stack_u.pop()
            bool_b = bool_b and phi(s_prime,prop)
        else:
            while s_prime_2 in set_r:
                s_prime_2, new_context = next(s_prime.post(new_context)) # state.post() return generator, next() to get next value of generator
            stack_u.push((s_prime_2, new_context))
            set_r.add(s_prime_2)
    return set_r, bool_b, new_context

# Algorithme principal qui utilise la fonction visiteur pour traverser les états
def algo_1(set_states: set[State], context: Context,prop):
    b: bool = True
    R: set[State] = set()
    U: Stack = Stack()
    I = set_states
    s: State = list(I)[0]
    while len(I.difference(R)) != 0 and b:
        s = list(I.difference(R))[0]
        R, b, new_context = visiter(s, U, R, b, context,prop)
    if b:
        print("OUI")
    else:
        print("NON", U)

def main():
    # Conditions
    def no_condition(context: Context) -> bool:
        return True

    def not_negative(context: Context) -> bool:
        return context.y > 0

    # Actions
    def plus_one(context: Context):
        context.y += 1

    def minus_one(context: Context):
        context.y -= 1

    def do_nothing(context: Context):
        pass

    # Etats
    State1 = State("n1", "n2")
    State2 = State("p1", "n2")
    State3 = State("n1", "p2")
    State4 = State("c1", "n2")
    State5 = State("p1", "p2")
    State6 = State("n1", "c2")
    State7 = State("c1", "p2")
    State8 = State("p1", "c2")
    State9 = State("c1", "c2")
    set_states = {State1, State2, State3, State4, State5, State6, State7, State8}

    no_condition_do_nothing = Condition(no_condition, do_nothing)
    not_neg_condition = Condition(not_negative, minus_one)
    no_condition_add_one =Condition(no_condition, plus_one)


    # Ajout Transition aux Etats avec condition necessaire
    State1.next_states.add((State2, no_condition_do_nothing))
    State1.next_states.add((State3, no_condition_do_nothing))

    State2.next_states.add((State4, no_condition_do_nothing))
    State2.next_states.add((State5, not_neg_condition))

    State3.next_states.add((State4, no_condition_do_nothing))
    State3.next_states.add((State6, not_neg_condition))

    State4.next_states.add((State7, not_neg_condition))
    State4.next_states.add((State8, not_neg_condition))

    State5.next_states.add((State1, no_condition_add_one))
    State5.next_states.add((State7, no_condition_do_nothing))

    State6.next_states.add((State1, no_condition_add_one))
    State6.next_states.add((State8, no_condition_do_nothing))

    State7.next_states.add((State3, no_condition_add_one))

    State8.next_states.add((State2, no_condition_add_one))

    State9.next_states.add((State5, no_condition_add_one))
    State9.next_states.add((State6, no_condition_add_one))
    # Prop = {"n1","n2","p1","p2","c1","c2"}
    # Proposition Phi
    Phi = Or(Not(Unary("c1")),Not(Unary("c2")))

    # Contexte
    actual_context = Context(1)
    algo_1(set_states, actual_context,Phi)


if __name__ == "__main__":
    main()

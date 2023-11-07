# Définition de la classe Property représentant les Propertys logiques P
import abc

class Property(abc.ABC):
    def eval(self, state):
        ...

class Not(Property):
    def __init__(self, term: Property):
        self.term = term
    
    def eval(self, elm: str):
        return not self.term.eval(elm)

class Or(Property):
    def __init__(self, term1: Property, term2: Property):
        self.term1 = term1
        self.term2 = term2
    
    def eval(self, state):
        return self.term1.eval(state) or self.term2.eval(state)

class Unary(Property):
    def __init__(self, term):
        self.term = term
    
    def eval(self, state):
        return self.term in state.get_label()

class And(Property):
    def __init__(self, term1: Property, term2: Property):
        self.term1 = term1
        self.term2 = term2
    
    def eval(self, state):
        return self.term1.eval(state) and self.term2.eval(state)

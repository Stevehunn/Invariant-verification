# Définition de la classe Property représentant les Propertys logiques P

class Property:
    def __init__(self):
        pass

    def eval():
        pass

class Not(Property):

    term: Property

    def __init__(self, term):
        self.term = term
    
    def eval(labels):
        return not self.term.eval(labels)

class Or(Property):

    term1: Property
    term2: Property

    def __init__(self, term1, term2):
        self.term1
        self.term2
    
    def eval(labels):
        return self.term1.eval(labels) or self.term2.eval(labels)

class Unary(Property):

    term: Property

    def __init__(self, term):
        self.term = term
    
    def eval(labels):
        for l in labels:
            if label == term
            return true
        
        return false

class And(Property):

    term1: Property
    term2: Property

    def __init__(self, term1, term2):
        self.term1
        self.term2
    
    def eval(labels):
        return self.term1.eval(labels) and self.term2.eval(labels)
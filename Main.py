from typing import Callable


class Condition:
    def __init__(self, function_condition: Callable, function_transition: Callable):
        self.inner_callable = function_condition
        self.transition_callable = function_transition

    def check(self, context) -> bool:
        return self.inner_callable(context)

    def apply_transition(self, context):
        self.transition_callable(context)

class Context:
    def __init__(self, y: int):
        self.y = y

class State:
    def __init__(self, t1: str, t2: str):
        self.next_states: set[(State, Condition)] = set()
        self.inner_state_info: tuple[str, str] = (t1, t2)

    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self.inner_state_info[0] == other.inner_state_info[0] and self.inner_state_info[1] == other.inner_state_info[1] and self.inner_state_info[2] == other.inner_state_info[2]
        return False

    def post(self, context: Context):
        for next_state, condition in self.next_states:
            if condition.check(context):
                yield next_state

class Stack:
    def __init__(self):
        self.inner_stack = list()

    def push(self, elm):
        self.inner_stack.append(elm)

    def is_empty(self) -> bool:
        return len(self.inner_stack) == 0

    def top(self) -> State:
        return self.inner_stack[-1]

    def pop(self) -> State:
        return self.inner_stack.pop()

def phi(s: State) -> bool:
    return True # TODO

def visiter(s: State, stack_u: Stack, set_r: set[State], bool_b: bool, context: Context):
    stack_u.push(s)
    set_r.add(s)
    while not stack_u.is_empty() or not bool_b:
        s_prime = stack_u.top()
        if next(s_prime.post(context)) in set_r:
            stack_u.pop()
            bool_b = bool_b and phi(s_prime)
        else:
            s_prime_2 = next(s_prime.post(context))  # state.post() return generator, next() to get next value of generator
            while s_prime_2 in set_r:
                s_prime_2 = next(s_prime.post(context)) # state.post() return generator, next() to get next value of generator
                stack_u.push(s_prime_2)
                set_r.add(s_prime_2)
    return set_r, bool_b

def algo_1(set_states: set[State], context: Context):
    b: bool = True
    R: set[State] = set()
    U: Stack = Stack()
    I: State | None = None  # TODO
    s: State = I
    while I not in R and b:
        s: State = I
        R, b = visiter(s, U, R, b, context)
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
    State4 = State("p1", "p2")
    State5 = State("c1", "n2")
    State6 = State("n1", "c2")
    State7 = State("c1", "p2")
    State8 = State("p1", "c2")
    set_states = {State1, State2, State3, State4, State5, State6, State7, State8}
    no_condition_do_nothing = Condition(no_condition, do_nothing)

    State1.next_states.add((State2, no_condition_do_nothing))
    State1.next_states.add((State3, no_condition_do_nothing))

    # Contexte
    actual_context = Context(1)
    algo_1(set_states, actual_context)


if __name__ == "__main__":
    main()

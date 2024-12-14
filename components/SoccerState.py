class State:
    def __init__(self, name: str):
        self.name: str = name
        self.transitions: dict = {}

    def add_transition(self, symbol: str, state):
        self.transitions[symbol] = state

    def next_state(self, symbol: str):
        return self.transitions.get(symbol, None)

    def __str__(self):
        return f"State({self.name})"

    def __repr__(self):
        return f"State({self.name})"

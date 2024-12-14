from components.SoccerState import State


class NFA:

    def __init__(self):
        self.states = [] 
        self.alphabet = [] 
        self.initial_state = None  
        self.final_states = []  

    def add_state(self, state: State):
        self.states.append(state)

    def parse_input_to_nfa(self, input_string: str):
        lines = input_string.strip().split("\n")

        # Remove comments and empty lines
        lines = [line.split("#")[0].strip() for line in lines if line.strip() and not line.strip().startswith("#")]

        states = lines[0].split()
        alphabet = lines[1].split()
        initial_state_name = lines[2].strip()
        final_states_names = lines[3].split()

        # Add states
        for name in states:
            self.add_state(State(name))

        self.alphabet = alphabet

        # Add transitions
        for line in lines[4:]:
            state_name, symbol, next_state_name = line.split()
            state = next(s for s in self.states if s.name == state_name)
            next_state = next(s for s in self.states if s.name == next_state_name)
            state.add_transition(symbol, next_state)

        # Set initial and final states
        self.initial_state = next(s for s in self.states if s.name == initial_state_name)
        self.final_states = [s for s in self.states if s.name in final_states_names]

    def run(self, input_string: str) -> bool:
        current_states = [self.initial_state]

        # Split input string into symbols based on the alphabet
        symbol_list = []
        buffer = ""
        for char in input_string:
            buffer += char
            if buffer in self.alphabet:
                symbol_list.append(buffer)
                buffer = ""

        for symbol in symbol_list:
            next_states = []
            for state in current_states:
                next_state = state.next_state(symbol)
                if next_state:
                    next_states.append(next_state)
            if not next_states:
                return False
            current_states = next_states

        return any(state in self.final_states for state in current_states)

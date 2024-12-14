from components.soccernfa import NFA
from tests import accept

def main():
    nfa = NFA()
    with open("src/automata/exampleNfa.txt", "r") as file:
        nfa.parse_input_to_nfa(file.read())

    print("Welcome to the Soccer Automaton Tester!")
    print("Enter strings to test. Type '0' to exit.")

    while True:
        test = input("Enter a string: ").strip()
        if test == "0":
            print("Goodbye!")
            break
        result = accept(nfa, test)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

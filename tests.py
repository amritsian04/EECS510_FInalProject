from components.soccernfa import NFA

def accept(nfa: NFA, string: str) -> str:
    return "accept" if nfa.run(string) else "reject"

def run_tests():
    nfa = NFA()
    # Use absolute path to exampleNfa.txt
    import os
    file_path = os.path.join(os.path.dirname(__file__), "automata/exampleNfa.txt")
    with open(file_path, "r") as file:
        nfa.parse_input_to_nfa(file.read())

    test_strings = [
        "g45⚽",  # Valid
        "r78🟥",  # Valid
        "p30⚽",  # Valid
        "s10🎯",  # Valid
        "g",      # Invalid
        "12⚽",    # Invalid
        "90⚽🟥"   # Invalid
    ]

    for test in test_strings:
        result = accept(nfa, test)
        print(f"String: {test} -> Result: {result}")

if __name__ == "__main__":
    run_tests()

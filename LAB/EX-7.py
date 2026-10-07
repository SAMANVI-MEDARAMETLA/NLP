#Experiment 7: Finite State Automaton for Strings Ending with 'ab'

def fsa(s):
    state = "q0"
    print("Start:", state)

    for ch in s:
        if state == "q0":
            state = "q1" if ch == "a" else "q0"
        elif state == "q1":
            state = "q1" if ch == "a" else "q2"
        elif state == "q2":
            state = "q1" if ch == "a" else "q0"

        print(ch, "->", state)

    print("Result:", "Accepted" if state == "q2" else "Rejected")


for s in ["ab", "aab", "abb", "abab"]:
    print("\nInput:", s)
    fsa(s)

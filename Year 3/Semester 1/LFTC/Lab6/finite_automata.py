from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Set


# A production is:
# (left-hand nonterminal, right-hand side)
#
# None represents epsilon.
# A terminal can be a literal character or a symbolic class.
ProductionRule = Tuple[str, Optional[Tuple[str, ...]]]


# Terminal character classes

def is_letter(ch):
    return len(ch) == 1 and ch.isascii() and ch.isalpha()


def is_digit(ch):
    return len(ch) == 1 and ch in "0123456789"


def is_nonzero(ch):
    return len(ch) == 1 and ch in "123456789"


def is_id_start(ch):
    return is_letter(ch) or ch == "_"


def is_id_rest(ch):
    return is_letter(ch) or is_digit(ch) or ch == "_"


def is_character_char(ch):
    return len(ch) == 1 and (
        is_letter(ch)
        or is_digit(ch)
        or ch in "-_.,!? :;()"
    )


def is_string_char(ch):
    return is_character_char(ch)


CLASSES = {
    "@LETTER": is_letter,
    "@DIGIT": is_digit,
    "@NONZERO": is_nonzero,
    "@ID_START": is_id_start,
    "@ID_REST": is_id_rest,
    "@STRING_CHAR": is_string_char,
    "@CHARACTER_CHAR": is_character_char,
}

# checks if a terminal belongs to any of the above classes
def matches(terminal, char):
    if terminal in CLASSES:
        return CLASSES[terminal](char)

    return terminal == char

@dataclass
class FiniteAutomata:
    # FA has: Q - states, Sigma - terminals, Gamma - transition rules, q0 - initial state, F - final states
    start_state: str
    final_states: Set[str]
    transitions: Dict[str, List[Tuple[str, str]]]

    # ex: 60 - integer =>
#{
#     "N": [("0", "FINAL"), ("@NONZERO", "A")],
#     "A": [("@DIGIT", "A")]
# }
    def accepts(self, text):
        # states = {"N"}
        states = {self.start_state}

        for char in text:
            # 1. char = 6
            # 2. char = 0
            #   next_states gets refreshed
            # 3. Stops cause there are no more characters in the text
            next_states = set()

            # 1. states = {"N"}
            # 2. states = {"A"}
            for state in states:
                # gets the next rule + the state it leads to for the current state
                # 1. N -> ("0", "FINAL"), ("@NONZERO", "A")
                # 2. A -> [("@DIGIT", "A")]
                for terminal, destination in self.transitions.get(state, []):
                    # 1.
                    #   a. terminal = 0, destination = final
                    #       0 is not in CLASSES, and is not = 6, so we do not move to its destination
                    #   b. terminal = @NONZERO, destination = A
                    #       @NONZERO is in classes, and 6 is valid for the class, so we go to its destination = A
                    #
                    # 2. terminal = @DIGIT, destination = A
                    #       @DIGIT ia a CLASS, and 0 is valid => next_states = {A}
                    if matches(terminal, char):
                        next_states.add(destination)

            # Refresh next states to check
            # 1. states = A
            # 2. states = A
            states = next_states

            # if there are no states to check, this is an invalid automata
            if not states:
                return False

        # states = {"A"}, final_states = "A"
        # final_states = {"FINAL", "A"}
        # check that at least one final state is included in states
        return bool(states & self.final_states)


# Regular Grammar -> Finite Automaton

def rg_to_fa(start_symbol, grammar_rules):
    # S: [(@LETTER, "A"), (@DIGIT, 1)]
    # means that: From state S, if character matches @LETTER, move onto
    # state A
    transitions = {}
    final_states = set()

    # gets all the symbols: get the state for every state, rule pair in the grammar
    nonterminals = {lhs for lhs, _ in grammar_rules}
    # special state we add to transitions to terminals ONLY
    # so for: X:("@RULE", )
    # NOT FOR: X: None, X: ("@RULE", "NextState")
    # this is bc the starting state SHOULD NOT BE the final state in this implementation
    # ex: "" could be considered a valid integer bc
    # it skips the whole character check (it is empty) and only checks
    # if N is in its final states, which it would be in this situation
    final_state = "FINAL"

    # for every state - rule pair in the grammar
    for lhs, rhs in grammar_rules:

        # check epsilon
        # aka if the current state points to an empty rule
        if rhs is None or len(rhs) == 0:
            final_states.add(lhs)

        # A -> terminal B
        elif len(rhs) == 2:
            terminal, destination = rhs

            #check for undefined destination states
            if destination not in nonterminals:
                raise ValueError(
                    f"Unknown nonterminal: {destination}"
                )

            # add the transition as:
            # transitions["S"] = [("@ID_START", "A")]
            # so, if a character is valid, move from S to A
            transitions.setdefault(lhs, []).append(
                (terminal, destination)
            )

        # A -> terminal
        elif len(rhs) == 1:
            # this means that we've reached a final state, so we add it as such
            transitions.setdefault(lhs, []).append(
                (rhs[0], final_state)
            )

            final_states.add(final_state)

        else:
            raise ValueError(
                f"Invalid production: {lhs} -> {rhs}"
            )

    return FiniteAutomata(
        start_symbol,
        final_states,
        transitions
    )

# Regular Grammars
# ex:
# {
#     "S": [("@ID_START", "A")],
#     "A": [("@ID_REST", "B"), ("A", "FINAL")],
# }
IDENTIFIER_GRAMMAR = [
    ("S", ("@ID_START", "A")),
    ("A", ("@ID_REST", "A")),
    ("A", None),
]

# ex:
# {
#     "N": [("0", "FINAL"), ("@NONZERO", "A")],
#     "A": [("@DIGIT", "A")]
#       "A" can point to nothing => it will be added to the final states
# }
INTEGER_GRAMMAR = [
    ("N", ("0",)),
    ("N", ("@NONZERO", "A")),
    ("A", ("@DIGIT", "A")),
    ("A", None),
]

BOOLEAN_GRAMMAR = [
    ("B", ("t", "T")),
    ("T", ("r", "U")),
    ("U", ("u", "V")),
    ("V", ("e",)),

    ("B", ("f", "F")),
    ("F", ("a", "G")),
    ("G", ("l", "H")),
    ("H", ("s", "I")),
    ("I", ("e",)),
]

STRING_GRAMMAR = [
    ("Q", ('"', "A")),
    ("A", ("@STRING_CHAR", "A")),
    ("A", ('"',)),
]

CHARACTER_GRAMMAR = [
    ("C", ("'", "A")),
    ("A", ("@CHARACTER_CHAR", "B")),
    ("B", ("'",)),
]


# Build the automata

AUTOMATA = {
    "IDENTIFIER": rg_to_fa("S", IDENTIFIER_GRAMMAR),
    "INTEGER": rg_to_fa("N", INTEGER_GRAMMAR),
    "BOOLEAN": rg_to_fa("B", BOOLEAN_GRAMMAR),
    "STRING": rg_to_fa("Q", STRING_GRAMMAR),
    "CHARACTER": rg_to_fa("C", CHARACTER_GRAMMAR),
}
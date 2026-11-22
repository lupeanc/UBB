
from pathlib import Path

from antlr4 import CommonTokenStream
from antlr4.ListTokenSource import ListTokenSource
from antlr4.Token import Token
from antlr4.error.ErrorListener import ErrorListener

from .generated.CinematographyParser import CinematographyParser
from .pif_token_source import create_tokens


BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

PARSE_TREE_FILE = OUTPUT_DIR / "parse_tree.txt"
PRODUCTIONS_FILE = OUTPUT_DIR / "productions.txt"
SYNTAX_ERRORS_FILE = OUTPUT_DIR / "syntax_errors.txt"


class SyntaxErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(
        self, recognizer, offendingSymbol,
        line, column, msg, e
    ):
        self.errors.append(
            f"Line {line}, column {column}: {msg}"
        )


def collect_productions(node, parser, productions):
    """
    Visit the parse tree and record the production used
    at each parser rule.
    """

    # Ignore terminal nodes here.
    if not hasattr(node, "getRuleIndex"):
        return

    rule_name = parser.ruleNames[node.getRuleIndex()]

    right_side = []

    for child in node.getChildren():

        if hasattr(child, "getRuleIndex"):
            # A child parser rule.
            child_rule = parser.ruleNames[child.getRuleIndex()]
            right_side.append(child_rule)

        else:
            # A terminal token.
            symbol = child.getSymbol()

            if symbol.type != Token.EOF:
                right_side.append(repr(child.getText()))

    if right_side:
        production = f"{rule_name} -> {' '.join(right_side)}"
    else:
        production = f"{rule_name} -> ε"

    productions.append(production)

    # Visit child rules from left to right.
    for child in node.getChildren():
        if hasattr(child, "getRuleIndex"):
            collect_productions(child, parser, productions)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1. Read the PIF and reconstruct the ANTLR tokens.
    tokens = create_tokens()

    # 2. Give those tokens to ANTLR.
    token_source = ListTokenSource(tokens)
    token_stream = CommonTokenStream(token_source)

    # 3. Create the parser.
    parser = CinematographyParser(token_stream)

    # 4. Collect syntax errors.
    error_collector = SyntaxErrorCollector()
    parser.removeErrorListeners()
    parser.addErrorListener(error_collector)

    # 5. Start parsing from the program rule.
    tree = parser.program()

    # Save syntax errors separately from lexical errors.
    with open(
        SYNTAX_ERRORS_FILE, "w", encoding="utf-8"
    ) as file:

        if error_collector.errors:
            file.write("\n".join(error_collector.errors) + "\n")
        else:
            file.write("No syntax errors found.\n")

    if error_collector.errors:
        print("Parsing failed. Syntax errors were found.")

        for error in error_collector.errors:
            print(error)

        return

    # 6. Save the parse tree.
    with open(
        PARSE_TREE_FILE, "w", encoding="utf-8"
    ) as file:
        file.write(tree.toStringTree(recog=parser))

    # 7. Extract the productions.
    productions = []
    collect_productions(tree, parser, productions)

    with open(
        PRODUCTIONS_FILE, "w", encoding="utf-8"
    ) as file:
        file.write("\n".join(productions) + "\n")

    print("Parsing completed successfully.")
    print(f"Parse tree: {PARSE_TREE_FILE}")
    print(f"Productions: {PRODUCTIONS_FILE}")
    print(f"Syntax errors: {SYNTAX_ERRORS_FILE}")


if __name__ == "__main__":
    main()

import subprocess
from pathlib import Path
from prettytable import PrettyTable, ALL
from scanner import load_token_codes, tokenize

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

SOURCE_FILE = BASE_DIR / "source.txt"
TOKENS_FILE = BASE_DIR / "tokens.txt"

SYMBOL_INPUT_FILE = OUTPUT_DIR / "symbol_input.txt"
SYMBOL_TABLE_FILE = OUTPUT_DIR / "symbol_table.txt"
PIF_FILE = OUTPUT_DIR / "pif.txt"
ERRORS_FILE = OUTPUT_DIR / "errors.txt"

C_PROGRAM = BASE_DIR / "symbol_table.exe"

IDENTIFIER_CODE = 100
CONSTANT_CODE = 101

def write_symbol_input(tokens):
    with open(SYMBOL_INPUT_FILE, "w", encoding="utf-8") as file:

        for kind, lexeme, line_number in tokens:

            if kind == "IDENTIFIER":
                file.write(f"IDENTIFIER\t{lexeme}\n")

            elif kind in ("NUMBER", "STRING", "CHARACTER", "BOOLEAN_CONSTANT"):
                file.write(f"CONSTANT\t{lexeme}\n")

def run_c_symbol_table():
    try:
        subprocess.run(
            [str(C_PROGRAM)],
            cwd=OUTPUT_DIR,
            check=True
        )

    except subprocess.CalledProcessError:
        print("C symbol table program failed.")
        raise

    except FileNotFoundError:
        print("Could not find symbol_table.exe.")
        raise

def load_symbol_table():
    symbol_positions = {}

    with open(SYMBOL_TABLE_FILE, "r", encoding="utf-8") as file:

        # Skip the header.
        next(file, None)

        for line in file:
            parts = line.rstrip("\n").split("\t", 2)

            if len(parts) != 3:
                continue

            position, category, lexeme = parts

            # (IDENTIFIER, "fps"): 0
            #   ^key               ^value
            symbol_positions[(category, lexeme)] = int(position)

    return symbol_positions

def write_pif(tokens, token_codes, symbol_positions):
    with open(PIF_FILE, "w", encoding="utf-8") as file:

        file.write("TokenCode\tSymbolTablePosition\tLineNumber\n")

        for kind, lexeme, line_number in tokens:

            if kind == "IDENTIFIER":
                code = IDENTIFIER_CODE
                position = symbol_positions[("IDENTIFIER", lexeme)]

            elif kind in ("NUMBER", "STRING", "CHARACTER", "BOOLEAN_CONSTANT"):
                code = CONSTANT_CODE
                position = symbol_positions[("CONSTANT", lexeme)]

            else:
                code = token_codes[lexeme]
                position = -1

            file.write(f"{code}\t{position}\t{line_number}\n")

def write_errors(errors):
    with open(ERRORS_FILE, "w", encoding="utf-8") as file:

        if not errors:
            file.write("No lexical errors found.\n")
            return

        for error in errors:
            file.write(error + "\n")

def print_tokens(tokens):
    table = PrettyTable()
    table.hrules = ALL
    table.field_names = ["Type", "Lexeme", "Line"]

    for kind, lexeme, line in tokens:
        table.add_row([kind, lexeme, line])

    print("\nTOKENS")
    print(table)

def print_symbol_table():
    table = PrettyTable()
    table.hrules = ALL
    table.field_names = ["Position", "Type", "Lexeme"]

    with open(SYMBOL_TABLE_FILE, "r") as file:
        next(file)  # Skip header

        for line in file:
            position, category, lexeme = line.strip().split("\t", 2)
            table.add_row([position, category, lexeme])

    print("\nSYMBOL TABLE")
    print(table)

def print_errors(errors):
    table = PrettyTable()
    table.hrules = ALL
    table.field_names = ["Error"]

    for error in errors:
        table.add_row([error])

    print("\nERRORS")

    if errors:
        print(table)
    else:
        print("No lexical errors found.")

def print_pif():
    table = PrettyTable()
    table.hrules = ALL
    table.field_names = ["Token Code", "Symbol Table Position", "Line Number"]

    with open(PIF_FILE, "r") as file:
        next(file)  # Skip header

        for line in file:
            token_code, position, line_number = line.strip().split("\t")
            table.add_row([token_code, position, line_number])

    print("\nPIF")
    print(table)

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    # load tokens
    token_codes = load_token_codes(TOKENS_FILE)

    # load source file
    with open(SOURCE_FILE, "r", encoding="utf-8") as file:
        source = file.read()

    # go through all of the text in the source file
    # and tokenize it -> return its list of tokens, and errors
    tokens, errors = tokenize(source, token_codes)

    # Check that all fixed tokens have codes.
    for kind, lexeme, line_number in tokens:

        if kind in ("KEYWORD", "OPERATOR", "SEPARATOR"):

            if lexeme not in token_codes:
                errors.append(
                    f"Line {line_number}: "
                    f"Token has no code in tokens.txt: {lexeme}"
                )

    # Generate symbol input for the C program.
    write_symbol_input(tokens)

    # Run the C BST implementation.
    run_c_symbol_table()

    # Read the positions assigned by the C program.
    symbol_positions = load_symbol_table()

    # Generate PIF and errors.
    write_pif(tokens, token_codes, symbol_positions)
    write_errors(errors)

    if errors:
        print("Skipping parsing because lexical errors were found.")
    else:
        from parser.parser_main import main as run_parser
        run_parser()

    # pretty print
    print_tokens(tokens)
    print_symbol_table()
    print_errors(errors)
    print_pif()


if __name__ == "__main__":
    main()
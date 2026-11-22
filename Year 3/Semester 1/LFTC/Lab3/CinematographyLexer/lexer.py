from prettytable import PrettyTable, ALL
import re
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SOURCE_FILE = BASE_DIR / "source.txt"
# SOURCE_FILE = BASE_DIR / "hasError.txt"
TOKENS_FILE = BASE_DIR / "tokens.txt"
SYMBOL_INPUT_FILE = BASE_DIR / "symbol_input.txt"
SYMBOL_TABLE_FILE = BASE_DIR / "symbol_table.txt"
PIF_FILE = BASE_DIR / "pif.txt"
ERRORS_FILE = BASE_DIR / "errors.txt"
C_PROGRAM = BASE_DIR / "symbol_table.exe"

# Token codes reserved for identifiers and constants.
IDENTIFIER_CODE = 100
CONSTANT_CODE = 101

TOKEN_SPECIFICATION = [
    # //<any character except new line> zero or more times
    ("COMMENT",    r"//[^\n]*"),

    # matches tabs, spaces, new lines one or more times
    ("WHITESPACE", r"[ \t\r\n]+"),

    # "<anything but " and new line>"
    ("STRING",     r'"[^"\n]*"'),

    # '<anything byt ' and new line>'
    ("CHARACTER",  r"'[^'\n]'"),

    # <any digit one or more times>
    ("NUMBER",     r"\d+"),

    # <any letter/underscore> followed by <any letter/underscore> zero or more times
    ("IDENTIFIER", r"[A-Za-z_][A-Za-z0-9_]*"),

    # any of the following operators
    ("OPERATOR",   r"==|!=|<=|>=|&&|\|\||[+\-*/%<>=]"),

    # any one of the following symbols
    ("SEPARATOR",  r"[(){};,. :]"),
]

# combine patterns by splitting them into python named capturing groups
# syntax: (?P<name>pattern)
# ( / ) - start/end group
# ?P<name> - name of the group
# pattern - rule for recognizing that group
# ---------------------------------------------
# .group() - actual text/pattern
# .lastgroup - token name
TOKEN_REGEX = re.compile(
    "|".join(
        f"(?P<{name}>{pattern})"
        for name, pattern in TOKEN_SPECIFICATION
    )
)

# read tokens.txt
def load_token_codes():

    #dictionary of tokens and codes
    token_codes = {}

    with open(TOKENS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # skip comment lines/empty lines
            if not line or line.startswith("#"):
                continue

            # token = "script", code = "4"
            token, code = line.rsplit(maxsplit=1)

            # map to dictionary
            token_codes[token] = int(code)

    return token_codes

# source = the text from source.txt
def tokenize(source, token_codes):
    # valid tokens
    tokens = []

    # lexical errors
    errors = []

    # position tracking
    line_number = 1
    position = 0

    # loop through all the characters in the source code
    while position < len(source):
        ### ERROR DETECTION

        # 1. Detect identifiers that start with a digit, such as 2fps.
        invalid_identifier = re.match(
            r"\d+[A-Za-z_][A-Za-z0-9_]*",
            source[position:]
        )

        # if an invalid token was found - record it in the errors file
        if invalid_identifier:
            lexeme = invalid_identifier.group()

            errors.append(
                f"Line {line_number}: invalid identifier {lexeme!r}; "
                "identifiers cannot start with a digit"
            )

            # increase the position with the length of the invalid token
            position += len(lexeme)
            continue

        # 2. Detect a string that has no closing double quote.
        if source[position] == '"':
            # search for the first \n character, staring from current position
            end_of_line = source.find("\n", position)

            # if there is no \n, then we are at the end of the source code
            # so end_of_line = length of the source code
            if end_of_line == -1:
                end_of_line = len(source)

            # find the position of the closing ", starting from
            # the position of first " + 1
            # all the way through to the end of the current line
            closing_quote = source.find('"', position + 1, end_of_line)

            # if closing quotes do not exist, add this to the errors file
            if closing_quote == -1:
                errors.append(
                    f"Line {line_number}: unterminated string literal"
                )

                position = end_of_line
                continue

        # 3. Detect invalid character literals such as 'AB'.
        if source[position] == "'":
            end_of_line = source.find("\n", position)

            if end_of_line == -1:
                end_of_line = len(source)

            closing_quote = source.find("'", position + 1, end_of_line)

            # if a closing ' was found ...
            if closing_quote != -1:
                # grab the invalid character with '' included
                lexeme = source[position:closing_quote + 1]

                if len(lexeme) != 3:
                    errors.append(
                        f"Line {line_number}: invalid character literal {lexeme!r}; "
                        "exactly one character is required"
                    )

                    position = closing_quote + 1
                    continue
            else:
                errors.append(
                    f"Line {line_number}: unterminated char literal"
                )

                position = end_of_line
                continue

        ### TOKEN HAS NO ERROR

        # Check if it exists
        # match the characters in the file starting at position to the
        # existing regexes
        # so, for "fps = 30;"
        # match() recognizes f, p, s as an identifier
        # match() tries to continue with = as an identifier
        # it cannot, so it matches it to the next thing: operator
        # then it tries to match() 3 with the operator regex
        # it cannot, so it matches it with number, along with 0
        # finally it tries to match ; with the number regex, but it cant
        # so it matches it with the separator regex
        match = TOKEN_REGEX.match(source, position)

        # if the match could not be made to anything, add to errors
        if match is None:
            char = source[position]

            errors.append(
                f"Line {line_number}: invalid character {char!r}"
            )

            position += 1
            continue

        # the type of the regex matched: NUMBER, OPERATOR, etc.
        kind = match.lastgroup

        # the actual text matched
        lexeme = match.group()

        # increase the number of current line with the number of \n
        if kind == "WHITESPACE":
            line_number += lexeme.count("\n")

        # if the line is a comment, ignore it
        elif kind == "COMMENT":
            pass

        # add to the tokens list
        elif kind == "IDENTIFIER":
            if lexeme in token_codes:
                # This word is a reserved keyword
                tokens.append(("KEYWORD", lexeme, line_number))
            else:
                # This word is a normal identifier
                tokens.append(("IDENTIFIER", lexeme, line_number))
        else:
            # Add numbers, strings, characters,
            # operators and separators to the token list.
            tokens.append((kind, lexeme, line_number))

        position = match.end()

    return tokens, errors

def write_symbol_input(tokens):
    with open(SYMBOL_INPUT_FILE, "w", encoding="utf-8") as file:
        for kind, lexeme, line_number in tokens:
            if kind == "IDENTIFIER":
                file.write(f"IDENTIFIER\t{lexeme}\n")

            elif kind in ("NUMBER", "STRING", "CHARACTER"):
                file.write(f"CONSTANT\t{lexeme}\n")

# run the .c file
def run_c_symbol_table():
    if not C_PROGRAM.exists():
        raise FileNotFoundError(
            "symbol_table.exe was not found. "
            "Compile symbol_table.c first."
        )

    subprocess.run(
        [
            str(C_PROGRAM),
            str(SYMBOL_INPUT_FILE),
            str(SYMBOL_TABLE_FILE),
        ],
        check=True,
        cwd=BASE_DIR,
    )


def load_symbol_table():
    positions = {}

    with open(SYMBOL_TABLE_FILE, "r", encoding="utf-8") as file:
        next(file, None)  # Skip the header.

        for line in file:
            position, kind, lexeme = line.rstrip("\r\n").split("\t", 2)
            positions[(kind, lexeme)] = int(position)

    return positions

def write_pif(tokens, token_codes, symbol_positions):
    with open(PIF_FILE, "w", encoding="utf-8") as file:
        for kind, lexeme, line_number in tokens:
            if kind == "IDENTIFIER":
                code = IDENTIFIER_CODE
                position = symbol_positions[("IDENTIFIER", lexeme)]

            elif kind in ("NUMBER", "STRING", "CHARACTER"):
                code = CONSTANT_CODE
                position = symbol_positions[("CONSTANT", lexeme)]

            else:
                code = token_codes[lexeme]
                position = -1

            file.write(f"{code}\t{position}\t{line_number}\n")

def write_errors(errors):
    with open(ERRORS_FILE, "w", encoding="utf-8") as file:
        if errors:
            file.write("\n".join(errors) + "\n")
        else:
            file.write("No lexical errors found.\n")


def main():
    token_codes = load_token_codes()

    with open(SOURCE_FILE, "r", encoding="utf-8") as file:
        source = file.read()

    tokens, errors = tokenize(source, token_codes)

    # Report any recognized token absent from tokens.txt.
    for kind, lexeme, line_number in tokens:
        if (
            kind not in ("IDENTIFIER", "NUMBER", "STRING", "CHARACTER")
            and lexeme not in token_codes
        ):
            errors.append(
                f"Line {line_number}: token {lexeme!r} "
                "has no code in tokens.txt"
            )

    # Do not build an incomplete PIF if the token definitions
    # are missing codes.
    if any("has no code in tokens.txt" in error for error in errors):
        write_errors(errors)
        print("Fix tokens.txt before generating the PIF.")
        return

    write_symbol_input(tokens)
    run_c_symbol_table()

    symbol_positions = load_symbol_table()
    # print([token for token in tokens if token[1] == "nomemory"])
    write_pif(tokens, token_codes, symbol_positions)
    write_errors(errors)

    print("Lexical analysis finished.")
    print(f"PIF: {PIF_FILE.name}")
    print(f"Symbol Table: {SYMBOL_TABLE_FILE.name}")
    print(f"Errors: {ERRORS_FILE.name}")

    if errors:
        print(f"Found {len(errors)} lexical error(s).")
    else:
        print("No lexical errors found.")

    print_symbol_table()
    print_pif()
    print_errors(errors)


def print_pif():
    """Display the Program Internal Form in the console."""
    table = PrettyTable(hrules=ALL)
    table.field_names = ["Token Code", "Symbol Table Position", "Line"]

    with open(PIF_FILE, "r", encoding="utf-8") as file:

        for line in file:
            parts = line.strip().split()

            if len(parts) == 3:
                table.add_row(parts)

    print("\nPROGRAM INTERNAL FORM (PIF)")
    print(table)


def print_symbol_table():
    """Display the Symbol Table produced by the C program."""
    table = PrettyTable(hrules=ALL)
    table.field_names = ["Position", "Type", "Lexeme"]

    with open(SYMBOL_TABLE_FILE, "r", encoding="utf-8") as file:
        next(file, None)  # Skip the header in the file

        for line in file:
            parts = line.rstrip("\n").split("\t")

            if len(parts) == 3:
                table.add_row(parts)

    print("\nSYMBOL TABLE (ST)")
    print(table)


def print_errors(errors):
    """Display lexical errors in the console."""
    table = PrettyTable(hrules=ALL)
    table.field_names = ["Error"]

    if errors:
        for error in errors:
            table.add_row([error])
    else:
        table.add_row(["No lexical errors found."])

    print("\nLEXICAL ERRORS")
    print(table)


if __name__ == "__main__":
    main()


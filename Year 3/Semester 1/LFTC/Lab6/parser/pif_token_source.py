
from pathlib import Path
import re

from antlr4.Token import CommonToken
from antlr4 import Token

from .generated.CinematographyLexer import CinematographyLexer


BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

PIF_FILE = OUTPUT_DIR / "pif.txt"
SYMBOL_TABLE_FILE = OUTPUT_DIR / "symbol_table.txt"
TOKENS_FILE = BASE_DIR / "tokens.txt"

IDENTIFIER_CODE = 100
CONSTANT_CODE = 101


# Load the fixed token codes from tokens.txt.
def load_token_codes():
    token_codes = {}

    with open(TOKENS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            lexeme, code = line.rsplit(maxsplit=1)
            token_codes[lexeme] = int(code)

    return token_codes


# Recover lexemes using their symbol table positions.
def load_symbol_table():
    symbols = {}

    with open(SYMBOL_TABLE_FILE, "r", encoding="utf-8") as file:
        next(file, None)  # Skip the header.

        for line in file:
            position, kind, lexeme = line.rstrip("\r\n").split("\t", 2)
            symbols[int(position)] = (kind, lexeme)

    return symbols


# Map each fixed lexeme to its ANTLR token type.
TOKEN_NAMES = {
    "int": "INT",
    "char": "CHAR",
    "script": "SCRIPT",
    "bool": "BOOL",
    "new": "NEW",
    "film": "FILM",
    "onScreen": "ONSCREEN",
    "true": "TRUE",
    "false": "FALSE",
    "check": "CHECK",
    "else": "ELSE",
    "for": "FOR",
    "do": "DO",
    "while": "WHILE",
    "record": "RECORD",
    "reel": "REEL",
    "return": "RETURN",
    "add": "ADD",
    "cut": "CUT",
    "get": "GET",
    "overwrite": "OVERWRITE",
    "nomemory": "NOMEMORY",

    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLY",
    "/": "DIVIDE",
    "%": "MODULO",
    "<": "LESS",
    "<=": "LESS_EQUAL",
    ">": "GREATER",
    ">=": "GREATER_EQUAL",
    "==": "EQUAL",
    "!=": "NOT_EQUAL",
    "=": "ASSIGN",
    "&&": "AND",
    "||": "OR",

    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE",
    "}": "RBRACE",
    ":": "COLON",
    ";": "SEMI",
    ",": "COMMA",
    ".": "DOT",
}


def classify_constant(lexeme):
    if lexeme == "true":
        return CinematographyLexer.TRUE

    if lexeme == "false":
        return CinematographyLexer.FALSE

    if re.fullmatch(r"0|[1-9][0-9]*", lexeme):
        return CinematographyLexer.NUMBER

    if (
        len(lexeme) >= 2
        and lexeme.startswith('"')
        and lexeme.endswith('"')
    ):
        return CinematographyLexer.STRING

    if (
        len(lexeme) == 3
        and lexeme.startswith("'")
        and lexeme.endswith("'")
    ):
        return CinematographyLexer.CHARACTER

    raise ValueError(f"Unknown constant in symbol table: {lexeme!r}")


def create_tokens():
    token_codes = load_token_codes()
    symbols = load_symbol_table()

    # Convert token codes back to their lexemes.
    code_to_lexeme = {
        code: lexeme
        for lexeme, code in token_codes.items()
    }

    tokens = []

    with open(PIF_FILE, "r", encoding="utf-8") as file:
        next(file, None)  # Skip header.

        for line in file:
            parts = line.strip().split("\t")

            if len(parts) != 3:
                raise ValueError(f"Invalid PIF line: {line!r}")

            code = int(parts[0])
            position = int(parts[1])
            line_number = int(parts[2])

            # Identifier or constant: recover it from the symbol table.
            if code in (IDENTIFIER_CODE, CONSTANT_CODE):
                if position not in symbols:
                    raise ValueError(
                        f"Symbol table position {position} does not exist."
                    )

                kind, lexeme = symbols[position]

                if code == IDENTIFIER_CODE:
                    if lexeme in ("true", "false"):
                        token_type = classify_constant(lexeme)
                    else:
                        token_type = CinematographyLexer.IDENTIFIER

                else:
                    token_type = classify_constant(lexeme)

            # Keyword, operator, or separator: recover from tokens.txt.
            else:
                if code not in code_to_lexeme:
                    raise ValueError(f"Unknown token code: {code}")

                lexeme = code_to_lexeme[code]

                if lexeme not in TOKEN_NAMES:
                    raise ValueError(
                        f"No ANTLR token mapping for {lexeme!r}"
                    )

                token_name = TOKEN_NAMES[lexeme]
                token_type = getattr(CinematographyLexer, token_name)

            token = CommonToken(type=token_type)
            token.text = lexeme
            token.line = line_number
            token.column = 0

            tokens.append(token)

    # Add EOF so ANTLR knows the input has ended.
    eof = CommonToken(type=Token.EOF)
    eof.text = "<EOF>"
    eof.line = tokens[-1].line if tokens else 1
    eof.column = 0
    tokens.append(eof)

    return tokens

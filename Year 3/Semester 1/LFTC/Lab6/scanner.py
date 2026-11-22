import re

from finite_automata import AUTOMATA, is_id_start, is_digit

# Regular expressions are used only for comments,
# whitespace, operators, and separators.
TOKEN_SPECIFICATION = [
    ("COMMENT", r"//[^\n]*"),
    ("WHITESPACE", r"[ \t\r\n]+"),
    ("OPERATOR", r"==|!=|<=|>=|&&|\|\||[+\-*/%<>=]"),
    ("SEPARATOR", r"[(){};,. :]"),
]

TOKEN_REGEX = re.compile(
    "|".join(
        f"(?P<{name}>{pattern})"
        for name, pattern in TOKEN_SPECIFICATION
    )
)


def load_token_codes(file_path):
    token_codes = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            # split by whitespaces
            parts = line.rsplit(maxsplit=1)

            # each keyword/etc, has a code that is mapped to it
            if len(parts) == 2:
                lexeme, code = parts
                token_codes[lexeme] = int(code)

    return token_codes


def tokenize(source, token_codes):
    tokens = []
    errors = []

    line_number = 1
    position = 0

    while position < len(source):

        current_char = source[position]

        # 1. Strings

        if current_char == '"':
            line_end = source.find("\n", position)

            if line_end == -1:
                line_end = len(source)

            closing_quote = source.find('"', position + 1)

            if closing_quote == -1 or closing_quote >= line_end:
                errors.append(
                    f"Line {line_number}: Unterminated string constant"
                )

                position = line_end
                continue

            lexeme = source[position:closing_quote + 1]

            # check automata
            if AUTOMATA["STRING"].accepts(lexeme):
                tokens.append(
                    ("STRING", lexeme, line_number)
                )
            else:
                errors.append(
                    f"Line {line_number}: Invalid string constant: {lexeme}"
                )

            position = closing_quote + 1
            continue

        # 2. Character constants

        if current_char == "'":
            line_end = source.find("\n", position)

            if line_end == -1:
                line_end = len(source)

            closing_quote = source.find("'", position + 1)

            if closing_quote == -1 or closing_quote >= line_end:
                errors.append(
                    f"Line {line_number}: Unterminated character constant"
                )

                position = line_end
                continue

            lexeme = source[position:closing_quote + 1]

            if AUTOMATA["CHARACTER"].accepts(lexeme):
                tokens.append(
                    ("CHARACTER", lexeme, line_number)
                )
            else:
                errors.append(
                    f"Line {line_number}: Invalid character constant: {lexeme}"
                )

            position = closing_quote + 1
            continue

        # 3. Identifiers, keywords, booleans and integers

        # if the character we're at can be an identifier, or a number ...
        if is_id_start(current_char) or is_digit(current_char):

            # Read the complete sequence of letters, digits and underscores.
            # The automata will decide whether it is valid.
            end = position

            while end < len(source):
                char = source[end]

                if (
                    char.isascii()
                    and (char.isalnum() or char == "_")
                ):
                    end += 1
                else:
                    break

            lexeme = source[position:end]

            # Starts with a letter or underscore => IDENTIFIER
            if is_id_start(current_char):

                if not AUTOMATA["IDENTIFIER"].accepts(lexeme):
                    errors.append(
                        f"Line {line_number}: Invalid identifier: {lexeme}"
                    )

                elif AUTOMATA["BOOLEAN"].accepts(lexeme):
                    tokens.append(
                        ("BOOLEAN_CONSTANT", lexeme, line_number)
                    )

                elif lexeme in token_codes:
                    tokens.append(
                        ("KEYWORD", lexeme, line_number)
                    )

                else:
                    tokens.append(
                        ("IDENTIFIER", lexeme, line_number)
                    )

            # Starts with a digit => NUMBER / invalid IDENTIFIER
            else:

                # A sequence such as 123abc or 2_name is invalid.
                if any(
                    char.isascii() and (char.isalpha() or char == "_")
                    for char in lexeme
                ):
                    errors.append(
                        f"Line {line_number}: Invalid identifier: {lexeme}"
                    )

                elif AUTOMATA["INTEGER"].accepts(lexeme):
                    tokens.append(
                        ("NUMBER", lexeme, line_number)
                    )

                else:
                    errors.append(
                        f"Line {line_number}: Invalid integer constant: {lexeme}"
                    )

            position = end
            continue

        # 4. Comments, whitespace, operators and separators

        match = TOKEN_REGEX.match(source, position)

        if match:
            # ex: OPERATOR, COMMENT, etc
            kind = match.lastgroup
            # actual value
            lexeme = match.group()

            if kind == "WHITESPACE":
                line_number += lexeme.count("\n")

            elif kind == "COMMENT":
                pass

            else:
                tokens.append(
                    (kind, lexeme, line_number)
                )

            position = match.end()
            continue

        # 5. Invalid character

        errors.append(
            f"Line {line_number}: Invalid character: {current_char}"
        )

        position += 1

    return tokens, errors
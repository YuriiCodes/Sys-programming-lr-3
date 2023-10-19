import re


class AssemblerLexerFinalV2:
    def __init__(self):
        self.token_patterns = [
            ("NUMBER_FLOAT", r"^\d*\.\d+$"),
            ("NUMBER_DEC", r"^\d+$"),
            ("NUMBER_HEX", r"^0[xX][0-9a-fA-F]+$"),
            ("STRING_CONST", r'^".*"$'),
            ("CHAR_CONST", r"^'.*'$"),
            ("PREPROCESSOR", r"^#[a-zA-Z_]\w*$"),
            ("COMMENT", r"^;.*$"),
            ("RESERVED_WORD", r"^(MOV|ADD|SUB|DIV|MUL)$"),
            ("OPERATOR", r"^(AND|OR|XOR)$"),
            ("SEPARATOR", r"^[\.,;:\[\]{}()]$"),
            ("IDENTIFIER", r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
        ]

    def tokenize(self, text):
        tokens = []
        # Adjusting the splitting logic to handle comments as a whole
        words = re.findall(r';.*|\d*\.\d+|\w+|[\.,;:\[\]{}()]', text)

        for word in words:
            token_type = None

            for token_name, pattern in self.token_patterns:
                if re.match(pattern, word):
                    token_type = token_name
                    break

            # If token type is not identified, mark it as an error
            if token_type is None:
                tokens.append((word, "ERROR"))
            else:
                tokens.append((word, token_type))

        return tokens

sample_code = """
MOV AX, 1
ADD BX, AX
SUB CX, 0x10
; This is a comment
#directive
MOV AL, 'a'
DIV DX, 3.14
"""

# Let's test the updated lexer
lexer_final_v2 = AssemblerLexerFinalV2()
tokens_final_v2 = lexer_final_v2.tokenize(sample_code)
for token in tokens_final_v2:
    print(token)



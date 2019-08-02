import sys
from lexer import lexer
from parser import parser

if len(sys.argv) > 2:
    raise Exception("Got multiple input arguments")

expression = sys.argv[1] if len(sys.argv) == 2 else "(1 + 2) + 3 * 4"

tokens = list(lexer.lex(expression))
print(f"Got tokens: {tokens}")
parsed = parser.parse(iter(tokens))
value = parsed.eval()
print(f"Result of {expression}:")
print(value)

from lexer import lexer
from parser import parser
expression = "1 + 2 + 3 * 4"
tokens = lexer.lex(expression)
parsed = parser.parse(tokens)
value = parsed.eval()
print(f"Result of {expression}:")
print(value)

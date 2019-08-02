from rply import ParserGenerator
from ast import *
pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)

@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    print("Matched to NUMBER token:", p[0])
    return Number(int(p[0].getstr()))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    print("Matched to parentheses", p)
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
def expression_binop(p):
    print("Matched to binary operation", p)
    left = p[0]  # `ast.Number type`
    right = p[2]  # `ast.Number type`
    operation_token_type = p[1].gettokentype()
    if operation_token_type == 'PLUS':
        return Add(left, right)
    elif operation_token_type == 'MINUS':
        return Sub(left, right)
    elif operation_token_type == 'MUL':
        return Mul(left, right)
    elif operation_token_type == 'DIV':
        return Div(left, right)
    else:
        raise AssertionError(f'No matching operation for {operation_token_type}')

parser = pg.build()

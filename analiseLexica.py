import ply.lex as lex
reserved = {
    'using' : 'USING',
    'Bool': 'BOOL',
    'class': 'CLASS',
    'else': 'ELSE',
    'false': 'FALSE',
    'true': 'TRUE',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'if': 'IF',
    'in': 'IN',
    'is': 'IS',
    'namespace': 'NAMESPACE',
    'new': 'NEW',
    'null': 'NULL',
    'object': 'OBJECT',
    'public': 'PUBLIC',
    'return': 'RETURN',
    'sizeof': 'SIZEOF',
    'static': 'STATIC',
    'this': 'THIS',
    'while': 'WHILE',
    'int': 'INT',
    'string': 'STRING'
}
tokens = ['newLine',
          "SOMA", "SUB", "DIV", "INCREMENTO", "DECREMENTO", "MUL", "ATRIBUICAO",
          "IGUAL", "DIFERENTE", "MAIOR", "MENOR", "MAIOR_IGUAL", "MENOR_IGUAL",
          "AND", "OR", "NOT", "PONTO", "PONTO_VIRGULA", "PARENTESE_L", "PARENTESE_R",
          "CHAVE_L", "CHAVE_R",  "ID",'VIRGULA','COMMENT', 'BIT_AND', 'BIT_OR','BIT_NOT', 'XOR'] + list(reserved.values())
t_ignore = ' \t'
t_CHAVE_L = r'{'
t_CHAVE_R = r'}'
t_VIRGULA = r','
t_PONTO = r'\.'
t_ATRIBUICAO = r'='
t_PONTO_VIRGULA = r';'
t_PARENTESE_L = r'\('
t_PARENTESE_R = r'\)'
#operador bit a bit 
t_BIT_AND = r'&'
t_BIT_OR = r'\|'
t_BIT_NOT = r'~'
t_XOR = r'\^'
# operadores logico
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
# operadores relacionais
t_IGUAL = r'=='
t_DIFERENTE = r'=!'
t_MAIOR = r'>'
t_MENOR = r'<'
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
# operadores aritimeticos
t_SOMA = r'\+'
t_SUB = r'-'
t_DIV = r'/'
t_MUL = r'\*'
t_INCREMENTO = '\+\+'
t_DECREMENTO = '--'
def t_INT (t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t
def t_COMMENT (t):
    r'(//.*)|(/\*(.|\n)*?\*/)'
    pass
def t_STRING(t):
    r'\"([^\\]|(\\.))*?\"'
    return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    #print("Token inválido!!!!! '%s'" % t.value[0])
    print("Token inválido!!!!! '", t.value[0], "'")

    t.lexer.skip(1)
lexer = lex.lex()
lexer.input("15Abstract as base Bool break byte case Catch char checked class Const continue decimal default Delegate dodouble else Enum event explicit extern false finally fixed float for foreach goto if implicit in int interface internal is lock long namespace new null object operator out override params private protected public readonly ref return sbyte sealed short sizeof stackalloc static string struct this throw")
"""for tok in lexer:
    print(tok.type, tok.lineno, tok.value, tok.lexpos)
lexer.input("as{}(()(+---*%++++>=<===<>=!&&||!|<<>>&^~..;;1 2 23 /*1110*/Abstract@:\'\n\"rei\nnan\"\'@\''\n'' ' '@'_math/*eus*/ \"\\\\n\"")
for tok in lexer:
    print(tok.type, tok.lineno, tok.value, tok.lexpos)"""

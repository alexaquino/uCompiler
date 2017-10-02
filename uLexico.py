#------------------------------------------------------------------------------#
#!/usr/bin/env python                                                          #
# -*- encoding: utf-8 -*-                                                      #
#                                                                              #
# 14 AGOSTO 2017                                                               #
# Trabalho I - Compiladores - Analisador Lexico - PASCAL                       #
# Alex Aquino de Claudia Medeiros                                              #
#                                                                              #
# Referencias:                                                                 #
#   PLY (Python Lex-Yacc): http://www.dabeaz.com/ply/                          #
#                          http://www.dabeaz.com/ply/PLYTalk.pdf               #
#   Pascal - Quick Guide: https://www.tutorialspoint.com/pascal/index.htm      #
#   Python documentation: https://docs.python.org/3/index.html                 #
#   re - Regular expression: https://docs.python.org/3/library/re.html         #
#------------------------------------------------------------------------------#

# Modulo - lex (scanner)
import ply.lex as lex
import re

# Reserved words
reserved = (
    'ARRAY', 'BEGIN', 'CASE', 'CONST', 'DIV', 'DO', 'DOWNTO','ELSE', 'END', 'FILE',
    'FOR', 'FUNCTION', 'GOTO', 'IF', 'IN', 'LABEL', 'NIL', 'NOT', 'OF', 'PACKED',
    'AND', 'OR', 'RECORD', 'REPEAT', 'SET', 'THEN', 'TO', 'TYPE', 'UNTIL', 'VAR',
    'PROCEDURE', 'PROGRAM', 'WHILE', 'WITH', 'MOD',
) # 35

# Tokens
tokens = reserved + (
    # Arithmetic Operators ( +  -  *  / )
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    # Relational Operators ( :=  <  <=  >  >=  =  <> )
    'EQUALS', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NEQ',
    # Delimeters ( (  )  [  ]  .  ,  ;  : )
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'POINT', 'COMMA', 'SEMICOLON', 'COLON',
    # Literals (integer, real, number, string, boolean, identifier)
    'INTEGER', 'REAL', 'NUMBER', 'STRING', 'BOOLEAN', 'ID',
)

# Arithmetic Operators ( +  -  *  /  % )
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Relational Operators ( :=  <  <=  >  >=  =  <> )
t_EQUALS = r':='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'='
t_NEQ = r'<>'

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_POINT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'

# Literals
def t_INTEGER(t):
    r'INTEGER'
    return t

def t_REAL(t):
    r'REAL'
    return t

def t_STRING(t):
    r'STRING'
    return t

def t_BOOLEAN(t):
    r'BOOLEAN'
    return t

def t_NUMBER(t):
    r'[-+]?\d*\.\d+ | \d+'
    return t

# Reserved words
def t_ARRAY(t):
    r'ARRAY'
    return t

def t_BEGIN(t):
    r'BEGIN'
    return t

def t_CASE(t):
    r'CASE'
    return t

def t_CONST(t):
    r'CONST'
    return t

def t_DIV(t):
    r'DIV'
    return t

def t_DO(t):
    r'DO'
    return t

def t_DOWNTO(t):
    r'DOWNTO'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_END(t):
    r'END'
    return t

def t_FILE(t):
    r'FILE'
    return t

def t_FOR(t):
    r'FOR'
    return t

def t_FUNCTION(t):
    r'FUNCTION'
    return t

def t_GOTO(t):
    r'GOTO'
    return t

def t_IF(t):
    r'IF'
    return t

def t_IN(t):
    r'IN'
    return t

def t_LABEL(t):
    r'LABEL'
    return t

def t_NIL(t):
    r'NIL'
    return t

def t_NOT(t):
    r'NOT'
    return t

def t_OF(t):
    r'OF'
    return t

def t_PACKED(t):
    r'PACKED'
    return t

def t_PROCEDURE(t):
    r'PROCEDURE'
    return t

def t_PROGRAM(t):
    r'PROGRAM'
    return t

def t_RECORD(t):
    r'RECORD'
    return t

def t_REPEAT(t):
    r'REPEAT'
    return t

def t_SET(t):
    r'SET'
    return t

def t_THEN(t):
    r'THEN'
    return t

def t_TO(t):
    r'TO'
    return t

def t_TYPE(t):
    r'TYPE'
    return t

def t_UNTIL(t):
    r'UNTIL'
    return t

def t_VAR(t):
    r'VAR'
    return t

def t_WHILE(t):
    r'WHILE'
    return t

def t_WITH(t):
    r'WITH'
    return t

def t_MOD(t):
    r'MOD'
    return t

def t_AND(t):
    r'AND'
    return t

def t_OR(t):
    r'OR'
    return t

def t_ID(t):
    r'[A-Za-z][\w_]*'
    if t.value.upper() in tokens:
        t.value = t.value.upper()
        t.type = t.value
    return t
#35

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_ignore = ' \t\x0c'

# COMMENTS {* ... *}  { ... }
def t_COMMENTS(t):
    r'({\*(.|\n)*?\*}) | ({(.)*?})'
    t.lexer.lineno += t.value.count('\n')

# ERROR
def t_error(t):
    print("Illegal character: '%s'" % t.value[0])
    print("   -> Line: '%s'" % t.lexer.lineno)
    t.lexer.skip(1)


# ------------------------------------------------------------------------------
def uLexico(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

# Build the lexer
lexer = lex.lex()
# ------------------------------------------------------------------------------

if __name__ == '__main__':

    f = open('pascal_6.pas')
    data = f.read()
    f.close()
    # Build lexer and try on
    uLexico(data, lexer)

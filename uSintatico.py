#------------------------------------------------------------------------------#
# !/usr/bin/env python                                                         #
# -*- encoding: utf-8 -*-                                                      #
#                                                                              #
# 23 SETEMBRO 2017                                                             #
# Trabalho II - Compiladores - Analisador Sintatico - PASCAL                   #
# Alex Aquino de Claudia Medeiros                                              #
#                                                                              #
# Referencias:                                                                 #
#   PLY (Python Lex-Yacc): http://www.dabeaz.com/ply/                          #
#                          http://www.dabeaz.com/ply/PLYTalk.pdf               #
#   Pascal ISO 7185 : 1990                                                     #
#   Pascal - Quick Guide: https://www.tutorialspoint.com/pascal/index.htm      #
#   Python documentation: https://docs.python.org/3/index.html                 #
#   Regular expression  : https://docs.python.org/3/library/re.html            #
#------------------------------------------------------------------------------#

import ply.yacc as yacc
# Get the token map from the lexer. This is required.
from uLexico import tokens

TEST_ERROR = 1

# PRECEDENCE
precedence = (
    # Relational Operators ( = )
    ('right', 'EQ'),
    # Relational Operators ( := )
    ('right', 'EQUALS'),
    # Relational Operators ( <> )
    ('left', 'NEQ'),
    # Relational Operators ( <  <=  > )
    ('left', 'LT', 'LE', 'GT', 'GE'),
    # Arithmetic Operators ( +  - )
    ('left', 'PLUS', 'MINUS'),
    # Arithmetic Operators ( *  / )
    ('left', 'TIMES', 'DIVIDE'),
    # Delimeters ( (  ) )
    ('left', 'LPAREN', 'RPAREN'),
)

# GRAMMAR RULES
# PROGRAM
def p_program(p):
    'program : PROGRAM ID SEMICOLON block POINT'
    pass

# BLOCK
# block = label-declaration-part constant-definition-part type-definition-part
#         variable-declaration-part procedure-and-function-declaration-part
#         statement-part
def p_block(p):
    'block : labelDecl constDecl varDecl BEGIN procDecl functDecl statement END'
    pass

#LABEL
#label-declaration-part = [ `label' label { `,' label } ` ;' ]
def p_labelDecl(p):
    'labelDecl : LABEL NUMBER SEMICOLON'
    pass

def p_labelDeclEmpty(p):
    'labelDecl : empty'
    pass

# CONST
#constant-definition-part = [ 'const' constant-definition ';' { constant-definition ';' } ]
def p_constDeclEmpty(p):
    'constDecl : empty'
    pass

def p_constDecl(p):
    'constDecl : CONST constAssignmentList SEMICOLON'
    pass

def p_constAssignmentList_1(p):
    'constAssignmentList : ID EQ INTEGER'
    pass

def p_constAssignmentList_2(p):
    'constAssignmentList : ID EQ REAL'
    pass

def p_constAssignmentList_3(p):
    'constAssignmentList : ID EQ STRING'
    pass

def p_constAssignmentList_4(p):
    'constAssignmentList : ID EQ NUMBER'
    pass

def p_constAssignmentList_5(p):
    'constAssignmentList : ID EQ BOOLEAN'
    pass

# TYPE
# type-definition-part = [ 'type' type-definition ';' { type-definition ';' } ]
def p_typeDefinitionEmpty(p):
    'typeDefinition : empty'
    pass

def p_typeDefinition_1(p):
    'typeDefinition : INTEGER'
    pass

def p_typeDefinition_2(p):
    'typeDefinition : REAL'
    pass

def p_typeDefinition_3(p):
    'typeDefinition : STRING'
    pass

def p_typeDefinition_4(p):
    'typeDefinition : BOOLEAN'
    pass

# VAR
# variable-declaration-part = [ `var' variable-declaration ` ;' { variable-declaration `;' ~ ] .
def p_varDeclEmpty(p):
    'varDecl : empty'
    pass

def p_varDecl(p):
    'varDecl : VAR identList COLON typeDefinition SEMICOLON identList_2'
    pass

def p_identList_1(p):
    'identList : ID'
    pass

def p_identList_2(p):
    'identList : identList COMMA ID'
    pass

def p_identList_3(p):
    'identList_2 : empty'
    pass

def p_identList_4(p):
    'identList_2 : identList COLON typeDefinition SEMICOLON identList_2'
    pass

# PROCEDURE
# procedure-and-function-declaration-part = { (procedure-declaration | function-declaration) ';'}
def p_procDecl1(p):
    'procDecl : PROCEDURE ID LPAREN parameters RPAREN SEMICOLON block SEMICOLON'
    pass

def p_procDeclEmpty(p):
    'procDecl : empty'
    pass

# FUNCTION
# procedure-and-function-declaration-part = { (procedure-declaration | function-declaration) ';'}
def p_functDeclEmpty(p):
    'functDecl : empty'
    pass

def p_functDecl1(p):
    'functDecl : FUNCTION ID LPAREN parameters RPAREN COLON typeDefinition SEMICOLON block SEMICOLON'
    pass

# PARAMETERS (ID : TYPE; ID : TYPE; ID : TYPE; ...)  or (ID, ID, ID... : TYPE)
def p_parametersEmpty(p):
    'parameterList : empty'
    pass

def p_parameters(p):
    'parameters : parameterList'
    pass

def p_parameterList_1(p):
    'parameterList : parameterList SEMICOLON parameter'
    pass

def p_parameterList_2(p):
    'parameterList : parameter'
    pass

def p_parameter_1(p):
    'parameter : ID COLON typeDefinition'
    pass

def p_parameter_2(p):
    'parameter : ID COMMA parameter'
    pass

def p_parameter_3(p):
    'parameter : COLON typeDefinition'
    pass

# STATEMENT
def p_statementEmpty(p):
    'statement : empty'
    pass

def p_statement_1(p):
    'statement : statement ID EQUALS expression SEMICOLON'
    pass

def p_statement_2(p):
    'statement : BEGIN statementList END'
    pass

def p_statement_3(p):
    'statement : statement IF condition THEN statement'
    pass

def p_statement_4(p):
    'statement : statement IF condition THEN statement ELSE statement'
    pass

def p_statement_5(p):
    'statement : WHILE condition DO statement'
    pass

# STATEMENT - List
def p_statementList_1(p):
    'statementList : statement'
    pass

def p_statementList_2(p):
    'statementList : statementList SEMICOLON statement'
    pass

# STATEMENT - condition
def p_condition(p):
    'condition : expression relation expression'
    pass

# STATEMENT - relation
def p_relation_1(p):
    'relation : EQUALS'
    pass

def p_relation_2(p):
    'relation : LT'
    pass

def p_relation_3(p):
    'relation : LE'
    pass

def p_relation_4(p):
    'relation : GT'
    pass

def p_relation_5(p):
    'relation : GE'
    pass

def p_relation_6(p):
    'relation : EQ'
    pass

def p_relation_7(p):
    'relation : NEQ'
    pass

# STATEMENT - expression
def p_expression_1(p):
    'expression : term'
    pass

def p_expression_2(p):
    'expression : addOperator term'
    pass

def p_expression_3(p):
    'expression : expression addOperator term'
    pass

def p_addOperator_1(p):
    'addOperator : PLUS'
    pass

def p_addOperator_2(p):
    'addOperator : MINUS'
    pass

def p_term_1(p):
    'term : factor'
    pass

def p_term_2(p):
    'term : term multOperator factor'
    pass

def p_multOperator_1(p):
    'multOperator : TIMES'
    pass

def p_multOperator_2(p):
    'multOperator : DIVIDE'
    pass

def p_factor_1(p):
    'factor : ID'
    pass

def p_factor_2(p):
    'factor : REAL'
    pass

def p_factor_3(p):
    'factor : INTEGER'
    pass

def p_factor_4(p):
    'factor : LPAREN expression RPAREN'
    pass

def p_factor_5(p):
    'factor : NUMBER'
    pass

def p_factor_6(p):
    'factor : BOOLEAN'
    pass

def p_empty(p):
    'empty :'
    pass

# ERROS
def p_error(p):
    if TEST_ERROR:
        if p is not None:
            print("Context Error: '%s'" % (str(p.value)))
            print("   -> Sintax Error! Line: '%s'" % (str(p.lexer.lineno)))
        else:
            print("   -> Lexer Error! Line: '%s'" % uLexico.lexer.lineno)
    else:
        raise Exception('Syntax', 'Error')

# ------------------------------------------------------------------------------
def uParser(data):
    parser.parse(data, tracking = True)
# Build the parser
parser = yacc.yacc()
# ------------------------------------------------------------------------------

if __name__ == '__main__':

    f = open('pascal_6.pas', 'r')
    data = f.read()
    f.close()
    uParser(data)

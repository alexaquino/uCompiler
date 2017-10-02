
{ PROCEDURE }
{ 'procDecl : PROCEDURE ID LPAREN parameters RPAREN SEMICOLON block SEMICOLON' }

PROGRAM Soma_Pares;
LABEL 123456;

CONST
PI = 3.1415926;

VAR
  Idade: INTEGER;
  Salario: REAL;
  Nome, CPF: STRING;

BEGIN

  PROCEDURE findMin(x, y, z: INTEGER);
  { Finds the minimum of the 3 values }
  BEGIN
    IF x < y THEN
      m := x;
    ELSE
      m := y;
    IF z < m THEN
      m := z;
  END;

END.

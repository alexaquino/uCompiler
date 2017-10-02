
{ FUNCTION }
{ 'functDecl : FUNCTION ID LPAREN parameters RPAREN COLON typeDefinition SEMICOLON block' }

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

  FUNCTION max(num1, num2: INTEGER): INTEGER;
  { function returning the max between two numbers }
  VAR
  { local variable declaration }
  result: INTEGER;

  BEGIN
    IF num1 > num2 THEN
      result := num1;
    ELSE
      result := num2;
    max := result;
  END;

END.

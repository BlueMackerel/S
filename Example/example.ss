FUN Add(a,b)->a+b


FUN Sub(a,b)->a-b



FUN Mul(a,b)->a*b



FUN Div(a,b)->a/b

VAR i=0

VAR result=0


FOR i=0 TO 101 THEN VAR result=Add(result,i)

PRINT(result)
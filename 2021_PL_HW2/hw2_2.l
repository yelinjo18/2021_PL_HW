%{
#include <stdio.h>
%}
%%

(10(0+)1((1*)|0)1)+	{printf("%s is danger\n", yytext);}
.|\n	;
%%

int main(){
	yylex();
	return 0;
}

int yywrap(){
	return 1;
}
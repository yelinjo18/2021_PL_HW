%{
#include <stdio.h>
int n_love = 0;
%}
%%

love|Love		{n_love++;}
.|\n	;
%%

int main(){
	yylex();
	printf("number of love=%d\n", n_love);
	return 0;
}

int yywrap(){
	return 1;
}
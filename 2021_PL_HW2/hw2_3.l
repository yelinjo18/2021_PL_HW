%{
#include <stdio.h>
int n_arr[13] = { 0, };
%}

DIGIT	[0-9]
LETTER	[a-zA-Z]
NOTP	[a-oq-zA-OQ-Z]

%%

"/*"(.*|\n*)*"*/"	{n_arr[5]++;}	// 여러줄 주석
"//"(.)*\n	{n_arr[5]++;}	// 한줄 주석

(#include|#define)(.*)\n	{n_arr[0]++;}	// 전처리기
0{DIGIT}+		{n_arr[1]++;}	// 8진수
-{DIGIT}+	{n_arr[2]++;}	// 음수
{DIGIT}+	{n_arr[3]++;}	// 양수

"+"|"-"|"*"|"/"|"%"		{n_arr[4]++;}	//산술연산자
==|!=|>|<|>=|<=	{n_arr[4]++;}	// 관계연산자
&&|"||"|!	{n_arr[4]++;}	// 논리연산자
"++"|"--"	{n_arr[4]++;}	// 증감연산자
","|"&"|"*"	|"->"	{n_arr[4]++;}	// 콤마, 참조, 포인터

=	{n_arr[6]++;}	// 대입연산자
"{"	{n_arr[7]++;}
"}"	{n_arr[8]++;}

{NOTP}*p{NOTP}*p{NOTP}*	{n_arr[9]++;}	// wordcase1
e{LETTER}*m	{n_arr[10]++;}	// wordcase2

{LETTER}+	{n_arr[11]++;}	// 그외 단어수
.|\n	{n_arr[12]++;}	
%%

int main(){
	yylex();
	printf("preprocessor = %d\n", n_arr[0]);
	printf("octal number = %d\n", n_arr[1]);
	printf("negative decimal number = %d\n", n_arr[2]);
	printf("positive decimal number = %d\n", n_arr[3]);
	printf("operator = %d\n", n_arr[4]);
	printf("comment = %d\n", n_arr[5]);
	printf("'=' = %d\n", n_arr[6]);
	printf("'{' = %d\n", n_arr[7]);
	printf("'}' = %d\n", n_arr[8]);
	printf("wordcase1 = %d\n", n_arr[9]);
	printf("wordcase2 = %d\n", n_arr[10]);
	printf("word = %d\n", n_arr[11]);
	printf("mark = %d\n", n_arr[12]);
	return 0;
}

int yywrap(){
	return 1;
}
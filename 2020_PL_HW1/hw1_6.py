'''
 과제 6
 / 홍익대학교 리눅스 서버 접속 시 데이터는 0,1 두 비트로 변경되어 전송된다
서버의 안전을 위해 수신된 데이터는 암호화가 되어있는지 확인이 필요하다
지환이는 데이터를 분석해 암호화 되지 않은 데이터는 일정한 패턴을 가지고 있다는 것을 알게 되었다.
서버의 안전을 위해 지환이는 암호화 되지 않은 데이터를 확인해 차단하고자 한다
프로그래밍을 잘 하지 못하는 지환이를 대신해 암호화 되지 않은 데이터를 차단하는 프로그램을 만들어주자
이때 ~ 기호의 의미는 다음과 같다
- X~는 X가 한 번 이상 반복되는 모든 경우의 수의 집합
- (xyz)~는 xyz가 한 번 이상 반복되는 모든 경우의 수의 집합
ex) 1~={1,11,111,1111……,....}
10~11={1011,10011,100011,1000….11,....}
또한 | 기호의 의미는 다음과 같다
- (x|y)는 x 또는 y 중 아무거나 하나만을 선택해서 만든 경우의 수의 집합을 의미한다
ex) (1001|0101)={1001,0101}
만약 (x|y)~가 될 경우는 x와 y를 마음대로 섞어서 만들 수 있는 모든 경우의 수의 집합을 의미한다
ex)(100|11)~={100,11,10011,11100,1110011,....}
과제 6
Python- Input의 첫번째 줄은 문자열의 개수 n
두번째 줄부터는 0과 1로 이루어진 문자열이 주어진다
- Output은 패턴과 같은 데이터이면 DANGER, 아닐 경우는 PASS를 출력
- 입력은 input()을 통해 받을 것
- 주어진 패턴 : (100~1~|01)~
Input : 2
1000101
10101
Output : DANGER
PASS
'''

def code_test(code):
    # 100
    if code[:3]=='100':
        code=code[3:]
    else:
        code='-'
        return code

    # ~
    while code[0]=='0':
        code=code[1:]

    # 1
    if code[0]=='1':
        code = code[1:]
    else:
        code='-'
        return code

    # ~|01
    # ~1
    if code[0]=='1':
        while code[0]=='1':
            code = code[1:]
        if code[0]=='0':
            code.insert(0,'1')
    # 01
    elif code[0]=='0':
        if code[:2]=='01':
            code = code[2:]
        else:
            code='-'
            return code
    else:
        code='-'
        return code

    return code


# input data
n=int(input())
codes=[]
for n in range(0, n, 1):
    codes.append(input())

for c in codes:
    while len(c)>0 and c[0]!='-':
        c=code_test(c)

    if len(c)==0:
        print("DANGER")
    elif c[0]=='-':
        print("PASS")


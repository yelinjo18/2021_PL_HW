'''
 과제 5
 / 한 개의 강의실이 있고 이를 사용하고자 하는 N개의 수업이 존재한다
각 강의들마다 시작 시간과 종료 시간은 다르므로, 강의실에 강의들이 겹치지 않고 배치되는 강의의 수가
최대가 되도록 하는 배치 방법을 찾아라
- input의 첫번째 줄은 강의의 개수
두번째 줄부터는 강의 번호, 강의 시간, 종료 시간으로 이루어져 있다
- output은 최대 배치 강의 수
배치되는 강의의 리스트 로 출력한다
- 입력을 input()을 통해 받을 것

Input:11
1 3 8
2 5 9
3 3 5
4 1 4
5 8 12
6 0 6
7 8 11
8 2 13
9 4 7
10 6 10
11 12 14
Output:[4,9,7,11]
'''
from operator import itemgetter

# input
n=int(input())
classes=[]
for i in range(0, n, 1):
    my_class = list(map(int, input().split()))
    classes.append(my_class)

# 시작 시간을 기준으로 정렬
classes.sort(key=itemgetter(1))

# 배정 시작
now_time=0
playing=classes[0]
result=[]

for cl in classes:
    now_time=cl[1]

    # 현재 강의가 끝나면
    if playing[2]<=now_time:
        result.append(playing[0])
        playing=cl
    # 지금 보고 있는 강의의 종료시간이 더 빠르다면
    elif playing[2]>cl[2]:
        playing=cl
# 마지막 수업 추가
result.append(playing[0])

print(result)

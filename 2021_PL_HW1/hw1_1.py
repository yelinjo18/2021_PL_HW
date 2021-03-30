'''
 과제 1
 리스트에서 숫자 n이 몇 번째 순서에 위치하여 있는지를 Binary Search로 찾아 출력하는 함수를 구현하라
- 입력한 숫자가 없을 경우, None을 출력
- 입력은 input()을 통해 받을 것
- 입력 값의 첫 줄은 list의 요소가, 두번째 줄은 n의 값이다
Input : 1 11 15 19 37 40 59 61
15
Output : 3
Input : 1 11 15 19 32 48 59 65
58
Output : None
'''

def BS(list, key):
    low=0
    high=len(list)-1
    # Search key!
    while low<=high:
        m = int((low + high) / 2)
        if list[m]==key:
            break
        elif list[m]<key:
            low=m+1
        elif list[m]>key:
            high=m-1

    if low>high:
        print("None")
    else:
        print(m+1)



#Input to List, key
my_list = list(map(int,input().split()))
key=int(input())
BS(my_list, key)



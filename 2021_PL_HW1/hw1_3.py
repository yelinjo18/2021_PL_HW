'''
 과제 3
 / 리스트를 Merge Sort로 정렬하라
- 입력은 input()을 통해 받을 것
- 입력은 리스트의 요소들이다
Input : 100 23 31 123 435 642 1
Output : [1, 23, 31, 100, 123, 435, 642]
'''

#Merge Sort
def MergeSort(list):
    if len(list)<=1:
        return list
    else:
        m_i=int(len(list)/2)

        # Recursion
        pre=MergeSort(list[:m_i])
        post=MergeSort(list[m_i:])

        return Merge(pre, post)

# Merge
def Merge(pre, post):
    t_list=[]
    i=0
    j=0

    while i<len(pre) and j<len(post):
        if pre[i]<=post[j]:
            t_list.append(pre[i])
            i+=1
        else:
            t_list.append(post[j])
            j+=1

    if i>=len(pre):
        t_list.extend(post[j:])
    elif j>=len(post):
        t_list.extend(pre[i:])

    return t_list

# Input to List
list = list(map(int,input().split()))

print(MergeSort(list))
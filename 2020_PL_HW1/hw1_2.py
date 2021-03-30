'''
 과제 2
/ 리스트를 Quick Sort로 정렬하라
- 입력은 input()을 통해 받을 것
- 입력은 리스트의 요소들이다
Input : 26 5 37 1 61 11 59 15 48 19
Output : [1, 5, 11, 15, 19, 26, 37, 48, 59, 61]
'''

# Quick Sort
def QuickSort(first_i, last_i):
    if(first_i<last_i):
        # Partition
        pivot=list[first_i]
        i=first_i+1
        j=last_i

        while i<=j:
            while i<=last_i and list[i]<pivot:
                i+=1
            while j>first_i and list[j]>pivot:
                j-=1

            if i>j:
                # Exchange pivot & list[j]
                list[first_i]=list[j]
                list[j]=pivot
            else:
                # Exchange list[i] & list[j]
                tmp=list[i]
                list[i]=list[j]
                list[j]=tmp

        # Recursion
        QuickSort(first_i, j-1)
        QuickSort(j+1, last_i)

# Input to List
list = list(map(int,input().split()))

QuickSort(0, len(list)-1)
print(list)




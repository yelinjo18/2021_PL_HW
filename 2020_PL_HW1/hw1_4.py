'''
 과제 4
/ 아래 그림과 같은 이진 트리를 생성하고 전위 순회, 중위 순회, 후위 순회 방식으로 각 방문 노드를 방문하고
방문 순서를 출력하라.
- 클래스로 구현할 것
- 전위 순회, 중위 순회, 후위 순회는 함수를 각각 따로 만들 것
- Input : null
'''

def PreOrder(now):
    print(my_tree[now].key)
    if my_tree[now].L!=-1:
        PreOrder(my_tree[now].L)
    if my_tree[now].R!=-1:
        PreOrder(my_tree[now].R)

def InOrder(now):
    if my_tree[now].L != -1:
        InOrder(my_tree[now].L)
    print(my_tree[now].key)
    if my_tree[now].R != -1:
        InOrder(my_tree[now].R)

def PostOrder(now):
    if my_tree[now].L != -1:
        PostOrder(my_tree[now].L)
    if my_tree[now].R != -1:
        PostOrder(my_tree[now].R)
    print(my_tree[now].key)

class Node:
    def __init__(self, Key, L, R):
        self.key=Key
        self.L=L
        self.R=R

# Main
my_tree=[]
my_tree.append(Node(15, 1, 2))
my_tree.append(Node(1, 3, 4))
my_tree.append(Node(37, 5, 6))
my_tree.append(Node(61, -1, -1))
my_tree.append(Node(26, -1, -1))
my_tree.append(Node(59, -1, -1))
my_tree.append(Node(48, -1, -1))

print("Preorder Traverse")
PreOrder(0)
print("Inorder Traverse")
InOrder(0)
print("Postorder Traverse")
PostOrder(0)

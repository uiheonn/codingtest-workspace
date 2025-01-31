n = int(input())
graph_lst = [[] for _ in range(26)] # 26개의 리스트 생성 -> 알파벳의 자식 노드를 저장
for _ in range(n):
    root,left,right = map(str, input().split())
    graph_lst[ord(root)-65].append(left)
    graph_lst[ord(root)-65].append(right)

def preorder_traversal(start):
    print(start,end="")
    a,b = graph_lst[ord(start)-65]
    if a != ".":
        preorder_traversal(a)
    if b != ".":
        preorder_traversal(b)

def inorder_traversal(start):
    a,b = graph_lst[ord(start)-65]
    if a != ".":
        inorder_traversal(a)
    print(start,end="")
    if b != ".":
        inorder_traversal(b)

def postorder_traversal(start):
    a,b = graph_lst[ord(start)-65]
    if a != ".":
        postorder_traversal(a)
    if b != ".":
        postorder_traversal(b)
    print(start,end="")

preorder_traversal("A")
print()
inorder_traversal("A")
print()
postorder_traversal("A")
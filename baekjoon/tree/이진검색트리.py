import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_bst(preorder):
    if not preorder:
        return None

    root = Node(preorder[0])
    stack = [root]

    for value in preorder[1:]:
        node = Node(value)
        if value < stack[-1].value:  # 왼쪽 자식
            stack[-1].left = node
        else:  # 오른쪽 자식
            parent = None
            while stack and stack[-1].value < value:
                parent = stack.pop()
            parent.right = node
        stack.append(node)

    return root

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

# BST 구성 및 후위 순회 실행
root = build_bst(lst)
postorder(root)
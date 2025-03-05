import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
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
    
def change_original(lst):
    node = Node(lst[0])
    stack = [node]
    for nd in lst[1:]:
        tmp = Node(nd)
        if nd < stack[-1].value:
            stack[-1].left = tmp
        else:
            parent = None
            while stack and stack[-1].value < nd:
                parent = stack.pop()
            parent.right = tmp
        stack.append(tmp)
    return node

def postorder(node):
    if node == None:
        return
    v,l,r = node.value, node.left, node.right
    postorder(l)
    postorder(r)
    print(v)

temp = change_original(lst)
postorder(temp)
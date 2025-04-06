import sys

input = sys.stdin.readline
V,E = map(int, input().split())
graph_lst = []

for _ in range(E):
    a,b,c = map(int, input().split())
    graph_lst.append([a,b,c])

graph_lst.sort(key = lambda x:x[2])
selected = [-1 for _ in range(V+1)]

def find_root(vertax):
    while selected[vertax] != -1:
        vertax = selected[vertax]
    return vertax

def check_cycle(v1,v2): # v1,v2를 연결함으로서 사이클이 생성되는지 확인
    v1_root = find_root(v1)
    v2_root = find_root(v2)
    if v1_root != v2_root: # 싸이클이 아니다
        if v1_root > v2_root:
            selected[v1_root] = v2_root
        else:
            selected[v2_root] = v1_root
        return True
    else:
        return False

result = 0
count = 0
for node in graph_lst:
    if count == V-1:
        break
    v1,v2,cost = node
    if check_cycle(v1,v2):
        # print("정점", v1, "과 정점", v2,"가 연결되었습니다!")
        # print("selected : ", selected)
        result+=cost
        count+=1

print(result)
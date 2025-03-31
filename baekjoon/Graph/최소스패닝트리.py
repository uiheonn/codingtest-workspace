import collections
import sys

input = sys.stdin.readline
V,E = map(int, input().split())
dic = collections.defaultdict(tuple)
graph_lst = []

for _ in range(E):
    a,b,c = map(int, input().split())
    graph_lst.append([a,b,c])

graph_lst.sort(key = lambda x:x[2])
selected = [-1 for _ in range(V+1)]

def check_cycle(v1,v2): # v1,v2를 연결함으로서 사이클이 생성되는지 확인
    if v1 == -1 and v2 == -1:
        if v1 < v2:
            selected[v2] = v1
        else:
            selected[v1] = v2
        return True
    v1_copy = v1
    while selected[v1_copy] != -1:
        v1_copy = selected[v1_copy]
    v2_copy = v2
    while selected[v2_copy] != -1:
        v2_copy = selected[v2_copy]
    if v1_copy == v2_copy: # 같은 부모라면 사이클
        return False
    else:
        if v1 < v2:
            selected[v2] = v1
        else:
            selected[v1] = v2
        return True

result = 0
count = set()
for node in graph_lst:
    if len(count) == V:
        break
    v1,v2,cost = node
    if check_cycle(v1,v2):
        print("정점", v1, "과 정점", v2,"가 연결되었습니다!")
        print("selected : ", selected)
        result+=cost
        count.add(v1)
        count.add(v2)

print(result)



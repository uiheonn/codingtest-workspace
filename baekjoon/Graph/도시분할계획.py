import sys

input = sys.stdin.readline
N,M = map(int, input().split())
lst = []
for _ in range(M):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x : x[2])
selected = [-1 for _ in range(N+1)]
result = []

def find_root(v):
    while selected[v] != -1:
        v = selected[v]
    return v

def check_cycle(a,b):
    v1 = find_root(a)
    v2 = find_root(b)
    if v1 != v2: # 다르면 사이클이 아님
        if v1 > v2:
            selected[v1] = v2
        else:
            selected[v2] = v1
        return False
    else:
        return True

for i in range(M):
    a,b,cost = lst[i] # 연결 노드, 비용
    if check_cycle(a,b): # 사이클이면 연결하지 않음
        continue
    else:
        result.append(cost)
        if len(result) == N-1: # 모두 연결되었으면 종료
            break
result.pop() # 비용이 가장 큰 경로를 제거
print(sum(result))
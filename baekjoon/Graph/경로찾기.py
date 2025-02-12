# 3
# 0 1 0
# 0 0 1
# 1 0 0
import collections
import sys

n = int(input())
graph_lst = [[] for _ in range(n)]
for i in range(n):
    semi_lst = list(map(int, input().split()))
    for j in range(len(semi_lst)):
        if semi_lst[j]:
            graph_lst[i].append(j)

def bfs(i):
    visited = [False for _ in range(n)]
    queue = collections.deque()
    queue.append(i)
    while len(queue) != 0:
        tmp = queue.popleft() # 연결된 노드 1

        for ele in graph_lst[tmp]:
            if not visited[ele]:
                queue.append(ele)
                visited[ele] = True
    res = []
    for i in range(n):
        if visited[i]:
            res.append(1)
        else:
            res.append(0)
    return res

for i in range(n):
    sys.stdout.write(" ".join(map(str, bfs(i))))
    print()
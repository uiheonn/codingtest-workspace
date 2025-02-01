import collections
import sys

n = int(input())
graph_lst = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    graph_lst[a].append(b)
    graph_lst[b].append(a)

queue = collections.deque()
queue.append(1)
visited[1] = True
parent = [0 for _ in range(n+1)]

while len(queue) != 0:
    tmp = queue.popleft()
    # print("tmp : ", tmp)

    for ele in graph_lst[tmp]:
        if not visited[ele]:
            queue.append(ele)
            visited[ele] = True
            parent[ele] = tmp

sys.stdout.write("\n".join(map(str, parent[2:])))
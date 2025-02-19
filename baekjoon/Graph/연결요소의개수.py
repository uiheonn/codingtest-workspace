import collections

n,m = map(int, input().split())
graph_lst = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    graph_lst[a-1].append(b-1)
    graph_lst[b-1].append(a-1)
# for ele in graph_lst:
#     print(ele)
visited = [False] * n

queue = collections.deque()

def bfs(vertax):
    queue.append(vertax)
    visited[vertax] = True

    while len(queue) != 0:
        tmp = queue.popleft()
        for i in graph_lst[tmp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

count = 0
for i in range(n):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)
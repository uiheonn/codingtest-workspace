import collections

n,m = map(int, input().split())
graph_lst = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    graph_lst[a-1].append(b-1)
    graph_lst[b-1].append(a-1)
# for ele in graph_lst:
#     print(ele)

def bfs(i): # i정점 나머지 정점들의 최단거리의 합
    queue = collections.deque()
    queue.append([i,0])
    visited = [-1 for _ in range(n)]
    visited[i] = 0

    while len(queue) != 0:
        tmp, cost = queue.popleft()

        for ele in graph_lst[tmp]:
            if visited[ele] == -1:
                queue.append([ele,cost+1])
                visited[ele] = cost+1
    # print("visited : ", visited)
    return sum(visited)

result = []
for i in range(n):
    result.append(bfs(i))
min_num = min(result)
for i in range(n):
    if min_num == result[i]:
        print(i+1)
        break
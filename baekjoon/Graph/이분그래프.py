# 인접하는 노드면 visited과 다른 색깔을 부여
# 만약 같은 색깔이라면 return
import collections

n = int(input())
for _ in range(n):
    v, e = map(int, input().split()) # v는 정점의 개수, e는 간선의 개수
    graph_lst = [[] for i in range(v)]
    visited = [0] * v
    queue = collections.deque()

    for i in range(e):
        a,b = map(int, input().split())
        graph_lst[a-1].append(b-1)
        graph_lst[b-1].append(a-1)


    def bfs(start):
        queue.append([start, graph_lst[start]])
        visited[start] = 1

        while len(queue) != 0:
            u, close_nodes = queue.popleft()
            color = visited[u]

            for i in close_nodes: # [2,3]
                if not visited[i]:
                    if color == 1:
                        visited[i] = 2
                    else:
                        visited[i] = 1
                    queue.append([i, graph_lst[i]])
                elif visited[i] == color:
                    return False
        return True

    result = "YES"
    for i in range(v):
        if not visited[i]:
            if not bfs(i):
                result = "NO"
                break
    print(result)
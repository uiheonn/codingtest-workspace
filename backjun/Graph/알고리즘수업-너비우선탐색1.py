import sys
import collections

sys.setrecursionlimit(10 ** 5)

n,m,r = map(int, input().split())
graphLst = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    graphLst[a-1].append(b-1)
    graphLst[b-1].append(a-1)

# n,m,r = map(int, input().split())
# graphLst = [[] for _ in range(n)]
# for i in range(m):
#     a,b = map(int, input().split())
#     graphLst[a-1].append(b-1)
#     graphLst[b-1].append(a-1)

for ele in graphLst:
    ele.sort()

visited = [0] * (n) # 정점을 방문했는지 확인하는 배열
count = 1
queue = collections.deque()

def bfs(start):
    global count

    visited[start] = count
    count+=1
    queue.append(start)

    while len(queue) != 0:
        u = queue.popleft()
        for ele in graphLst[u]:
            if visited[ele] == 0:
                visited[ele] = count
                count+=1
                queue.append(ele)

bfs(r-1)

sys.stdout.write("\n".join(map(str, visited)))
import sys
import collections

sys.setrecursionlimit(10 ** 5)

# n,m,r = map(int, input().split())
# graphLst = [[] for _ in range(n)]
# for i in range(m):
#     a,b = map(int, input().split())
#     graphLst[a-1].append(b-1)
#     graphLst[b-1].append(a-1)

input = sys.stdin.read
data = input().splitlines()
n, m, r = map(int, data[0].split())
graphLst = [[] for _ in range(n)]
for i in range(1, m+1):
    a,b = map(int, data[i].split())
    graphLst[a-1].append(b-1)
    graphLst[b-1].append(a-1)

for ele in graphLst:
    ele.sort()

dfs_visited = [False] * (n) # 정점을 방문했는지 확인하는 배열
dfs_result = []
bfs_visited = [False] * (n)
bfs_result = []
queue = collections.deque()

def dfs(start):
    dfs_visited[start] = True
    dfs_result.append(start+1)
    
    for ele in graphLst[start]:
        if dfs_visited[ele] == False:
            dfs(ele)

def bfs(start):
    bfs_visited[start] = True
    queue.append(start)

    while len(queue) != 0:
        u = queue.popleft() 
        bfs_result.append(u+1)
        for ele in graphLst[u]:
            if bfs_visited[ele] == False:
                bfs_visited[ele] = True
                queue.append(ele)

dfs(r-1)
bfs(r-1)

sys.stdout.write(" ".join(map(str, dfs_result)))
print()
sys.stdout.write(" ".join(map(str, bfs_result)))

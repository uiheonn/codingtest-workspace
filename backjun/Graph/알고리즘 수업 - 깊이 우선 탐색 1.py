import sys

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

# input = sys.stdin.read
# data = input().splitlines()
# n,m,r = map(int, data[0].split())
# graph = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(1,m+1):
#     a,b = map(int, data[i].split())
#     graph[a-1][b-1] = 1
#     graph[b-1][a-1] = 1

visited = [0] * (n) # 정점을 방문했는지 확인하는 배열
count = 1

def dfs(start):
    global count

    visited[start] = count
    count+=1
    
    for ele in graphLst[start]:
        if visited[ele] == 0:
            dfs(ele)

dfs(r-1)

sys.stdout.write("\n".join(map(str, visited)))
import sys

sys.setrecursionlimit(10 ** 5)

# n = int(input())
# m = int(input())
# graphLst = [[] for _ in range(n)]
# for i in range(m):
#     a,b = map(int, input().split())
#     graphLst[a-1].append(b-1)
#     graphLst[b-1].append(a-1)

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
m = int(data[1])
graphLst = [[] for _ in range(n)]
for i in range(2,m+2):
    a,b = map(int, data[i].split())
    graphLst[a-1].append(b-1)
    graphLst[b-1].append(a-1)

for ele in graphLst:
    ele.sort()

visited = [False] * (n) # 정점을 방문했는지 확인하는 배열
count = 0

def dfs(start):
    global count

    visited[start] = True
    count+=1
    
    for ele in graphLst[start]:
        if visited[ele] == False:
            dfs(ele)

dfs(0)

print(count-1)
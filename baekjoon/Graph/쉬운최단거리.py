import collections
import sys

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
lst = []
for i in range(1,n+1):
    tmp = list(map(str, data[i].split()))
    lst.append(tmp)

# n,m = map(int, input().split()) # n은 세로, m은 가로
# lst = []
# for i in range(n):
#     tmp = list(map(str, input().split()))
#     lst.append(tmp)

visited = [[False for i in range(m)] for j in range(n)]
distance = [[0 if lst[i][j] == "0" else -1 for j in range(m)] for i in range(n)]
queue = collections.deque()
dy = [1,0,-1,0]
dx = [0,1,0,-1]

row = None
col = None
for i in range(n):
    for j in range(m):
        if lst[i][j] == "2":
            row, col = i, j

def bfs(r, c, count):
    queue.append([r,c,count])
    visited[r][c] = True
    
    while len(queue) != 0:
        tmp = queue.popleft()
        rr = tmp[0]
        cc = tmp[1]
        count_c = tmp[2]
        distance[rr][cc] = count_c

        for i in range(4):
            ny = cc + dy[i]
            nx = rr + dx[i]
            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == "1" and not visited[nx][ny]:
                queue.append([nx,ny,count_c+1])
                visited[nx][ny] = True


bfs(row, col, 0)
for ele in distance:
    sys.stdout.write(" ".join(map(str, ele)))
    print()
import collections
import sys

input = sys.stdin.read
data = input().splitlines()
col, row = map(int, data[0].split())
visited = [[False for _ in range(col)] for j in range(row)]
feeLst = [[0 for _ in range(col)] for j in range(row)]
lst = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
queue = collections.deque()
for i in range(row):
    tmp = list(map(str, data[i+1].split()))
    for j in range(col):
        if tmp[j] == "1":
            queue.append([i,j,1])
            visited[i][j] = True
        elif tmp[j] == "-1":
            feeLst[i][j] = -1
    lst.append(tmp)

# col, row = map(int, input().split())
# visited = [[False for _ in range(col)] for j in range(row)]
# feeLst = [[0 for _ in range(col)] for j in range(row)]
# lst = []
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# queue = collections.deque()
# for i in range(row):
#     tmp = list(map(str, input().split()))
#     for j in range(col):
#         if tmp[j] == "1":
#             queue.append([i,j,1])
#             visited[i][j] = True
#         elif tmp[j] == "-1":
#             feeLst[i][j] = -1
#     lst.append(tmp)

while len(queue) != 0:
    r, c, count = queue.popleft()
    feeLst[r][c] = count
    
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and lst[nx][ny] != "-1":
            queue.append([nx, ny, count+1])
            visited[nx][ny] = True

maxData = -1
for ele in feeLst:
    if 0 in ele:
        maxData = 0
        break
    tmp = max(ele)
    if tmp > maxData:
        maxData = tmp

print(maxData - 1)
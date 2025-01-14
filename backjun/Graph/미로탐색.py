import collections
import sys

# input = sys.stdin.read
# data = input().splitlines()
# row, col = map(int, data[0].split())
# lst = []
# for i in range(1,row+1):
#     tmp = data[i]
#     semi = []
#     for j in range(col):
#         semi.append(tmp[j])
#     lst.append(semi)

row, col = map(int, input().split())
lst = []
for i in range(row):
    tmp = input()
    semi = []
    for j in range(col):
        semi.append(tmp[j])
    lst.append(semi)

visited = []
for i in range(row):
    tmp = []
    for j in range(col):
        tmp.append(False)
    visited.append(tmp)

queue = collections.deque()
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def bfs():
    visited[0][0] = True
    queue.append([0, 0, 1])

    while len(queue) != 0:
        tmp = queue.popleft()
        r = tmp[0]
        c = tmp[1]
        count = tmp[2]

        if r == row-1 and c == col-1:
            return count
        
        for i in range(4):
            ny = c + dy[i]
            nx = r + dx[i]
            if 0 <= nx < row and 0 <= ny < col and lst[nx][ny] == "1" and not visited[nx][ny]:
                queue.append([nx, ny, count+1])
                visited[nx][ny] = True

print(bfs())
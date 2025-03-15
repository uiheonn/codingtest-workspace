import itertools
import collections
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
wall_available_lst = []
graph_lst = []
lst = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(n):
    temp = list(map(int, input().split()))
    lst.append(temp)
    for j in range(m):
        if temp[j] == 2:
            graph_lst.append([i,j]) # 바이러스의 위치
        elif temp[j] == 0:
            wall_available_lst.append([i,j]) # 빈 공간의 위치

data = itertools.combinations(wall_available_lst, 3)
temp = list(data)

def bfs():
    visited = [[False for _ in range(m)] for j in range(n)]
    queue = collections.deque()
    for graph in graph_lst:
        gx, gy = graph
        queue.append([gx,gy])
        visited[gx][gy] = True
        while len(queue) != 0:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and lst[nx][ny] == 0:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
    count = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0 and not visited[i][j]:
                count+=1
    return count

max_num = 0
aaa = 0
for ele in temp:
    for nm in ele: # 벽 세우기
        lst[nm[0]][nm[1]] = 1
    
    virus = bfs()

    if virus > max_num:
        max_num = virus

    for nm in ele: # 벽 치우기
        lst[nm[0]][nm[1]] = 0

print(max_num)
import collections

n = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

normal_lst = []
for i in range(n):
    normal_lst.append(input())

abnormal_lst = []
for i in range(n):
    tmp = ""
    for j in range(n):
        st = normal_lst[i][j]
        if normal_lst[i][j] == "G":
            st = "R"
        tmp+=st
    abnormal_lst.append(tmp)

normal_visited = [[False for _ in range(n)] for j in range(n)]
abnormal_visited = [[False for _ in range(n)] for j in range(n)]

def findNext(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                return i,j
    return -1,-1

def bfs(lst, visited):
    queue = collections.deque()
    count = 0

    while True:
        next_x, next_y = findNext(visited)
        if next_x == -1:
            break
        queue.append([next_x,next_y])
        visited[next_x][next_y] = True

        while len(queue) != 0:
            x,y = queue.popleft()
            color = lst[x][y]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] == color and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
        count+=1
    return count

normal = bfs(normal_lst, normal_visited)
abnormal = bfs(abnormal_lst, abnormal_visited)

print(normal, abnormal)
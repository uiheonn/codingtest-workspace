# 벽을 부술수도 있고, 아닐수도있다 -> 부쉈는지를 체크하는 데이터를 큐에 넣으면 되지 않을까
# 벽을 부순 이력이 있는 사람의 방문 이력에는 뒷꼬리표를 붙인다 -> False를 붙여서 벽을 부순 이력이 없는 사람은 visited이 True여도 방문이 가능하도록 한다
import sys
import collections

input = sys.stdin.read
data = input().splitlines()
row, col = map(int, data[0].split())
lst = []
for i in range(1, row+1):
    inp = data[i]
    tmp = []
    for j in range(col):
        tmp.append(inp[j])
    lst.append(tmp)

# row, col = map(int, input().split())
# lst = []
# for i in range(row):
#     inp = input()
#     tmp = []
#     for j in range(col):
#         tmp.append(inp[j])
#     lst.append(tmp)

visited = [[[False, False] for _ in range(col)] for j in range(row)]
dy = [1,0,-1,0]
dx = [0,1,0,-1]
queue = collections.deque()
queue.append([0,0,True,1])
visited[0][0][0] = True
visited[0][0][1] = True

result = -1
while len(queue) != 0:
    r, c, canCrack, count = queue.popleft()

    if r == row-1 and c == col-1:
        result = count
        break
    
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        
        if 0 <= nx < row and 0 <= ny < col and lst[nx][ny] == "0" and not visited[nx][ny][0]: # 아무도 방문하지 곳을 지나가는 경우
            if canCrack: # 벽을 부수지 않은 사람이면 꼬리표를 달음 -> 나중에 또 방문하는 사람이 없어야 하므로 
                visited[nx][ny][1] = True
            queue.append([nx,ny,canCrack,count+1])
            visited[nx][ny][0] = True
        elif 0 <= nx < row and 0 <= ny < col and lst[nx][ny] == "0" and visited[nx][ny][0] and not visited[nx][ny][1] and canCrack: # 벽을 부순적이 없는 사람인데 이미 벽을 부순 사람이 지나가는 경우
            queue.append([nx,ny,canCrack,count+1])
            visited[nx][ny][1] = True
        elif 0 <= nx < row and 0 <= ny < col and lst[nx][ny] == "1" and canCrack and not visited[nx][ny][0]: # 벽을 부수고 지나가는 경우
            queue.append([nx,ny,False,count+1])
            visited[nx][ny][0] = True

print(result)
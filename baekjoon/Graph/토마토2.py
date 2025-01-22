import collections

col, row, height = map(int, input().split())
visited = [[[False for _ in range(col)] for j in range(row)] for i in range(height)]
feeLst = [[[0 for _ in range(col)] for j in range(row)] for k in range(height)]
lst = []
dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]

queue = collections.deque()
for k in range(height):
    semi = []
    for i in range(row):
        tmp = list(map(str, input().split()))
        for j in range(col):
            if tmp[j] == "1":
                queue.append([k,i,j,1])
                visited[k][i][j] = True
            elif tmp[j] == "-1":
                feeLst[k][i][j] = -1
        semi.append(tmp)  
    lst.append(semi)

while len(queue) != 0:
    h, r, c, count = queue.popleft()
    feeLst[h][r][c] = count

    for i in range(6):
        nx = r + dx[i]
        ny = c + dy[i]
        nh = h + dh[i]
        if 0 <= nx < row and 0 <= ny < col and 0 <= nh < height and not visited[nh][nx][ny] and lst[nh][nx][ny] != "-1":
            queue.append([nh, nx, ny, count+1])
            visited[nh][nx][ny] = True

# print("feeLst")
# for ele in feeLst:
#     for lel in ele:
#         print(lel)


result = []
for ele in feeLst:
    for lel in ele:
        result.append(lel)

max_data = -1
for ele in result:
    if 0 in ele:
        max_data = 0
        break
    tmp = max(ele)
    if tmp > max_data:
        max_data = tmp
print(max_data - 1)
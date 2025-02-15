import collections

a,b = map(int, input().split())
lst = []
location = None
for i in range(a):
    tmp = input()
    if location == None and 'I' in tmp:
        t = tmp.index('I')
        location = [i,t]
    lst.append(tmp)

dx = [0,0,1,-1]
dy = [-1,1,0,0]
visited = [[False for _ in range(b)] for j in range(a)]
count = 0
queue = collections.deque()
queue.append(location)
visited[location[0]][location[1]] = True

while len(queue) != 0:
    row, col = queue.popleft()

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny] and lst[nx][ny] != 'X':
            if lst[nx][ny] == 'P':
                count+=1
            queue.append([nx,ny])
            visited[nx][ny] = True

if count:
    print(count)
else:
    print("TT")
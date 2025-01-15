import sys
import collections

n = int(input())
dx = [-1,1,-2,2,-2,2,-1,1]
dy = [-2,-2,-1,-1,1,1,2,2]
result = []

for _ in range(n):
    length = int(input())
    startRow, startCol = map(int, input().split())
    endRow, endCol = map(int, input().split())
    queue = collections.deque()
    visited = [[False for j in range(length)] for i in range(length)]
    queue.append([startRow, startCol, 0])
    visited[startRow][startCol] = True
    
    while len(queue) != 0:
        tmp = queue.popleft()
        row, col, count = tmp

        if row == endRow and col == endCol:
            result.append(count)
            break

        for i in range(8):
            nx, ny = row + dx[i], col + dy[i]
            if 0 <= nx < length and 0 <= ny < length and visited[nx][ny] == False:
                queue.append([nx, ny, count+1])
                visited[nx][ny] = True

sys.stdout.write("\n".join(map(str, result)))
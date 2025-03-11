import sys

input = sys.stdin.readline
r,c = map(int, input().split())
lst = []
for _ in range(r):
    lst.append(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [False for i in range(26)]
result = -1
def dfs(row, col, alphabet):
    global result
    alphabet[ord(lst[row][col])-65] = True

    for i in range(4):
        nx = dx[i] + row
        ny = dy[i] + col
        if 0 <= nx < r and 0 <= ny < c and not alphabet[ord(lst[nx][ny])-65]:
            dfs(nx,ny,alphabet)
    tmp = alphabet.count(True)
    if result < tmp:
        result = tmp
    alphabet[ord(lst[row][col])-65] = False

dfs(0,0, visited)
print(result)
import sys

sys.setrecursionlimit(10 ** 9)

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split()) # 가로 # 세로 # 간선 수 # 세로는 row, 가로는 col인거임
    lst = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(0)
        lst.append(tmp)
    
    for i in range(k): # 간선 수 만큼 반복문 수행
        mm, nn = map(int, input().split())
        lst[nn][mm] = 1
    
    graph_lst = []
    for i in range(n):
        tmp = []
        for j in range(m):
            if lst[i][j] == 1:
                tmp.append(j)
        graph_lst.append(tmp)

    
    visited = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(False)
        visited.append(tmp)

    def dfs(row, col):
        if visited[row][col] == True:
            return
        visited[row][col] = True

        if row > 0 and lst[row-1][col] == 1 and visited[row-1][col] == False:
            dfs(row-1, col)
        if row < n-1 and lst[row+1][col] == 1 and visited[row+1][col] == False:
            dfs(row+1, col)
        if col > 0 and lst[row][col-1] == 1 and visited[row][col-1] == False:
            dfs(row, col-1)
        if col < m - 1 and lst[row][col+1] == 1 and visited[row][col+1] == False:
            dfs(row, col+1)
        
        return 0
    
    count = 0
    for i in range(len(graph_lst)):
        for j in graph_lst[i]:
            tmp = dfs(i, j)
            if tmp != None:
                count+=1

    print(count)
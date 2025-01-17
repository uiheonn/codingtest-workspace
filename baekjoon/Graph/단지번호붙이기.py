import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
lst = []
for i in range(1,n+1):
    tmp = data[i]
    semi = []
    for ele in tmp:
        semi.append(int(ele))
    lst.append(semi)

# n = int(input())
# lst = []
# for i in range(n):
#     tmp = input()
#     semi = []
#     for ele in tmp:
#         semi.append(int(ele))
#     lst.append(semi)

visited = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(False)
    visited.append(tmp)

graph_lst = []
for i in range(n):
    tmp = []
    for j in range(n):
        if lst[i][j] == 1:
            tmp.append(j)
    graph_lst.append(tmp)

def dfs(row, col):
    count = 0
    if visited[row][col] == True:
        return
    
    visited[row][col] = True
    count+=1

    if row > 0 and lst[row-1][col] == 1 and visited[row-1][col] == False:
        count+=dfs(row-1, col)
    if row < n-1 and lst[row+1][col] == 1 and visited[row+1][col] == False:
        count+=dfs(row+1, col)
    if col > 0 and lst[row][col-1] == 1 and visited[row][col-1] == False:
        count+=dfs(row, col-1)
    if col < n-1 and lst[row][col+1] == 1 and visited[row][col+1] == False:
        count+=dfs(row, col+1)
    return count

result = []
for i in range(len(graph_lst)):
    for j in graph_lst[i]:
        tmp = dfs(i, j)
        if tmp != None:
            result.append(tmp)
result.sort()
print(len(result))
sys.stdout.write("\n".join(map(str, result)))
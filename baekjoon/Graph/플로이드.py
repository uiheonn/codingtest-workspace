import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph_lst = [[1000000001 for i in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,cost = map(int, input().split())
    if graph_lst[a-1][b-1] > cost:
        graph_lst[a-1][b-1] = cost

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j != k:
                graph_lst[j][k] = min(graph_lst[j][k], graph_lst[j][i] + graph_lst[i][k])

for i in range(n):
    for j in range(n):
        if graph_lst[i][j] == 1000000001:
            graph_lst[i][j] = 0

for ele in graph_lst:
    sys.stdout.write(" ".join(map(str, ele)))
    print()
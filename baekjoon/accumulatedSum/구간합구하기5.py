import sys

input = sys.stdin.read
data = input().splitlines()
n,m = map(int, data[0].split())
lst = []
for i in range(1,n+1):
    lst.append(list(map(int, data[i].split())))

accumulate = []
for i in range(n):
    semi = []
    for j in range(n):
        summ = lst[i][j]
        if j != 0:
            summ += semi[-1]
        semi.append(summ)
    accumulate.append(semi)

for i in range(1, n):
    for j in range(n):
        accumulate[i][j] += accumulate[i-1][j]

result = []
for i in range(n+1, m+n+1):
    x1,y1,x2,y2 = map(int, data[i].split())
    pre = accumulate[x2-1][y2-1]
    post,row,col = 0,0,0

    if x1-2 >= 0 and y1-2 >= 0:
        post = accumulate[x1-2][y1-2]
    if x1-2 >= 0:
        row = accumulate[x1-2][y2-1]
    if y1-2 >= 0:
        col = accumulate[x2-1][y1-2]

    result.append(pre-row-col+post)

sys.stdout.write("\n".join(map(str, result)))
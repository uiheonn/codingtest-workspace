import sys

input = sys.stdin.read
output = sys.stdout.write
data = input().splitlines()
firstRow, firstCol = list(map(int, data[0].split()))
first = []
for i in range(1, firstRow+1):
    tmp = list(map(int, data[i].split()))
    first.append(tmp)

t = firstRow+1
secondRow, secondCol = list(map(int, data[t].split()))
second = []
for i in range(t+1, t+secondRow+1):
    tmp = list(map(int, data[i].split()))
    second.append(tmp)

# firstRow와 secondCol로 범위가 결정됨
result = []
for i in range(firstRow): # first 행 범위
    semi = []
    for j in range(secondCol): # second 열 범위
        tmp = 0
        for k in range(secondRow):
            tmp += first[i][k] * second[k][j]
        semi.append(tmp)
    result.append(semi)

output("\n".join(" ".join(map(str, row)) for row in result) + "\n")
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split()) # 10 4790
lst = []
for i in range(n, 0, -1):
    coin = int(data[i])
    lst.append(coin)

cnt = 0
tries = 0
while k != 0:
    if lst[cnt] > k:
        cnt+=1
        continue
    minusNum = k // lst[cnt]
    k-=minusNum * lst[cnt]
    tries+=minusNum

print(tries)
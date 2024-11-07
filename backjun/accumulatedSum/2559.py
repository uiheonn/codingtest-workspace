# 10 2
# 3 -2 -4 -9 0  3  7  13  8  -3
# 1. 첫항부터 k항까지 더한다
# 2. 하나빼고 하나더하면서 계산한다

import sys

input = sys.stdin.read
data = input().splitlines()

n,k = map(int, data[0].split())
lst = list(map(int, data[1].split()))

temp = [0] * (n - k + 1) # 9
temp[0] = sum(lst[0:k])
res = temp[0]

for i in range(1, n - k + 1): # 1부터 8까지
    res = res - lst[i-1] + lst[i+k-1]
    temp[i] = res
#print("temp : ", temp)
print(max(temp))
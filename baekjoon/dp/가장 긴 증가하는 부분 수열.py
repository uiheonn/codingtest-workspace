import bisect
import sys

# 입력 처리
input = sys.stdin.read
Data = input().splitlines()
n = int(Data[0])
lst = list(map(int, Data[1].split()))

# LIS 계산
dp = []

for num in lst:
    pos = bisect.bisect_left(dp, num)

    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))

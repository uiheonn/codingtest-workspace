import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
lst = []
for i in range(1,n+1):
    lst.append(int(data[i]))

memo = [[-1] * 3 for _ in range(n)]
def dp(level, priorGap):
    global memoBeforeOneStep
    global memoBeforeTwoStep

    if level < 0:
        return 0
    
    if memo[level][priorGap] != -1:
        return memo[level][priorGap]

    tmp = None
    
    if priorGap == 1: # 포도주를 바로 앞 노드에서 마셨다면
        tmp = max(dp(level-2,2), dp(level-3,2)) + lst[level]
    elif priorGap == 2: # 포도주를 바로 앞 노드에서 마시지 않았다면
        tmp = max(dp(level-1,1), dp(level-2,2)) + lst[level]
    memo[level][priorGap] = tmp
    return tmp
        
result = max(dp(n-1,2), dp(n-2,2))

print(result)
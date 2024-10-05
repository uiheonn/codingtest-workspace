import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

pList = []
for i in range(1, n + 1):
    inp = int(data[i])
    pList.append(inp)

# pList = [10, 20, 15, 25, 10, 20]
memoBeforeOneStep = [0 for _ in range(n)]
memoBeforeTwoStep = [0 for _ in range(n)]
def dp(level, gap): # 6번째 계단, 이전에 한칸이동했는지 두칸이동했는지
    global memoBeforeOneStep
    global memoBeforeTwoStep

    if level < 0:
        return 0
    
    tmp = None
    if gap == 1: # 이전에 한칸을 이동했다면
        if memoBeforeOneStep[level] != 0:
            return memoBeforeOneStep[level]
        tmp = dp(level-2, 2) + pList[level]
        memoBeforeOneStep[level] = tmp
    elif gap == 2: # 이전에 두칸을 이동했다면
        if memoBeforeTwoStep[level] != 0:
            return memoBeforeTwoStep[level]
        tmp = max(dp(level-1, 1), dp(level-2, 2)) + pList[level]
        memoBeforeTwoStep[level] = tmp
    
    return tmp

tmp = dp(n-1, 2)

# print(memoBeforeOneStep)
# print(memoBeforeTwoStep)
print(tmp)
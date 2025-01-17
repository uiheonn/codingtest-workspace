import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

dpList = []
for i in range(1, n + 1):
    inp = list(map(int, data[i].split()))
    dpList.append(inp)

#print(dpList) # [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]

triangleList = [[-1] * i for i in range(1, n+1)] # [[-1], [-1, -1], [-1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1, -1]]
triangleList[0][0] = dpList[0][0]

def inForground(level, num): # level은 현재 층, num은 몇번째
    global triangleList

    if triangleList[level][num] != -1:
        return triangleList[level][num]
    
    tmp = None
    if num == 0:
        tmp = inForground(level-1, num) + dpList[level][num]
    elif num == level:
        tmp = inForground(level-1, num-1) + dpList[level][num]
    else:
        tmp = max(inForground(level-1, num-1), inForground(level-1, num)) + dpList[level][num]
    
    triangleList[level][num] = tmp

    return tmp

maxData = 0
for i in range(n):
    cnt = inForground(n-1, i)
    if cnt > maxData:
        maxData = cnt

print(maxData)


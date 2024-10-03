import sys
# 3
# 26 40 83
# 49 60 57
# 13 89 99

# f(x) = min(r(x), g(x), b(x))
# r(x) = min(g(x-1), b(x-1)) + r의 비용
# 1. 해당 식으로 값을 구해나간다
# 2. 메모이제이션을 통해 효율성을 높인다

sys.setrecursionlimit(10**9)

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])

dpList = []
for i in range(1, n + 1):
    inp = list(map(int, data[i].split()))  # [26, 40, 83]
    dpList.append(inp)

def notRgb(rgb):
    if rgb==0:
        return 1,2
    elif rgb==1:
        return 0,2
    else:
        return 0,1

rgbList = [[0] * n for _ in range(3)] # rgb 각각 하나의 항이고 level이 index를 가리킨다

def inForground(rgb, level): # 0, 2
    global rgbList

    if level == 0:
        return dpList[0][rgb]
    
    a,b = notRgb(rgb) # a,b = 1,2

    aData = None
    if rgbList[a][level-1] != 0:
        aData = rgbList[a][level-1]
    else:
        aData = inForground(a, level-1) # 1, 1
        rgbList[a][level-1] = aData
    bData = None
    if rgbList[b][level-1] != 0:
        bData = rgbList[b][level-1]
    else:
        bData = inForground(b, level-1)
        rgbList[b][level-1] = bData

    minData = min(aData, bData)  + dpList[level][rgb]

    return minData

print(min(inForground(0, n-1), inForground(1, n-1), inForground(2, n-1)))
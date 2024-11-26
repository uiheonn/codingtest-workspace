import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.read
data = input().splitlines()
lst = []
n = int(data[0])
for i in range(1,n+1):
    temp = list(map(int, data[i].split()))
    lst.append(temp)

# n = int(input())

# lst = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     lst.append(temp)

def check(divideList, white, blue): # [[1,1],[0,1]]
    m = len(divideList)
    tmp = set()
    for i in range(len(divideList)):
        for j in range(len(divideList[i])):
            tmp.add(divideList[i][j])
    
    if len(tmp) == 2:
        slice1 = [row[: m//2] for row in divideList[: m//2]]
        slice2 = [row[m//2:] for row in divideList[: m//2]]
        slice3 = [row[: m//2] for row in divideList[m//2:]]
        slice4 = [row[m//2:] for row in divideList[m//2:]]
        result1 = check(slice1,white,blue)
        result2 = check(slice2,white,blue)
        result3 = check(slice3,white,blue)
        result4 = check(slice4,white,blue)
        wh = result1[0] + result2[0] + result3[0] + result4[0]
        bl = result1[1] + result2[1] + result3[1] + result4[1]
        return [wh, bl]
    elif tmp.pop() == 1:
        return [white, blue+1]
    else:
        return [white+1, blue]
    
real = check(lst,0,0)

print(real[0])
print(real[1])
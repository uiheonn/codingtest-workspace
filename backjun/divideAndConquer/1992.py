import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
lst = []
for i in range(1,n+1):
    temp = data[i]
    semiLst = []
    for j in range(n):
        semiLst.append(int(temp[j]))
    lst.append(semiLst)

# n = int(input())
# lst = []
# for i in range(n):
#     temp = input()
#     semiLst = []
#     for j in range(n):
#         semiLst.append(int(temp[j]))
#     lst.append(semiLst)

def quad(divideList):
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
        result1 = quad(slice1)
        result2 = quad(slice2)
        result3 = quad(slice3)
        result4 = quad(slice4)
        return '(' + result1 + result2 + result3 + result4 + ')'
    else:
        return str(tmp.pop())

result = quad(lst)
print(result)
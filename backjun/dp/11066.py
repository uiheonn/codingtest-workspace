import itertools

n = int(input())
lst = []
for i in range(n):
    k = int(input())
    semi = list(map(int, input().split()))
    semi.sort()
    lst.append(semi)

def fromListToCom(lst): # [(10,20), (20,30), (30,40)] -> [[10,20], [20,30], [30,40]]
    temp = []
    for i in range(len(lst)):
        tmp = list(lst[i])
        temp.append(tmp)
    return temp

def minusToLst(lst, com): # lst = [40,30,50] com = [40]
    nCb = lst.copy()
    for res in com:
        nCb.remove(res)
    return nCb

def makeStr(nCa):
    minStr = ""
    for i in range(len(nCa)):
        for j in range(len(nCa[i])):
            minStr += str(nCa[i][j]) + "+"
    return minStr

minDict = dict()
def dynamic(lst):
    k = len(lst)
    if k == 1:
        return lst[0]
    # minList = []
    # minData = 21483743
    minminList = []
    for i in range(1,k): # k가 1부터 k-1까지 -> a가 1,2,...,k-1개 선택했을 때 ex. lst =[30,30,40]
        a = i
        nCa = fromListToCom(list(itertools.combinations(lst, a))) # [[30],[30],[40]]
        minList = []
        minStr = makeStr(nCa)
        getStr = minDict.get(minStr,0)
        if getStr != 0:
            return getStr
        
        for j in range(len(nCa)):
            nCaData = nCa[j] # [30]
            nCb = minusToLst(lst, nCaData)
            f1 = dynamic(nCaData)
            if len(nCaData) != 1:
                f1 *= 2
            f2 = dynamic(nCb)
            if len(nCb) != 1:
                f2 *= 2
            tmp = f1 + f2
            minList.append(tmp)
        minDict[minStr] = min(minList)
        minminList.append(minDict[minStr])
    return min(minminList)

result = []
for i in range(n):
    res = dynamic(lst[i])
    result.append(res)

print(minDict)
print("result :", result)
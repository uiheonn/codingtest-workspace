import sys

n = int(input())
lst = []
for i in range(n):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

# input = sys.stdin.read
# data = input().splitlines()
# n = int(data[0])
# lst = []
# for i in range(1, n+1):
#     lst.append(list(map(int, data[i].split())))

# 선을 지나가는 다른 선이 최대값인 경우 -> DP 수행

def check(elec, wholeElec):
    if elec[0] > wholeElec[0] and elec[1] < wholeElec[1]:
        return True
    elif elec[0] < wholeElec[0] and elec[1] > wholeElec[1]:
        return True
    else:
        return False

def dp(lst,count): # 최소횟수를 구하는거니까 count 필요
    ttt = None
    maxLst = []
    for ele in lst: # 각 선을 지나는 선을 구해서 리스트화
        cnt = 0
        for semiEle in lst:
            if check(ele, semiEle):
                cnt+=1
        maxLst.append(cnt)
    maxNum = max(maxLst)
    # print("maxNum : ", maxNum)

    if maxNum == 0:
        return count
    
    tttLst = []
    # print("maxLst : ", maxLst)
    for i in range(len(lst)): # 지나는 선의 최대값을 가지고 DP 수행
        if maxLst[i] == maxNum:
            copyLst = lst.copy()
            copyLst.pop(i)
            # print("copyLst : ", copyLst)
            # print()
            ttt = dp(copyLst, count+1)
        if ttt:
            tttLst.append(ttt)
    # print("tttLst : ", tttLst)
    return min(tttLst)

total = dp(lst,0)
print(total)
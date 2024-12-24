# 10
# 1 6
# 2 8
# 3 2
# 4 9
# 5 5
# 6 10
# 7 4
# 8 1
# 9 7
# 10 3 -> 6 리턴

n = int(input())
lst = []
for i in range(n):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

def check(elec, wholeElec):
    if elec[0] > wholeElec[0] and elec[1] < wholeElec[1]:
        return True
    elif elec[0] < wholeElec[0] and elec[1] > wholeElec[1]:
        return True
    else:
        return False

realCount = 0


while True:
    countLst = []
    maxNum = -1
    maxLoc = None
    for i in range(len(lst)):
        electronic = lst[i]
        count = 0
        for j in range(len(lst)):
            wholeElec = lst[j]
            if check(electronic, wholeElec):
                count+=1
        print(count)
        if count >= maxNum:
            maxNum = count
            maxLoc = i

    print("max locate : ", maxLoc, "max Number : ", maxNum)
    
    if maxNum == 0:
        break

    if maxLoc != None:
        print("delete electronic : ", lst[maxLoc])
        lst.pop(maxLoc)
        realCount+=1

print("lst : ", lst)
print("real count : ", realCount)
import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
lst = []
for i in range(1, n + 1):
    startAndEnd = list(map(int, data[i].split()))
    lst.append(startAndEnd)

leftLst = sorted(lst, key=lambda x:(x[1], x[0]))

def isValid(lst, check): # 이미 스케줄링에 넣은 시간과 중복되는지 확인
    return lst[1] <= check[0]

count = 0
checkLst = []
for i in range(len(leftLst)):
    if not checkLst or isValid(checkLst[-1], leftLst[i]):
        checkLst.append(leftLst[i])

print(len(checkLst))
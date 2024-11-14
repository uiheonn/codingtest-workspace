import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
lst = []
for i in range(1,n+1):
    temp = list(map(int, data[i].split()))
    lst.append(temp)

# n = int(input())
# lst = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     lst.append(temp)

global minus
global zero
global one
minus = 0
zero = 0
one = 0

def divide(divideList):
    global minus
    global zero
    global one

    m = len(divideList)
    tmp = set()
    for i in range(m):
        for j in range(len(divideList[i])):
            tmp.add(divideList[i][j])

    popData = tmp.pop()

    if m == 3 and len(tmp) >= 1: # 3x3이면서 모두 같은 종이가 아닌 경우
        for i in range(m):
            for j in range(len(divideList[i])):
                res = divideList[i][j]
                if res == -1:
                    minus+=1
                elif res == 0:
                    zero+=1
                else:
                    one+=1
    elif m != 3 and len(tmp) >= 1:
        cnt = m//3
        slice1 = [row[:cnt] for row in divideList[:cnt]] # 좌상단
        slice2 = [row[cnt:cnt*2] for row in divideList[:cnt]] # 좌중간
        slice3 = [row[cnt*2:] for row in divideList[:cnt]] # 좌하단
        slice4 = [row[:cnt] for row in divideList[cnt:cnt*2]] # 중상단
        slice5 = [row[cnt:cnt*2] for row in divideList[cnt:cnt*2]] # 중간
        slice6 = [row[cnt*2:] for row in divideList[cnt:cnt*2]] # 중하단
        slice7 = [row[:cnt] for row in divideList[cnt*2:]] # 우상단
        slice8 = [row[cnt:cnt*2] for row in divideList[cnt*2:]] # 우중간
        slice9 = [row[cnt*2:] for row in divideList[cnt*2:]] # 우하단
        divide(slice1)
        divide(slice2)
        divide(slice3)
        divide(slice4)
        divide(slice5)
        divide(slice6)
        divide(slice7)
        divide(slice8)
        divide(slice9)
    elif popData == 1:
        one+=1
    elif popData == 0:
        zero+=1
    elif popData == -1:
        minus+=1

divide(lst)

print(minus)
print(zero)
print(one)
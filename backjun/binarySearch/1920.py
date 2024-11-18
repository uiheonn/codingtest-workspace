n = int(input())
global nData
nData = list(map(int, input().split()))
m = int(input())
mData = list(map(int, input().split()))

nData.sort()

def check(tmp):
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if nData[mid] == tmp:
            return True
        elif nData[mid] < tmp:
            left = mid + 1
        else:
            right = mid
    return False

for i in range(len(mData)):
    if check(mData[i]):
        print(1)
    else:
        print(0)
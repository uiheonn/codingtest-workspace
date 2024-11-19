import sys

input = sys.stdin.read
output = sys.stdout.write

data = input().splitlines()
n = int(data[0])
nData = list(map(int, data[1].split()))
m = int(data[2])
mData = list(map(int, data[3].split()))

# n = int(input())
# nData = list(map(int, input().split()))
# m = int(input())
# mData = list(map(int, input().split()))

nHash = {}
for i in range(n):
    nHash[nData[i]] = nHash.get(nData[i],0) + 1

arr = []
for i in range(m):
    tmp = nHash.get(mData[i],0)
    if tmp:
        #print(tmp,end=" ")
        arr.append(tmp)
    else:
        arr.append(0)
        #print(0,end=" ")

output(" ".join(map(str, arr)))
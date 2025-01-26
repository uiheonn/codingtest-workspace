import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
lst = list(map(int, data[1].split()))
k = int(data[2])

# n = int(input())
# lst = list(map(int, input().split()))
# k = int(input())

lst.sort()
l, r = 0, n-1

count = 0
while l < r:
    tmp = lst[l] + lst[r]
    if tmp == k:
        count+=1
        r-=1
        l+=1
    elif tmp > k:
        r-=1
    else:
        l+=1

print(count)
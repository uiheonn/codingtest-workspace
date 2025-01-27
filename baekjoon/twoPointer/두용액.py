n = int(input())
lst = list(map(int, input().split()))
lst.sort()

l,r = 0, n-1
a, b = 0, n-1
minAbs = 2100000000
while l < r:
    tmp = abs(lst[l] + lst[r])
    if tmp < minAbs:
        minAbs = tmp
        a,b = l,r
    if abs(lst[l]) > abs(lst[r]):
        l+=1
    else:
        r-=1

print(lst[a], lst[b])
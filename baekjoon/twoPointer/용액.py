import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
# print(lst)

l = 0
r = n-1

result_l, result_r = 0,0
min_num = 2000000001
while l < r:
    tmp = lst[l] + lst[r]
    if abs(tmp) <= min_num:
        min_num = abs(tmp)
        result_l = lst[l]
        result_r = lst[r]
    if tmp < 0:
        l+=1
    elif tmp > 0:
        r-=1
    else:
        break
print(result_l, result_r)
# 두가지 선택이 가능
# 1. 겹치지 않는 1칸 앞의 스티커를 선택
# 2. 2칸 앞의 스티커 중 둘 다 선택

import sys
sys.setrecursionlimit(10 ** 9)

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    first_sticker = list(map(int, input().split()))
    second_sticker = list(map(int, input().split()))
    s1 = [-1 for _ in range(n)]
    s2 = [-1 for _ in range(n)]
    #print(lst)
    s1[0] = first_sticker[0]
    s2[0] = second_sticker[0]
    for i in range(1,n):
        s1_i = s2[i-1] + first_sticker[i]
        s2_i = s1[i-1] + second_sticker[i]
        s1_i1 = -1
        s2_i1 = -1
        if i != n-1:
            s1_i1 = max(s1[i-1] + first_sticker[i+1], s2[i-1] + first_sticker[i+1])
            s2_i1 = max(s1[i-1] + second_sticker[i+1], s2[i-1] + second_sticker[i+1])
        
        if s1_i > s1[i]:
            s1[i] = s1_i
        if s2_i > s2[i]:
            s2[i] = s2_i
        if i != n-1 and s1_i1 > s1[i+1]:
            s1[i+1] = s1_i1
        if i != n-1 and s2_i1 > s2[i+1]:
            s2[i+1] = s2_i1
        
    print(max(s1[-1], s2[-1]))
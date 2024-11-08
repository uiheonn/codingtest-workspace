# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14
# (1,4)(5,7)(8,11)(12,14)

n = int(input())
lst = []
for i in range(1, n + 1):
    startAndEnd = list(map(int, input().split()))
    lst.append(startAndEnd)

print(lst)

real = []
for i in range(n):
    semi = []
    semi.append(lst[i])
    for j in range(i+1, n):
        if semi[-1][1] < lst[j][0]:
            semi.append(lst[j])
    real.append(semi)

print(real)
n = int(input())
lst = list(map(int, input().split()))
lst.sort()

real_result = []
tmp = 0
for i in range(n):
    tmp += lst[i]
    real_result.append(tmp)

print(sum(real_result))
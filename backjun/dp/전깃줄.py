import sys

# LIS로 해결해야함
# 왼쪽 cost 기준으로 정렬
# 오른쪽 cost를 통해 LIS를 구하고 len(lst) - len(LIS)를 리턴하면 정답

# n = int(input())
# lst = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     lst.append(tmp)


input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
lst = []
for i in range(1, n+1):
    lst.append(list(map(int, data[i].split())))
lst.sort()

cnt_lst = []
lis_lst = []
for i in range(n):
    cnt_lst.append(lst[i][1])

for i in range(n):
    cnt = 1
    for j in range(i):
        if cnt_lst[j] < cnt_lst[i]:
            cnt = max(lis_lst[j]+1, cnt)
    lis_lst.append(cnt)

print(n - max(lis_lst))
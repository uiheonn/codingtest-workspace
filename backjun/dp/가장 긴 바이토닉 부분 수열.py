import sys

# n = int(input())
# lst = list(map(int, input().split()))

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
lst = list(map(int, data[1].split()))

cnt_list = []
for i in range(n):
    cnt = 1
    for j in range(i):
        if lst[j] < lst[i]:
            cnt = max(cnt_list[j]+1, cnt)
    cnt_list.append(cnt)

cnt_list_reverse = []
reverse_lst = lst.reverse()
for i in range(n):
    cnt = 1
    for j in range(i):
        if lst[j] < lst[i]:
            cnt = max(cnt_list_reverse[j]+1, cnt)
    cnt_list_reverse.append(cnt)

cnt_list_reverse.reverse()

result = []
for k in range(n):
    result.append(cnt_list[k] + cnt_list_reverse[k] - 1)

print(max(result))
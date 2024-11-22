from queue import PriorityQueue
import sys

# n = int(input())
# lst = []
# for i in range(n):
#     d = int(input())
#     lst.append(d)

input = sys.stdin.read
output = sys.stdout.write
data = input().splitlines()
n = int(data[0])
lst = []
for i in range(1,n+1):
    lst.append(int(data[i]))

pq = PriorityQueue()
result = []
for i in range(n):
    tmp = lst[i]
    if tmp == 0: # 자연수가 아닌 경우
        if pq.empty():
            result.append(0)
        else:
            result.append(pq.get() * (-1))
    else: # 자연수인 경우 -> 내림차순 정렬 기준으로 추가
        pq.put(tmp * (-1))

output("\n".join(map(str, result)))
from queue import PriorityQueue
import sys

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))

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
    if tmp == 0:
        if pq.empty():
            result.append(0)
        else:
            result.append(pq.get())
    else:
        pq.put(tmp)

output("\n".join(map(str, result)))
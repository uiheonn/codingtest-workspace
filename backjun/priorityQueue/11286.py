from queue import PriorityQueue
import sys

output = sys.stdout.write
# n = int(input())
# lst = []
# for i in range(n):
#     d = int(input())
#     lst.append(d)

input = sys.stdin.read
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
            res = pq.get()
            if res[1] == False:
                result.append(res[0] * -1)
            else:
                result.append(res[0])
    else:
        if tmp > 0:
            pq.put((abs(tmp), True))
        else:
            pq.put((abs(tmp), False))

output("\n".join(map(str, result)))
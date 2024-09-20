from collections import deque

queueStackSize = int(input())

queueStack = input().split() # ['0', '1', '1', '0']

queueStackData = input().split() # ['1', '2', '3', '4']

newDataSize = int(input())

newData = input().split() # ['2', '4', '7']

dq = deque()

for i in range(queueStackSize - 1, -1, -1):
    if len(dq) == newDataSize:
        break
    if queueStack[i] == '0':
        dq.append(queueStackData[i])

if len(dq) < newDataSize:
    for i in range(0, newDataSize - len(dq)):
        dq.append(newData[i])

print(' '.join(dq))

# 알고리즘 요약
# 0. 큐(0)이면 값이 변경, 스택이면(1) 그대로 빠져나감
# 1. 끝부터 0인 원소를 뺀다
# 2. 0인 개수가 M보다 작으면 M - 0의 개수 만큼 수열도 빼서 합친다
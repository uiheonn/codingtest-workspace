import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

total = int(data[0])
dq = deque()
result = []

for i in range(1, total + 1):
    inputWord = data[i].split()
    if inputWord[0] == 'push':
        dq.append(inputWord[1])
    elif inputWord[0] == 'pop':
        if dq:
            result.append(dq.popleft())
        else:
            result.append(-1)
    elif inputWord[0] == 'size':
        result.append(len(dq))
    elif inputWord[0] == 'empty':
        if dq:
            result.append(0)
        else:
            result.append(1)
    elif inputWord[0] == 'front':
        if dq:
            result.append(dq[0])
        else:
            result.append(-1)
    elif inputWord[0] == 'back':
        if dq:
            result.append(dq[-1])
        else:
            result.append(-1)

sys.stdout.write("\n".join(map(str, result)) + "\n")
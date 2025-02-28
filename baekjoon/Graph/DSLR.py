import collections
import sys

def to_left(num):
    tmp = str(num)
    while len(tmp) != 4:
        tmp = '0' + tmp
    tmp = tmp[1:] + tmp[0]
    return int(tmp)

def to_right(num):
    tmp = str(num)
    while len(tmp) != 4:
        tmp = '0' + tmp
    tmp = tmp[-1] + tmp[:3]
    return int(tmp)

input = sys.stdin.readline
n = int(input())
result = []
for i in range(1,n+1):
    a,b = map(int, input().split())
    visited = [False for _ in range(10001)]
    queue = collections.deque()
    queue.append([a,""])
    visited[a] = True

    while len(queue) != 0:
        # print("queue : ", queue)
        num, string = queue.popleft()

        d = (2 * num) % 10000
        if d == b:
            result.append(string + "D")
            break
        if not visited[d]:
            queue.append([d,string+"D"])
            visited[d] = True
        s = (num - 1) % 10000
        if s == b:
            result.append(string + "S")
            break
        if not visited[s]:
            queue.append([s,string+"S"])
            visited[s] = True
        l = to_left(num)
        if l == b:
            result.append(string + "L")
            break
        if not visited[l]:
            queue.append([l,string+"L"])
            visited[l] = True
        r = to_right(num)
        if r == b:
            result.append(string + "R")
            break
        if not visited[r]:
            queue.append([r,string+"R"])
            visited[r] = True

sys.stdout.write("\n".join(map(str, result)))
# 2 162 - 2 -> 4 -> 8 -> 81 -> 162
# 최단 횟수 -> BFS
import collections

start, end = map(int, input().split())
#visited = [False for _ in range(end+1)]
visited = []
queue = collections.deque()
queue.append([start,1])
# visited[start] = True
visited.append(start)
isOutput = True

while len(queue) != 0:
    tmp,count = queue.popleft()
    # print("tmp : ", tmp)
    # print("count : ", count)
    # print()
    if tmp == end:
        isOutput = False
        print(count)
        break
    a,b = tmp * 2, tmp * 10 + 1
    if a <= end and a not in visited:
        queue.append([a,count+1])
        visited.append(a)
    if b <= end and b not in visited:
        queue.append([b,count+1])
        visited.append(b)
    
if isOutput:
    print(-1)
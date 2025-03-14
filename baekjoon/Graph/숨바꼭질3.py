import collections

n,k = map(int, input().split())

queue =  collections.deque()
mx = max(n,k)
visited = [100001 for _ in range(2 * mx + 1)]

queue.append([n,0])
visited[n] = 0

while len(queue) != 0:
    location, cost = queue.popleft()
    
    minus = location-1
    if 0 <= minus < 2*mx+1:
        if cost+1 < visited[minus]:
            queue.append([minus,cost+1])
            visited[minus] = cost+1
    plus = location+1
    if 0 <= plus < 2*mx+1:
        if cost+1 < visited[plus]:
            queue.append([plus,cost+1])
            visited[plus] = cost+1
    multi = location * 2
    if 0 <= multi < 2*mx+1:
        if cost < visited[multi]:
            queue.append([multi,cost])
            visited[multi] = cost
print(visited[k])
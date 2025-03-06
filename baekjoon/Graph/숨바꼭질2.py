import collections

n,k = map(int, input().split())

queue =  collections.deque()
mx = max(n,k) * 2 + 1
visited = [[False,100001] for _ in range(2 * mx + 1)]
queue.append([n,0])
visited[n] = [True,0]
real_location = -1
reaul_cost = -1
best_cases = 1

while len(queue) != 0:
    location, cost = queue.popleft()

    if location == k:
        real_location = location
        real_cost = cost
        break
    
    minus = location-1
    if 0 <= minus < mx:
        if not visited[minus][0] or visited[minus][1] >= cost+1:
            queue.append([minus,cost+1])
            visited[minus] = [True, cost+1]
    plus = location+1
    if 0 <= plus < mx:
        if not visited[plus][0] or visited[plus][1] >= cost+1:
            queue.append([plus,cost+1])
            visited[plus] = [True, cost+1]
    multi = location * 2
    if 0 <= multi < mx:
        if not visited[multi][0] or visited[multi][1] >= cost+1:
            queue.append([multi, cost+1])
            visited[multi] = [True, cost+1]


for ele in queue:
    if ele[0] == real_location and ele[1] == real_cost:
        best_cases+=1

print(real_cost)
print(best_cases)